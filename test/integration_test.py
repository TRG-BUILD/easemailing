import os
import csv

from easemail import datasets, builder, logger, mailer
import job
import testdb_build


def get_data_path(filename: str):
    return os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "data",
        filename
    )

def assert_log_size(jlogger: logger.Logger, expected_size: int):
    """
    Compare the size of the log to the expected size
    """
    with open(jlogger.log_path, "r") as csvfile:
        log_reader = csv.reader(csvfile, delimiter=jlogger.delimiter)
        assert len([row for row in log_reader]) == expected_size

def main(config: str):
    cfg = job.read_job_config(config)
    
    subject = cfg["email_subject"]
    email_sender = cfg["email_sender"]
    email_pass = cfg["email_pass"]
    email_server = cfg["email_server"]
    email_type = cfg["email_type"]
    email_template = job.get_email_template(
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
    job.send_reminders(1, 7,
        jdataset,
        jbuilder,
        jmailer,
        jlogger, 
        email_in_debug_mode
    )

    job.send_reminders(2, 45,
        jdataset,
        jbuilder,
        jmailer,
        jlogger, 
        email_in_debug_mode
    )

    # tests
    assert len(jdataset.get_unsent_survey_results()) == 0
    assert_log_size(jlogger, expected_size=8)

if __name__ == "__main__":
    ### Create database
    config = "integrationcfg.json"
    db_sql = get_data_path("build_matching_testdb.sql")
    db_path = get_data_path("matching_testdb.sqlite3")
    log_path = "integration_log.csv"

    try:
        testdb_build.build_testdb_snapshot(db_path, db_sql)
        main(config)
    except Exception as e:
        raise e
    finally:
        os.remove(log_path)
        testdb_build.delete_testdb_snapshot(db_path)