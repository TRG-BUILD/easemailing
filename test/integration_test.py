import os
import json


from easemail import datasets, builder, logger, mailer
import job

import testdb_build

def get_data_path(filename: str):
    return os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "data",
        filename
    )


if __name__ == "__main__":
    ### Create database
    db_sql = get_data_path("build_matching_testdb.sql")
    db_path = get_data_path("matching_testdb.sqlite3")
    db_url = f'sqlite:///{db_path}'
    testdb_build.build_testdb_snapshot(db_path, db_sql)

    ### config part
    cfg = job.read_job_config("integrationcfg.json")
    
    subject = cfg["email_subject"]
    email_sender = cfg["email_sender"]
    email_pass = cfg["email_pass"]
    email_server = cfg["email_server"]
    email_type = cfg["email_type"]
    email_template = job.get_email_template(
        cfg["email_template"],
        cfg["email_template_dir"])
    survey_db_url = db_url
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
    job.first_attempt_job(
        jdataset,
        jbuilder,
        jmailer,
        jlogger, 
        email_in_debug_mode
    )

    testdb_build.delete_testdb_snapshot(db_path)