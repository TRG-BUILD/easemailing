import os
import unittest
import shutil

from easemail.datasets import DatasetError, SQLAlchemyDataset, SurveyResult 
import testdb_data


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


class TestSQLAlchemyMatchingDataset(unittest.TestCase):
    data_generator = testdb_data.SQLAlchemyTestData()
    matching_db_path = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "data",
        "matching_testdb.sqlite3"
    )
    updateable_db_path = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "data",
        "updateable_testdb.sqlite3"
    )
    matching_db_url = f'sqlite:///{matching_db_path}'
    updateable_db_url = f'sqlite:///{updateable_db_path}'

    def setUp(self):
        shutil.copyfile(self.matching_db_path, self.updateable_db_path)

    def tearDown(self):
        os.remove(self.updateable_db_path)

    def test_exception_on_incorrect_db_url(self):
        wrong_db_url = f'sqlite:///data/wrong.db'
        self.assertRaises(Exception, SQLAlchemyDataset(wrong_db_url))

    def test_result_dict_formatting(self):
        db = SQLAlchemyDataset(self.matching_db_url)
        
        result_dicts, expected = self.data_generator.get_result_dict_formatting_data()
        formatted = db._format_result_dicts(result_dicts)[0]
        self.assertEqual(expected.recipient_id, formatted.recipient_id)
        self.assertEqual(expected.recipient_email, formatted.recipient_email)
        self.assertEqual(expected.days_since_done, formatted.days_since_done)
        self.assertEqual(expected.situations, formatted.situations)
        self.assertEqual(expected.responses, formatted.responses)

    def test_result_dict_querying(self):
        db = SQLAlchemyDataset(self.matching_db_url)

        expected_dicts = self.data_generator.get_result_dict_querying_data()
        result_dicts = db._get_unsent_result_dicts()

        for expected, result in zip(expected_dicts, result_dicts):
            for val_e, val_r in zip(expected.values(), result.values()):
                if isinstance(val_e, float):
                    self.assertAlmostEqual(val_e, val_r, delta=1)
                else:
                    self.assertEqual(val_e, val_r)

    def test_get_unsent_survey_results(self):
        db = SQLAlchemyDataset(self.matching_db_url)
        results = db.get_unsent_survey_results()
        self.assertTrue(len(results), 4)
        self.assertIsInstance(results[0], SurveyResult)

    def test_update_double_attempt_successful_email_removes_users(self):
        db = SQLAlchemyDataset(self.updateable_db_url)
        recipient_id=827280790
        db.update_first_attempt(recipient_id, success=True)
        db.update_second_attempt(recipient_id, success=True)

        # should not be able to re-send to this id anymore
        results = db.get_unsent_survey_results()
        unsent_recipients = [r.recipient_id for r in results]
        self.assertNotIn(recipient_id, unsent_recipients)

class TestSQLAlchemyMismatchDataset(unittest.TestCase):
    mismatch_db_path = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "data",
        "mismatch_testdb.sqlite3"
    )
    mismatch_db_url = f'sqlite:///{os.path.join(mismatch_db_path)}'

    def test_get_unsent_survey_results_raises_on_incorrect_schema(self):
        db = SQLAlchemyDataset(self.mismatch_db_url)
        self.assertRaises(DatasetError, db.get_unsent_survey_results)