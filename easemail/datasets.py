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
    days_since_done: int = 0
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
    def update_attempt(self, attempt_number: int, recipient_id: int, success: bool):
        """
        Updates the date of succesul or fail attempt to send an email
        """


class SQLAlchemyDataset(SurveyDataset):
    """
    Flexible database input based on the URL:
    https://docs.sqlalchemy.org/en/14/core/engines.html
    """
    def __init__(self, db_url: str):
        self.db_url = db_url
        self.engine = create_engine(self.db_url)

    def get_unsent_survey_results(self) -> List[SurveyResult]:
        result_dicts = self._get_unsent_result_dicts()
        return self._format_result_dicts(result_dicts) 

    def _format_result_dicts(self, result_dicts: List[dict]) -> List[SurveyResult]:
        formatted = []
        for r in result_dicts:
            sr = SurveyResult(
                recipient_id=r["respondentid"],
                recipient_email=r["email_strategi"],
                days_since_done=r["days_since_done"],
                situations=tuple([v for k, v in r.items() if k.startswith("situation")]),
                responses=tuple([v for k, v in r.items() if "strategi" in k and "text" in k])
            )
            formatted.append(sr)
        return formatted

    def _get_unsent_result_dicts(self) -> List[tuple]:
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

    def _update_attempt_by_field(self, recipient_id: int, update_field: str):
        try:
            with self.engine.connect() as conn:
                conn.execute(
                    f"""
                        UPDATE 
                            answers3
                        SET 
                            {update_field} = datetime('now')
                        WHERE 
                            respondentid = {recipient_id}
                    """
                )
        except SQLAlchemyError as e:
            raise DatasetError("Unable to perform dataset operation", e)

    def update_attempt(self, attempt_number: int, recipient_id: int, success: bool):
        attempt_map = {
            1: "_first",
            2: "_second"
        }
        update_field = "strategi_mail_send" + attempt_map[attempt_number]
        if not success:
            update_field += "_failed"
        self._update_attempt_by_field(recipient_id, update_field)

if __name__ == "__main__":
    db_url = 'sqlite:///test/data/mismatch_testdb.sqlite3'
    db = SQLAlchemyDataset(db_url)
    print(db._get_unsent_result_dicts()[0])
    #print(db.get_unsent_survey_results())
    