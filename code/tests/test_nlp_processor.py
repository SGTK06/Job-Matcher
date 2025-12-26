"""
File to test the functions that handle word matching
using Natural Language Processing.
author: Sham Ganesh Thamarai Kannan
for: FIT2107 D1 - Custom Project - Job Matcher
"""

import unittest
from unittest import mock

from src.nlp_processor import NlpProcessor
import spacy

"""
Tests whether the NLP Processor matches words with similar meaning
correctly, and handles edge cases effectively.

Blackbox Tests:
Expected:
T01.  comparison of empty lists of keywords returns score of 0
T02.  comparison with/against an empty list also returns score 0
T03.  comparison of same words in different tense should result
      high score
T04.  comparison of same words in different case should result in
      in a score of 100%
T05.  comparison of same words surrounded by different puntuation
      should result in a score of 100%
T06.  comparison of same words should result in a score of 100%
T07.  comparison of words with whitespaces should result in a
      score of 0%

Whitebox and Mocking Tests:
Expected:
T08.  successful creation of nlp processor
T09.  using mock tokens and simplified similarity logic
      test if the comparison score is calculated
      appropriately (mocked to isolate scoring logic)
      a. comparison of source keywords with target
      b. comparison of target keywords with source
        (checking for source subset of target, so
        scores will change)
T10.  using mock tokens and simplified similarity to check
      if only tokens with similarity more than or equal to match are
      considered for scoring (mock to isolate token factoring logic)
      ->BVA on match percentage
        Boundary = match percentage value (3-way BVA)
        BVA points =>
         a. before match percentage value
         b. at match percentage value
         c. after match percentage value
T11.  test in case comparison raises error
"""

def nlp_model(word, default_similarity=None):
    """mock nlp model to return a list of fake tokens"""
    return [FakeToken(word, default_similarity)]

def nlp_before_boundary_similarity(word):
    """mock nlp model to return a list of fake tokens"""
    return [FakeToken(word, 0.69)]

def nlp_on_boundary_similarity(word):
    """mock nlp model to return a list of fake tokens"""
    return [FakeToken(word, 0.70)]

def nlp_after_boundary_similarity(word):
    """mock nlp model to return a list of fake tokens"""
    return [FakeToken(word, 0.71)]

class FakeToken:
    """Fake token class to test similarity evaluation
    and scoring logic"""

    def __init__(self, word, default_similarity=None):
        """Fake token constructor"""
        self.lemma_ = word
        self.word = word
        self.default_similarity = default_similarity

    def similarity(self, other):
        """simple similarity logic"""
        if self.default_similarity is not None:
            return self.default_similarity
        else:
            if self.word == other.word:
                return 1
            else:
                return 0

def errored_nlp(word):
    """mock nlp model to return a list of fake tokens"""
    return [SimilarityErrorToken(word)]

class SimilarityErrorToken:
    """Error token class to test similarity evaluation
    and scoring logic exception handling in case of error"""

    def __init__(self, word, similarity_error=BaseException):
        """Fake token constructor"""
        self.lemma_ = word
        self.word = word
        self.default_similarity = similarity_error

    def similarity(self, other):
        """simple similarity logic"""
        raise self.default_similarity

class TestNlpProcessor(unittest.TestCase):
    """class to test the functionality of NLP processing pipeline"""

    @classmethod
    def setUpClass(cls):
        """
        initialize NLP processor once then use for
        comparison
        """
        cls.match_percentage = 70
        cls.nlp_processor = NlpProcessor(cls.match_percentage)

    def test_compare_empty_keywords_lists_t01(self):
        source_list = []
        target_list = []
        comparison_score = self.nlp_processor.compare_keywords(source_list, target_list)
        self.assertEqual(comparison_score, 0)

    def test_compare_empty_keywords_list_with_proper_list_t02_a(self):
        source_list = []
        target_list = ["python", "numpy", "pandas", "agile", "java"]
        comparison_score = self.nlp_processor.compare_keywords(source_list, target_list)
        self.assertEqual(comparison_score, 0)

    def test_compare_proper_list_with_empty_keywords_list_t02_b(self):
        source_list = ["python", "numpy", "pandas", "agile", "java"]
        target_list = []
        comparison_score = self.nlp_processor.compare_keywords(source_list, target_list)
        self.assertEqual(comparison_score, 0)

    def test_compare_proper_lists_of_words_in_diff_tense_t03(self):
        source_list = ["run", "jump", "fly", "act", "fight", "cry", "cook"]
        target_list = ["ran", "jumping", "flight", "acting", "fought", "crying", "cooking"]
        comparison_score = self.nlp_processor.compare_keywords(source_list, target_list)
        self.assertTrue(comparison_score > 70)

    def test_compare_same_words_with_different_case_t04(self):
        source_list = ["python", "java"]
        target_list = ["PYTHON", "JAVA"]
        comparison_score = self.nlp_processor.compare_keywords(source_list, target_list)
        self.assertEqual(comparison_score, 100)

    def test_compare_same_words_with_different_punctuation_symbols_t05(self):
        source_list = ["python", "java"]
        target_list = ["@python..!", "#java$$"]
        comparison_score = self.nlp_processor.compare_keywords(source_list, target_list)
        self.assertEqual(comparison_score, 100)

    def test_compare_same_lists_of_words_t06(self):
        source_list = ["python", "numpy", "pandas", "agile", "java"]
        target_list = ["python", "numpy", "pandas", "agile", "java"]
        comparison_score = self.nlp_processor.compare_keywords(source_list, target_list)
        self.assertTrue(comparison_score > 90)

    def test_spaces_and_blanks_comparison_t07(self):
        source_list = [" ", ""]
        target_list = ["", "  "]
        comparison_score = self.nlp_processor.compare_keywords(source_list, target_list)
        self.assertEqual(comparison_score, 0)

    def test_initialization_t08(self):
        #assuming 70% is the required match percentage
        nlp_processor = NlpProcessor(70)
        self.assertTrue(True)

    def test_isolated_scoring_logic_source_to_target_t09a(self):
        """since source has everything in target, score should be 100"""
        source_list = ["java", "python", "math", "physics", "engineering"]
        target_list = ["java", "python", "math", "physics", "engineering", "c", "c#", "data science", "ai", "ml"]

        mock_processor = NlpProcessor(70)
        mock_processor.set_nlp_model(nlp_model)
        comparison_score = mock_processor.compare_keywords(source_list, target_list)
        self.assertEqual(comparison_score, 100)

    def test_isolated_scoring_logic_target_to_source_t09b(self):
        """since source has everything in target, score should be 100"""
        source_list = ["java", "python", "math", "physics", "engineering"]
        target_list = ["java", "python", "math", "physics", "engineering", "css", "html", "data science", "ai", "ml"]

        mock_processor = NlpProcessor(70)
        mock_processor.set_nlp_model(nlp_model)
        comparison_score = mock_processor.compare_keywords(target_list, source_list)
        self.assertEqual(comparison_score, 50)

    def test_word_factor_into_score_logic_before_threshold_t10a(self):
        """before boundery no comparison crosses threshold, 0%"""
        source_list = ["a", "b", "c", "d", "e"]
        target_list = ["f", "g", "h", "i", "j"]

        mock_processor = NlpProcessor(70)
        mock_processor.set_nlp_model(nlp_before_boundary_similarity)
        comparison_score = mock_processor.compare_keywords(source_list, target_list)
        self.assertEqual(comparison_score, 0)

    def test_word_factor_into_score_logic_at_threshold_t10b(self):
        """on boundery all comparisons at threshold, 100% score"""
        source_list = ["a", "b", "c", "d", "e"]
        target_list = ["f", "g", "h", "i", "j"]

        mock_processor = NlpProcessor(70)
        mock_processor.set_nlp_model(nlp_on_boundary_similarity)
        comparison_score = mock_processor.compare_keywords(source_list, target_list)
        self.assertEqual(comparison_score, 100)

    def test_word_factor_into_score_logic_after_threshold_t10c(self):
        """after boundery all comparisons score beyond threshold, 100% score"""
        source_list = ["a", "b", "c", "d", "e"]
        target_list = ["f", "g", "h", "i", "j"]

        mock_processor = NlpProcessor(70)
        mock_processor.set_nlp_model(nlp_after_boundary_similarity)
        comparison_score = mock_processor.compare_keywords(source_list, target_list)
        self.assertEqual(comparison_score, 100)

    def test_token_comparison_error_t11(self):
        """after boundery all comparisons score beyond threshold, 100% score"""
        source_list = ["a", "b", "c", "d", "e"]
        target_list = ["f", "g", "h", "i", "j"]

        mock_processor = NlpProcessor(70)
        mock_processor.set_nlp_model(errored_nlp)
        comparison_score = mock_processor.compare_keywords(source_list, target_list)
        self.assertEqual(comparison_score, 0)