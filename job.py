import os
from easemail import datasets, builder, logger, mailer


TEMPLATE_DIR = "email_templates"


def get_email_template(name: str):
    """
    Load test templates
    """
    path = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        TEMPLATE_DIR,
        name
    )
    if os.path.exists(path):
        with open(path, "r") as fin:
            return fin.read()
    else:
        raise FileExistsError("File does not exist: ", path)


def first_attempt_job(
    jdataset: datasets.SurveyDataset,
    jbuilder: builder.SurveyEmailBuilder,
    jmailer: mailer.EmailSender,
    jlogger: logger.Logger,
    debug_mode=True):
    """
    proceed first reminder
    """
    survey_results = jdataset.get_unsent_survey_results()
    
    surveys_to_process = [s for s in survey_results if s.days_since_done >= 7]
    emails_to_send = [jbuilder.build(s) for s in surveys_to_process]

    for email, survey in zip(emails_to_send, surveys_to_process):
        try:
            jmailer.send([email], debug_mode)
            jlogger.log_email_pass(survey.recipient_id, 1)

            print("LOG_TO_DB_PASS")
            #jdataset.update_first_attempt(survey.recipient_id, success=False) 
        except mailer.MailingError:
            print("CRUSH!")
            jlogger.log_email_fail(survey.recipient_id, 1)
            print("LOG_TO_DB_TRUE")
            #jdataset.update_first_attempt(survey.recipient_id, success=False) 


if __name__ == "__main__":
    ### config part
    db_path = os.path.join("env", "matching_testdb.sqlite3")
    db_url = f'sqlite:///{db_path}'

    html_template = get_email_template("email_template.html")
    text_template = get_email_template("email_template.txt")

    subject = "Projekt EASE - din egen strategi"

    email_sender = os.environ.get('EMAIL_USER')
    email_pass = os.environ.get('EMAIL_PASS')
    server = 'smtp.aau.dk'
    
    jdataset = datasets.SQLAlchemyDataset(db_url)

    jbuilder = builder.HTMLSurveyEmailBuilder(
        html_template,
        email_sender,
        subject
    )
    jbuilder = builder.TextSurveyEmailBuilder(
        text_template,
        email_sender,
        subject
    )

    jmailer = mailer.EmailSender(
        email_sender,
        email_pass,
        server
    )

    jlogger = logger.Logger(
        log_name="job_log",
        log_directory="env"
    )

    debug_mode=True
    first_attempt_job(jdataset, jbuilder, jmailer, jlogger, debug_mode)