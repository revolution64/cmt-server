import spacy;
from OpenDutchWordnet import Wn_grid_parser
from collections import Counter

nlp = spacy.load("nl_core_news_md")
instance = Wn_grid_parser(Wn_grid_parser.odwn)

def lemmatizeAndPosTagDoc(text):
    doc = nlp(text)
    lemmas = []
    pos_per_sentence = []
    sentence = ""

    for token in doc:
        sentence += "," + token.pos_

        if token.pos_ == "PUNCT":
            pos_per_sentence
            pos_per_sentence.append(sentence[1:])
            sentence = ""
        elif any(token.pos_ in pos for pos in ["NOUN", "VERB", "ADJ"]):
            lemmas.append(token.lemma_)

    return { "pos_per_sentence": pos_per_sentence, "lemmas": lemmas}        


def getSynonyms(most_occuring_lemmas):
    most_occuring_lemmas_with_synonyms = []

    for lemma in most_occuring_lemmas:
        synonyms = list(instance.les_lemma_synonyms(lemma[0]))[0:10]
        if lemma[0] in synonyms:
            synonyms.remove(lemma[0])
        most_occuring_lemmas_with_synonyms.append(
            {"lemma": lemma[0], "occurences": lemma[1], "synonyms": synonyms})

    return most_occuring_lemmas_with_synonyms

def getMostOccurringValues(dictValue, dictProperty, minAmount):
    return Counter(dictValue[dictProperty]).most_common(minAmount)

def getMostOccurringLemmaAndPOS(text):
    dictWithLemmasAndPOS = lemmatizeAndPosTagDoc(text)
    most_occurring_pos = getMostOccurringValues(dictWithLemmasAndPOS, "pos_per_sentence", 3)
    most_occuring_lemmas = getMostOccurringValues(dictWithLemmasAndPOS, "lemmas", 3)

    return {"most_occurring_pos": most_occurring_pos, "most_occurring_lemmas": getSynonyms(most_occuring_lemmas)}
