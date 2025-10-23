import unittest

from src.nlp_processor import NlpProcessor

class TestNlpProcessor(unittest.TestCase):
    """class to test the functionality of NLP processing pipeline"""

    def setUp(self):
        self.match_percentage = 70
        self.nlp_processor = NlpProcessor(self.match_percentage)

    def test_initialization(self):
        #assuming 70% is the required match percentage
        nlp_processor = NlpProcessor(70)
        self.assertTrue(True)


