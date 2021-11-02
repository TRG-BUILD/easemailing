import os
import json
from easemail import datasets, builder, logger, mailer


def read_job_config(filename: str) -> dict:
    """
    Converts JSON config to dictionary. Secure info like email sender and
    pass are obtained from environmental variables EMAIL_USER and EMAIL_PASS
    """
    cfg = {
        "email_sender": os.environ.get('EMAIL_USER'),
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
    jlogger: logger.Logger=None,
    debug_mode: bool=True):
    """
    Send mail reminder based on the surbey database
    """
    survey_results = jdataset.get_unsent_survey_results()
    
    surveys_to_process = [s for s in survey_results if s.days_since_done >= max_days]
    emails_to_send = [jbuilder.build(s) for s in surveys_to_process]

    for email, survey in zip(emails_to_send, surveys_to_process):
        try:
            jmailer.send([email], debug_mode)
            if jlogger:
                jlogger.log_email_pass(survey.recipient_id, attempt_no)

            jdataset.update_attempt(attempt_no, survey.recipient_id, success=True)
        except mailer.MailingError:
            if jlogger:
                jlogger.log_email_fail(survey.recipient_id, attempt_no)
            jdataset.update_attempt(attempt_no, survey.recipient_id, success=False)


if __name__ == "__main__":
    ### config part
    cfg = read_job_config("jobcfg.json")
    
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

    # build dataset handler
    jdataset = datasets.SQLAlchemyDataset(survey_db_url)
    
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
        email_server
    )

    # build logger
    jlogger = logger.Logger(log_name, log_folder)

    # run job
    send_reminders(1, 7,
        jdataset,
        jbuilder,
        jmailer,
        jlogger, 
        email_in_debug_mode
    )

    send_reminders(2, 45,
        jdataset,
        jbuilder,
        jmailer,
        jlogger, 
        email_in_debug_mode
    )