import os
import json
import argparse

from easemail import datasets, builder, logger, mailer


def read_job_config(filename: str) -> dict:
    """
    Converts JSON config to dictionary. Secure info like email sender and
    pass are obtained from environmental variables EMAIL_USER and EMAIL_PASS
    """
    cfg = {
        "email_pass": os.environ.get('EMAIL_PASS')
    }

    with open(filename, "r") as fin:
        cfg.update(json.load(fin))
    return cfg


def check_surveyresult(
        attempt_no: int,
        max_days: int,
        jdataset: datasets.SurveyDataset
        ):
    """
    Send mail reminder based on the surbey database
    """
    survey_results = jdataset.get_unsent_survey_results()
    # TODO: check attempt_no == attempt_no -1
    surveys_to_process = [s for s in survey_results if
                          s.days_since_done >= max_days and s.succesfull_attempt == attempt_no - 1]

    print("Answer_id", "Email", "Days_since_done", "Succesfull Attempt")
    for survey in surveys_to_process:
        print(survey.recipient_id, survey.recipient_email, survey.days_since_done, survey.succesfull_attempt)

def main(cfg: dict):
    """
    Run mailing pipeline
    """
    subject = cfg["email_subject"]
    survey_db_url = cfg["survey_db_url"]
    survey_id = cfg["survey_id"]

    # build dataset handler
    jdataset = datasets.SQLAlchemyDataset(survey_db_url, survey_id)


    print("Recipients 7 days reminder")
    # run 1st attempt for those with 7+ days
    check_surveyresult(1, 7,
                   jdataset,
                   )
    print("Recipients 45 days reminder")
    # run 2nd attempt for those with 45+ days
    check_surveyresult(2, 45,
                   jdataset,
                   )


if __name__ == "__main__":
    ag = argparse.ArgumentParser()
    ag.add_argument("-c", "--config", required=True, type=str, help=
    "Get list of recipients")
    args = ag.parse_args()
    ### config part
    cfg = read_job_config(args.config)
    main(cfg)
