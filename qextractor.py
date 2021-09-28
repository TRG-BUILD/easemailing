import sqlite3
from abc import ABC, abstractmethod

class QuestinaireExtractor(ABC):
    @abstractmethod
    def get_first_attempt_mailing(self) -> list:
        """
        Returns emails of recipients that want email strategy,
        a reminder and have not received mail before
        """

    @abstractmethod
    def get_second_attempt_mailing(self) -> list:
        """
        Returns emails of recipients that want email strategy,
        a reminder and have already received first mail
        """

    @abstractmethod
    def update_first_attempt(self, recipient_id: int, sucess: bool):
        """
        Updates the date of succesul or fail attempt to send a first email
        """

    @abstractmethod
    def update_second_attempt(self, recipient_id: int, sucess: bool):
        """
        Updates the date of succesul or fail attempt to send a second email
        """


class LocalSQLiteExtractor(QuestinaireExtractor):
    """
    Extract and update local sqlite3 questinoare database
    """
    def __init__(self, db):
        self.db = db
        self.conn = sqlite3.connect(self.db)
        self.cursor = self.conn.cursor()

    def get_first_attempt_mailing(self):
        with self.conn:
            result = self.cursor.execute(
                """
                SELECT
                    respondentid,
                    days_since,
                    closetime,
                    today,
                    situation1_text,
                    situation2_text,
                    situation3_text,
                    strategi1_text,
                    strategi2_text,
                    strategi3_text,
                    email_strategi
                FROM
                    strategi_mailings
                """
            )
        return result.fetchall()

    def get_second_attempt_mailing(self) -> list:
        """
        Returns emails of recipients that want email strategy,
        a reminder and have already received first mail
        """
        return []

    def update_first_attempt(self, recipient_id: int, sucess: bool):
        """
        Updates the date of succesul or fail attempt to send a first email

        -- Succes fuld udsending ved første
        UPDATE answer3 set strategi_mail_send_first = datetime('now') WHERE respondentid = {respondentid}

        -- Ved fejl udsending, indsæt seneste forsøgte dato
        UPDATE answer3 set strategi_mail_send_first_failed = datetime('now') WHERE respondentid = {respondentid}
        """
        pass

    def update_second_attempt(self, recipient_id: int, sucess: bool):
        """
        Updates the date of succesul or fail attempt to send a second email

        -- Success for udsending ved anden
        UPDATE answer3 set strategi_mail_send_second = datetime('now') WHERE respondentid = {respondentid}

        -- Ved fejl udsending, indsæt seneste forsøgte dato
        UPDATE answer3 set strategi_mail_send_second_failed = datetime('now') WHERE respondentid = {respondentid}
        """
        pass


if __name__ == "__main__":
    sqlm = LocalSQLiteExtractor(db="env/testdb.sqlite3")
    print(sqlm.get_first_attempt_mailing())



