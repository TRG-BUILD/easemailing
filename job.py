import os
import qextractor
import qformatter
#import qmailer


def first_attempt_job(extractor, formatter, emailcomposer, mailer):
    """
    proceed first reminder
    """
    dbdata = extractor.get_first_attempt_mailing()
    surveydata = formatter.format(dbdata)

    for survey in surveydata:
        recipient_id, email = emailcomposer.build_email(survey)

        success = mailer.send(email)
        extractor.update_first_attempt(recipient_id, success)


def second_attempt_job(extractor, formatter, emailcomposer=None, mailer=None):
    """
    proceed second reminder
    """
    dbdata = extractor.get_second_attempt_mailing()
    surveydata = formatter.format(dbdata)

    for survey in surveydata:
        recipient_id, email = emailcomposer.build_email(survey)

        success = mailer.send(email)
        extractor.update_second_attempt(recipient_id, success)


if __name__ == "__main__":
    db_path = os.path.join("env", "testdb.sqlite3")

    extractor = qextractor.LocalSQLiteExtractor(db_path)
    formatter = qformatter.SQLiteResultFormatter()
    #emailcomposer = qmailer.EaseEmailComposer(html_template)
    #qmailer = qmailer.EmailSender(EMAIL_USER, EMAIL_PASS, 'smtp.aau.dk', tls_port=587)

    first_attempt_job(extractor, formatter, emailcomposer=None, mailer=None)
    second_attempt_job(extractor, formatter, emailcomposer=None, mailer=None)