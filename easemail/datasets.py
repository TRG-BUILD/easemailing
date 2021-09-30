import sqlite3
from dataclasses import dataclass
from typing import List
from abc import ABC, abstractmethod
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError


@dataclass
class SurveyResult:
    """
    Class that all the extracted data will be formated to
    """
    recipient_id: int
    recipient_email: int
    days_since: int = 0
    situations: tuple = ()
    responses: tuple = ()
    additional: tuple = ()
    situation_tag: str = "situation_{}"
    response_tag: str = "response_{}"
    additional_tag: str = "additional_{}"

    def _get_dict(self, content: tuple, tags_rule: str):
        """
        Returns formatted content for easier subtitution into tagged text
        {tag1: content1, tag2: content2, ...}
        """
        result = {}
        for i, c in enumerate(content):
            key = tags_rule.format(i)
            result[key] = c
        return result       

    def get_situation_dict(self):
        return self._get_dict(self.situations, self.situation_tag)   
    
    def get_response_dict(self):
        return self._get_dict(self.responses, self.response_tag)

    def get_additional_dict(self):
        return self._get_dict(self.additional, self.additional_tag)

    def get_dict(self):
        result = {}
        result.update(self.get_situation_dict())
        result.update(self.get_response_dict())
        result.update(self.get_additional_dict())
        return result

class DatasetError(Exception):
    pass


class SurveyDataset(ABC):
    @abstractmethod
    def get_unsent_survey_results(self) -> List[SurveyResult]:
        """
        Returns emails of recipients that want email strategy,
        a reminder and have not received mail before
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

    def get_unsent_survey_results(self):
        try:
            conn = sqlite3.connect(self.db)
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT
                    respondentid,
                    days_since_done,
                    email_strategi,
                    strategi_mail_send_first,
                    strategi_mail_send_second,
                    situation1_text,
                    situation2_text,
                    situation3_text,
                    strategi1_text,
                    strategi2_text,
                    strategi3_text
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


class SQLAlchemyDataset(SurveyDataset):
    """
    Flexible database input based on the URL:
    https://docs.sqlalchemy.org/en/14/core/engines.html
    """
    def __init__(self, db_url: str):
        self.db_url = db_url
        self.engine = create_engine(self.db_url)

    def get_unsent_survey_results(self) -> List[SurveyResult]:
        result_tuples = self._get_unsent_result_tuples()
        return self._format_result_tuples(result_tuples) 

    def _format_result_tuples(self, result_tuples: List[tuple]) -> List[SurveyResult]:
        formatted = []
        for r in result_tuples:
            sr = SurveyResult(
                recipient_id=r["respondentid"],
                recipient_email=r["email_strategi"],
                days_since=r["days_since_done"],
                situations=tuple([v for k, v in r.items() if k.startswith("situation")]),
                responses=tuple([v for k, v in r.items() if k.startswith("strategi")])
            )
            formatted.append(sr)
        return formatted

    def _get_unsent_result_tuples(self) -> List[tuple]:
        try:
            with self.engine.connect() as conn:
                result = conn.execute(
                    """
                    SELECT
                        respondentid,
                        days_since_done,
                        email_strategi,
                        strategi_mail_send_first,
                        strategi_mail_send_second,
                        situation1_text,
                        situation2_text,
                        situation3_text,
                        strategi1_text,
                        strategi2_text,
                        strategi3_text
                    FROM
                        strategi_mailings
                    """
                )
                out = []
                for r in result:
                    out.append(r._asdict())
                return out
        except SQLAlchemyError as e:
            
            raise DatasetError("Unable to perform dataset operation", e)

    def update_first_attempt(self, recipient_id: int, sucess: bool):
        """
        Updates the date of succesul or fail attempt to send a first email
        """

    def update_second_attempt(self, recipient_id: int, sucess: bool):
        """
        Updates the date of succesul or fail attempt to send a second email
        """

if __name__ == "__main__":
    db_url = 'sqlite:///env/unittest.sqlite3'
    db = SQLAlchemyDataset(db_url)
    print(db.get_unsent_survey_results())