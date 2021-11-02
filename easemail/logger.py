import logging
import os


class Logger():
    """
    Logger object to capture db failures and mailing failures locally
    """
    def __init__(self, log_name: str, log_directory: str, extension: str="csv", delimiter: str="\t"):
        self.log_name = log_name
        self.extension = extension
        self.delimiter = delimiter

        if not log_directory:
            log_directory = os.getcwd()
        else:
            os.makedirs(log_directory, exist_ok=True)
        
        self.log_path = os.path.join(
            log_directory, log_name + "." + extension)

        self.logger = self._build_logger()
    
    def _build_logger(self):
        """
        Build logger object with tab separated rows as:
        <time levelname message> 
        """
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)

        formatter = logging.Formatter(
            f"%(asctime)s{self.delimiter}%(levelname)s{self.delimiter}%(message)s",
            "%Y-%m-%d %H:%M:%S")
        
        if len(logger.handlers) == 0:
            file_handler = logging.FileHandler(self.log_path)
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

        return logger

    def log_db_fail(self):
        self.logger.error("DB_FAIL")

    def log_email_fail(self, recipient_id: int, attempt_no: int):
        self.logger.error(f"EMAIL_FAIL{self.delimiter}{recipient_id}{self.delimiter}{attempt_no}")

    def log_email_pass(self, recipient_id: int, attempt_no: int):
        self.logger.info(f"EMAIL_PASS{self.delimiter}{recipient_id}{self.delimiter}{attempt_no}")


if __name__ == "__main__":
    logger = Logger(
        log_name="test_run",
        log_directory="env")

    logger.log_db_fail()
    logger.log_email_pass(recipient_id=123132, attempt_no=2)
    logger.log_email_fail(recipient_id=1123213, attempt_no=1)