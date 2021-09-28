from abc import ABC, abstractmethod
from dataclasses import dataclass
import datasets 
import formatters

@dataclass
class Pipeline(ABC):
    def __init__(self):
        self.dataset = datasets.SurveyDataset()
        self.formatter = formatters.SurveyFormatter()
    
    @abstractmethod
    def get_first_attempt_mailing(self):
        """
        Fetch recipients for mailing
        """

    def update_first_attempt(self, recipient_id: int, success: bool):
        """
        Updates status on receiving first emal
        """

class LocalSQLPipeline(Pipeline):
    def __init__(self, local_db): 
        self.dataset = datasets.LocalSQLiteDataset(local_db)
        self.formatter = formatters.SQLiteSurveyFormatter()

    def get_first_attempt_mailing(self):
        db_rows = self.dataset.get_first_attempt_mailing()
        survey_results = self.formatter.format(db_rows)
        return survey_results

    def update_first_attempt(self, recipient_id: int, success: bool):
        self.dataset.update_first_attempt(recipient_id, success)


#class RemoteSQLPipeline(Pipeline):
#class RemotePostgreSQLPipeline(Pipeline):

if __name__ == "__main__":
    test_db = "env/testdb.sqlite3"

    p = LocalSQLPipeline(test_db)

    for survey in p.get_first_attempt_mailing():
        print(survey)