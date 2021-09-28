import os
import qextractor
import qformatter
import qmailer


def first_attempt_job(
    extractor: qextractor.QuestinaireExtractor,
    formatter: qformatter.ResultFormatter,
    email_builder: qmailer.SurveyEMailBuilder,
    mailer: qmailer.EMailSender
    ):
    """
    proceed first reminder
    """
    db_rows= extractor.get_first_attempt_mailing()
    survey_results = formatter.format(db_rows)

    for survey in survey_results:
        if survey.days_since >= 7:
            email = email_builder.build(survey)
            success = mailer.send_localhost(email)
            extractor.update_first_attempt(survey.recipient_id, success)


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
    extractor = qextractor.LocalSQLiteExtractor(db_path)
    formatter = qformatter.SQLiteResultFormatter()
    
    email_builder = qmailer.HTMLSurveyEmailBuilder(email_sender, html_template, subject)
    mailer = qmailer.EmailSender(email_sender, email_pass, server)

    first_attempt_job(extractor, formatter, email_builder, mailer)