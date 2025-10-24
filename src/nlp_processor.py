import spacy

class NlpProcessor():
    """Handles the NLP processing data pipeline for comparing keywords
    of job description and applicatn skills"""

    def __init__(self, match_percentage):
        """constructor for processor"""
        self.nlp = spacy.load("en_core_web_md")
        self.comparisonThreshold = match_percentage

    def tokenizer(self, keywordList):
        tokensList = []
        #split the given list of keywords to tokens to be compared
        for keyword in keywordList:
            tokens = self.nlp(keyword)[0]
            tokensList.append(tokens)
        return tokensList

    def compare_keywords(self, source_keyword_list, target_keyword_list):
        """compares keywords in source keyword list and target keyword list"""
