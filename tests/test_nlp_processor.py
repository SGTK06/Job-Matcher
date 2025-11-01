"""
File to test the functions that handle word matching
using Natural Language Processing.
author: Sham Ganesh Thamarai Kannan
for: FIT2107 D1 - Custom Project - Job Matcher
"""

import unittest

from src.nlp_processor import NlpProcessor
import spacy

"""
Tests whether the NLP Processor matches words with similar meaning
correctly, and handles edge cases effectively.

Blackbox Tests:
Expected:
BT01. comparison of empty lists of keywords returns score of 0
BT02. comparison with/against an empty list also returns score 0
BT03. comparison of same words in different tense should result
      high score
BT04. comparison of same words in different case should result in
      in a score of 100%
BT05. comparison of same words surrounded by different puntuation
      should result in a score of 100%
BT06. comparison of same words should result in a score of 100%
"""


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
