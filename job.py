import os
import datapipelines
import mailer
from logger import Logger

def first_attempt_job(
    datapipeline: datapipelines.Pipeline,
    email_builder: mailer.SurveyEmailBuilder,
    mailer: mailer.EmailSender,
    local_logger: Logger
    ):
    """
    proceed first reminder
    """
    survey_results = datapipeline.get_first_attempt_mailing()

    for survey in survey_results:
        if survey.days_since >= 7: # hardcoded crap
            email = email_builder.build(survey)
            success = mailer.send(email, debug_mode=True)

            if success:
                local_logger.log_email_pass(survey.recipient_id, 1)
            else:
                local_logger.log_email_fail(survey.recipient_id, 1)

            datapipeline.update_first_attempt(survey.recipient_id, success)


if __name__ == "__main__":
    ### config part
    db_path = os.path.join("env", "testdb.sqlite3")
    html_template_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "email_template.html")
    subject = "Projekt EASE - din egen strategi"
    with open(html_template_path, "r") as fin:
        html_template = fin.read()

    email_sender = os.environ.get('EMAIL_USER')
    email_pass = os.environ.get('EMAIL_PASS')
    server = 'smtp.aau.dk'
    
    # extraction from DB
    datapipeline = datapipelines.LocalSQLPipeline(db_path)
    
    email_builder = mailer.HTMLSurveyEmailBuilder(
        email_sender, html_template, subject)
    sender = mailer.EmailSender(
        email_sender, email_pass, server)

    local_logger = Logger(
        log_name="job_log",
        log_directory="env"
    )
    first_attempt_job(datapipeline, email_builder, sender, local_logger)