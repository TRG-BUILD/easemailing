import os
import json
import argparse

from easemail import datasets, builder, logger, mailer
from teams_logger import TeamsHandler


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


def get_email_template(name: str, template_dir: str):
    """
    Load email template content from file
    """
    path = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        template_dir,
        name
    )
    if os.path.exists(path):
        with open(path, "r") as fin:
            return fin.read()
    else:
        raise FileExistsError("File does not exist: ", path)


def send_reminders(
        attempt_no: int,
        max_days: int,
        jdataset: datasets.SurveyDataset,
        jbuilder: builder.SurveyEmailBuilder,
        jmailer: mailer.EmailSender,
        jlogger: logger.Logger = None,
        debug_mode: bool = True):
    """
    Send mail reminder based on the surbey database
    """
    survey_results = jdataset.get_unsent_survey_results()
    # TODO: check attempt_no == attempt_no -1
    surveys_to_process = [s for s in survey_results if
                          s.days_since_done >= max_days and s.succesfull_attempt == attempt_no - 1]
    emails_to_send = [jbuilder.build(s) for s in surveys_to_process]

    count = {'fail': 0, 'succes': 0}
    for email, survey in zip(emails_to_send, surveys_to_process):
        try:
            jmailer.send([email], debug_mode)
            if jlogger:
                jlogger.log_email_pass(survey.recipient_id, attempt_no)
                count['succes'] += 1
            jdataset.update_attempt(attempt_no, survey.recipient_id, success=True)
        except mailer.MailingError:
            if jlogger:
                jlogger.log_email_fail(survey.recipient_id, attempt_no)
                count['fail'] += 1
            jdataset.update_attempt(attempt_no, survey.recipient_id, success=False)
    else:
        out = f"Succes udsendt: {count['succes']}, fejlet: {count['fail']}"
        if jlogger:
            jlogger.logger.info(out)
        else:
            print(out)

def main(cfg: dict):
    """
    Run mailing pipeline
    """
    subject = cfg["email_subject"]
    email_sender = cfg["email_sender"]
    email_pass = cfg["email_pass"]
    email_server = cfg["email_server"]
    email_type = cfg["email_type"]
    email_template = get_email_template(
        cfg["email_template"],
        cfg["email_template_dir"])
    survey_db_url = cfg["survey_db_url"]
    email_in_debug_mode = cfg["email_in_debug_mode"]
    log_name = cfg["log_name"]
    log_folder = cfg["log_dir"]
    survey_id = cfg["survey_id"]

    # build dataset handler
    jdataset = datasets.SQLAlchemyDataset(survey_db_url, survey_id)

    # build email composer
    if email_type == "html":
        jbuilder = builder.HTMLSurveyEmailBuilder(
            email_template,
            email_sender,
            subject
        )
    else:
        jbuilder = builder.TextSurveyEmailBuilder(
            email_template,
            email_sender,
            subject
        )

    # build mail sender
    jmailer = mailer.EmailSender(
        email_sender,
        email_pass,
        email_server,
        tls_port=25
    )

    # build logger
    jlogger = logger.Logger(log_name, log_folder)

    # Adding teamshandler to jlogger
    th = TeamsHandler(url=cfg["teams_webhook"], level=logger.logging.INFO)
    jlogger.logger.addHandler(th)

    # run 1st attempt for those with 7+ days
    send_reminders(1, 7,
                   jdataset,
                   jbuilder,
                   jmailer,
                   jlogger,
                   email_in_debug_mode
                   )

    # run 2nd attempt for those with 45+ days
    send_reminders(2, 45,
                   jdataset,
                   jbuilder,
                   jmailer,
                   jlogger,
                   email_in_debug_mode
                   )


if __name__ == "__main__":
    ag = argparse.ArgumentParser()
    ag.add_argument("-c", "--config", required=True, type=str, help=
    "mailer job configuration file")
    args = ag.parse_args()
    ### config part
    cfg = read_job_config(args.config)
    main(cfg)

