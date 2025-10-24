import spacy

class NlpProcessor():
    """Handles the NLP processing data pipeline for comparing keywords
    of job description and applicatn skills"""

    def __init__(self, match_percentage):
        """constructor for processor"""
        self.nlp = spacy.load("en_core_web_md")
        self.comparisonThreshold = match_percentage

    def tokenizer(self, keyword_list):
        tokens_list = []
        #split the given list of keywords to tokens to be compared
        for keyword in keyword_list:
            tokens = self.nlp(keyword)[0]
            tokens_list.append(tokens)
        return tokens_list

    def token_comparison(self, sourceTokens, targetTokens):
        """
        For every token in a list of tokens, find the best matching token
        in the other list and save the tokens details for comparison
        """
        comparison = []
        #check for every token in source keyword tokens
        for sourceToken in sourceTokens:

            bestMatchedToken = None
            bestMatchedScore = 0
            #find best match in target tokens
            for targetToken in targetTokens:
                tokenScore = sourceToken.similarity(targetToken)

                if tokenScore > bestMatchedScore:
                    bestMatchedScore = tokenScore
                    bestMatchedToken = targetToken

            comparison.append({"sourceToken":sourceToken, "matchedToken":bestMatchedToken, "score":bestMatchedScore})
        return comparison

    def compare_keywords(self, source_keyword_list, target_keyword_list):
        """compares keywords in source keyword list and target keyword list"""
