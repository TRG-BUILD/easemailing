from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List

@dataclass
class SurveyResult:
    """
    Class that all the extracted data will be formated to
    """
    recipient_id: int
    days_since: int
    recipient_email: int
    situations: tuple
    responses: tuple
    situation_tag: str = "situation{}"
    response_tag: str = "strategi{}"

    def get_response_dict(self):
        """
        Returns formatted responses for easier insertion into emails
        {tag1: response_text1, tag2: response_text2, ...}
        """
        result = {}
        for i, response in enumerate(self.responses):
            key = self.response_tag.format(i)
            result[key] = response
        return result

    def get_situation_dict(self):
        """
        Returns formatted situations for easier insertion into emails
        {tag1: situation_text1, tag2: situation_text2, ...}
        """
        result = {}
        for i, response in enumerate(self.situations):
            key = self.situation_tag.format(i)
            result[key] = response
        return result


class ResultFormatter(ABC):
    @abstractmethod
    def format(self, data: List[tuple]) -> List[SurveyResult]:
        """
        Formats the extracted data to results
        """


class SQLiteResultFormatter(ResultFormatter):
    """ Field order in SQLiteExtractor result
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
    """

    def format(self, data: List[tuple]) -> List[SurveyResult]:
        results = []
        for row in data:
            s = SurveyResult(
                recipient_id=row[0],
                days_since=row[1],
                recipient_email=row[-1],
                situations = tuple(row[4:7]),
                responses = tuple(row[7:10])
            )
            results.append(s)
        return results

if __name__ == "__main__":
    db_output = [
        (827280790, 17.982222222257406, 
        '2021-09-10 14:58:00', '2021-09-28 14:32:24',
        'Når jeg kører på strækninger, jeg kender godt',
        'Når en bagvedkørende trafikant presser mig',
        'Når der kun er lidt eller ingen anden trafik',
        'At hastighedsovertrædelser generelt ikke accepteres i samfundet',
        'At det er bedre at komme for sent end at køre for stærkt',
        'At bruge fartpilot eller fartbegrænser til at styre min hastighed', 
        'asdasd@build.aau.dk')
    ]

    fmt = SQLiteResultFormatter()
    result = fmt.format(db_output)
    print(result)
    print(result[0].get_situation_dict())
    print(result[0].get_response_dict())