import os
import unittest

from easemail.datasets import SQLAlchemyDataset, SurveyResult 

class TestSurveyResults(unittest.TestCase):
    situations = ("1","2")
    responses = ("hi","bye")
    additional = ("nope",)
    def test_generates_correct_dict(self):
        sr = SurveyResult(0, "whatver@mail.com", 0,
            self.situations,
            self.responses,
            self.additional
        )
        self.assertDictEqual(
            {"situation_0": "1", "situation_1": "2"}, sr.get_situation_dict())
        self.assertDictEqual(
            {"response_0": "hi", "response_1": "bye"}, sr.get_response_dict())
        self.assertDictEqual(
            {"additional_0": "nope"}, sr.get_additional_dict())
        self.assertDictEqual({
            "situation_0": "1", "situation_1": "2",
            "response_0": "hi", "response_1": "bye",
            "additional_0": "nope"
            }, sr.get_dict())


class TestSQLAlchemyDataset(unittest.TestCase):
    db_path = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "data",
        "unittest.sqlite3"
    )
    db_url = f'sqlite:///{os.path.join(db_path)}'
    expected = [
        (827280790, 19.930335647892207, 'qweasd321@build.aau.dk', None, None, 
        'Når jeg kører på strækninger',
        'jeg kender godt',
        'Når en bagvedkørende trafikant presser mig',
        'Når der kun er lidt eller ingen anden trafik',
        'At hastighedsovertrædelser generelt ikke accepteres i samfundet',
        'At det er bedre at komme for sent end at køre for stærkt',
        'At bruge fartpilot eller fartbegrænser til at styre min hastighed'), 
        (827288742, 19.878807870205492, 'qweasd321@build.aau.dk', None, None, 
        'Når der kun er lidt eller ingen anden trafik', 
        'For at følge trafikkens flow', 
        'Når bilen gerne vil køre hurtigere', 
        'At jeg skal forsøge at undgå at sætte mig selv i en lignende situation igen', 
        'Hvor pinligt det vil være at få en fartbøde', 
        'At der er mennesker i mit liv, der ønsker at jeg overholder hastighedsgrænsen'), 
        (827280888, 19.92877314798534, 'zxcasd765@build.aau.dk', None, None, 
        'Når der er lille risiko for at blive opdaget af politiet', 
        'Når bilen gerne vil køre hurtigere', 
        'Når jeg skal køre langt', 
        'At selv om det er let og dejligt at køre for stærkt, så er det en farlig vane', 
        'At det er bedre at komme for sent end at køre for stærkt', 
        'At høj fart gør det sværere at reagere i tide, hvis andre laver fejl'),
        (827284595, 19.904849536716938, 'zxcasd765@build.aau.dk', None, None, 
        'Når jeg er er stresset ', 
        'For at følge trafikkens flow', 
        'Når en bagvedkørende trafikant presser mig', 
        'At hastighedsovertrædelser øger brændstofforbruget. Det skader miljøet og er dyrt', 
        'At hastighedsovertrædelser øger brændstofforbruget. Det skader miljøet og er dyrt', 
        'At jeg ikke sparer ret meget tid ved at køre for stærkt')
    ]

    def test_exception_on_incorrect_db_url(self):
        wrong_db_url = f'sqlite:///data/wrong.db'
        self.assertRaises(Exception, SQLAlchemyDataset(wrong_db_url))

        
        