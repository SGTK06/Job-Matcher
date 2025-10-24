import unittest

from src.nlp_processor import NlpProcessor
import spacy

class TestNlpProcessor(unittest.TestCase):
    """class to test the functionality of NLP processing pipeline"""

    def setUp(self):
        self.match_percentage = 70
        self.nlp_processor = NlpProcessor(self.match_percentage)

    def test_initialization(self):
        #assuming 70% is the required match percentage
        nlp_processor = NlpProcessor(70)
        self.assertTrue(True)

    def test_compare_empty_keywords_lists(self):
        source_list = []
        target_list = []
        comparison_score = self.nlp_processor.compare_keywords(source_list, target_list)
        self.assertEqual(comparison_score, 0)

    def test_compare_empty_keywords_list_with_proper_list(self):
        source_list = []
        target_list = ["python", "numpy", "pandas", "agile", "java"]
        comparison_score = self.nlp_processor.compare_keywords(source_list, target_list)
        self.assertEqual(comparison_score, 0)

    def test_compare_proper_list_with_empty_keywords_list(self):
        source_list = ["python", "numpy", "pandas", "agile", "java"]
        target_list = []
        comparison_score = self.nlp_processor.compare_keywords(source_list, target_list)
        self.assertEqual(comparison_score, 0)

    def test_compare_proper_lists_of_words(self):
        source_list = ["run", "jump", "fly", "act", "fight", "cry", "cook"]
        target_list = ["running", "jumping", "flying", "acting", "fighting", "crying", "cooking"]
        comparison_score = self.nlp_processor.compare_keywords(source_list, target_list)
        self.assertTrue(comparison_score > 70)

    def test_compare_same_lists_of_words(self):
        source_list = ["python", "numpy", "pandas", "agile", "java"]
        target_list = ["python", "numpy", "pandas", "agile", "java"]
        comparison_score = self.nlp_processor.compare_keywords(source_list, target_list)
        self.assertTrue(comparison_score > 90)
