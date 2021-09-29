import sqlite3
from abc import ABC, abstractmethod


class DatasetError(Exception):
    pass

class SurveyDataset(ABC):
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


class LocalSQLiteDataset(SurveyDataset):
    """
    Extract and update local sqlite3 questinoare database
    """
    def __init__(self, db):
        self.db = db

    def get_first_attempt_mailing(self):
        try:
            conn = sqlite3.connect(self.db)
            cursor = conn.cursor()
            cursor.execute(
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
            result = cursor.fetchall() 
            cursor.close()
            return result

        except sqlite3.Error as error:
            print("Error while connecting to sqlite", error)
        finally:
            if conn:
                conn.close()

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
    test_db = "env/testdb.sqlite3"
    sqlm = LocalSQLiteDataset(test_db)
    print(sqlm.get_first_attempt_mailing())


"""
DROP VIEW strategi_mailings;

CREATE VIEW strategi_mailings
as
SELECT
    respondentid,
    julianday(datetime('now'))-julianday(closetime) as days_since_done,
    closetime,
    datetime('now') as today,
    l1.field_text as situation1_text,
    l2.field_text as situation2_text,
    l3.field_text as situation3_text,
    ls1.field_text as strategi1_text,
    ls2.field_text as strategi2_text,
    ls3.field_text as strategi3_text,
    email_strategi,
    strategi_mail_send_first,
    strategi_mail_send_second 
from
    answers3 a
    LEFT JOIN labels l1 on (a.situation1 = l1.field_value and l1.field_name = 'situation1')
    LEFT JOIN labels l2 on (a.situation2 = l2.field_value and l2.field_name = 'situation2')
    LEFT JOIN labels l3 on (a.situation3 = l3.field_value and l3.field_name = 'situation3')
    LEFT JOIN labels ls1 on (a.strategi1 = ls1.field_value and ls1.field_name = 'strategi1')
    LEFT JOIN labels ls2 on (a.strategi2 = ls2.field_value and ls2.field_name = 'strategi2')
    LEFT JOIN labels ls3 on (a.strategi3 = ls3.field_value and ls3.field_name = 'strategi3')
where
    strategimail = 1 AND
    strategireminder = 1 AND
    (strategi_mail_send_first is null OR strategi_mail_send_second is null)
;
"""