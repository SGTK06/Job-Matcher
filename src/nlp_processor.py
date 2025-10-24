"""
File for NLP processing pipeline handler class
author: Sham Ganesh Thamarai Kannan
for: FIT2107 D2
"""
import spacy


class NlpProcessor():
    """Handles the NLP processing data pipeline for comparing keywords
    of job description and applicatn skills"""

    def __init__(self, match_percentage):
        """constructor for processor"""
        self.nlp = spacy.load("en_core_web_md")
        self.comparisonThreshold = match_percentage/100  # convert to in range [0, 100]

    def tokenizer(self, keyword_list):
        tokens_list = []
        # split the given list of keywords to tokens to be compared
        for keyword in keyword_list:
            tokens = self.nlp(keyword)[0]
            tokens_list.append(tokens)
        return tokens_list

    def token_comparison(self, source_tokens, target_tokens):
        """
        For every token in a list of tokens, find the best matching token
        in the other list and save the tokens details for comparison
        """
        comparison = []
        # check for every token in source keyword tokens
        for source_token in source_tokens:

            best_matched_token = None
            best_matched_score = 0
            # find best match in target tokens
            for target_token in target_tokens:
                token_score = source_token.similarity(target_token)

                if token_score > best_matched_score:
                    best_matched_score = token_score
                    best_matched_token = target_token

            comparison.append({
                "sourceToken": source_token,
                "matchedToken": best_matched_token,
                "score": best_matched_score
            })
        return comparison

    def comparison_score(self, token_comparison):
        """
        Function to calculate the match percentage of source
        and target keywords based on threshold value of comparison
        and return number of matched keywords as %
        """
        match = 0
        # find number of keywords that match more than the threshold
        # value and get as %
        for comparison in token_comparison:
            if comparison["score"] > self.comparisonThreshold:
                match += 1

        if len(token_comparison) > 0:
            match_percentage = match/len(token_comparison) * 100
        else:
            match_percentage = 0

        return match_percentage

    def compare_keywords(self, source_keyword_list, target_keyword_list):
        """compares keywords in source keyword list and target keyword list"""
        source_tokens = self.tokenizer(source_keyword_list)
        target_tokens = self.tokenizer(target_keyword_list)
        # print(target_tokens, source_tokens)

        token_comparison = self.token_comparison(source_tokens, target_tokens)

        comparison_score = self.comparison_score(token_comparison)
        return comparison_score
