from datetime import datetime, timedelta
from easemail.datasets import SurveyResult
# function to generate database

# function for expected output of the tuples

def get_days_since_done(date_str: str, fmt: str='%Y-%m-%d %H:%M:%S'):
    today = datetime.now() - datetime.strptime(date_str, fmt)
    return today.total_seconds() / timedelta(days=1).total_seconds()

class SQLAlchemyTestData:
    def get_result_dict_formatting_data(self):
        data = [{
            "respondentid": 10,
            "days_since_done": 10,
            "email_strategi": "a@mail.com",
            "strategi_mail_send_first": None,
            "strategi_mail_send_second": None,
            "situation1_text": "æ",
            "situation2_text": "b",
            "situation3_text": "c",
            "strategi1_text": "d",
            "strategi2_text": "e",
            "strategi3_text": "f"
        }]
        expected = SurveyResult(
                recipient_id=10,
                recipient_email="a@mail.com",
                days_since_done=10,
                situations=("æ", "b", "c"),
                responses=("d", "e", "f")
            )
        return data, expected

    def get_result_tuples_querying_data(self):
        return [
            (827280790, 
            get_days_since_done('2021-09-10 14:58:00'),
            'qweasd321@build.aau.dk', None, None, 
            'Når jeg kører på strækninger, jeg kender godt',
            'Når en bagvedkørende trafikant presser mig',
            'Når der kun er lidt eller ingen anden trafik',
            'At hastighedsovertrædelser generelt ikke accepteres i samfundet',
            'At det er bedre at komme for sent end at køre for stærkt',
            'At bruge fartpilot eller fartbegrænser til at styre min hastighed'), 
            (827288742, 
            get_days_since_done('2021-09-10 16:12:12'),
            'qweasd321@build.aau.dk', None, None, 
            'Når der kun er lidt eller ingen anden trafik', 
            'For at følge trafikkens flow', 
            'Når bilen gerne vil køre hurtigere', 
            'At jeg skal forsøge at undgå at sætte mig selv i en lignende situation igen', 
            'Hvor pinligt det vil være at få en fartbøde', 
            'At der er mennesker i mit liv, der ønsker at jeg overholder hastighedsgrænsen'), 
            (827280888,
            get_days_since_done('2021-09-10 15:00:15'),
            'zxcasd765@build.aau.dk', None, None, 
            'Når der er lille risiko for at blive opdaget af politiet', 
            'Når bilen gerne vil køre hurtigere', 
            'Når jeg skal køre langt', 
            'At selv om det er let og dejligt at køre for stærkt, så er det en farlig vane', 
            'At det er bedre at komme for sent end at køre for stærkt', 
            'At høj fart gør det sværere at reagere i tide, hvis andre laver fejl'),
            (827284595,
            get_days_since_done('2021-09-10 15:34:42'),
            'zxcasd765@build.aau.dk', None, None, 
            'Når jeg er er stresset ', 
            'For at følge trafikkens flow', 
            'Når en bagvedkørende trafikant presser mig', 
            'At hastighedsovertrædelser øger brændstofforbruget. Det skader miljøet og er dyrt', 
            'At hastighedsovertrædelser øger brændstofforbruget. Det skader miljøet og er dyrt', 
            'At jeg ikke sparer ret meget tid ved at køre for stærkt')
        ]

    def get_result_dict_querying_data(self):
        datadict = {
            "respondentid": 10,
            "days_since_done": 10,
            "email_strategi": "a@mail.com",
            "strategi_mail_send_first": None,
            "strategi_mail_send_second": None,
            "situation1_text": "æ",
            "situation2_text": "b",
            "situation3_text": "c",
            "strategi1_text": "d",
            "strategi2_text": "e",
            "strategi3_text": "f"
        }

        expected = []
        for row in self.get_result_tuples_querying_data():
            dictrow = {k: v for k, v in zip(datadict.keys(), row)}
            expected.append(dictrow)
        return expected
            
            

