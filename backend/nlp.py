import spacy;
import json;
from OpenDutchWordnet import Wn_grid_parser
from collections import Counter

instance = Wn_grid_parser(Wn_grid_parser.odwn)
nlp = spacy.load("nl_core_news_md")

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
            print(token.lemma_ + "-" + token.pos_[0].lower() + "-1")
            lemmas.append(token.lemma_ + "-" + token.pos_[0].lower() + "-1")

    return { "pos_per_sentence": pos_per_sentence, "lemmas": lemmas}        


def getSynonyms(most_occuring_lemmas = []):
    most_occuring_lemmas_with_synonyms = []

    for lemma in most_occuring_lemmas:
        lemmaWithPOS = lemma[0]
        le_el = instance.les_find_le(lemmaWithPOS)
        
        if le_el is not None:
            synset_el = instance.synsets_find_synset(le_el.get_synset_id())
            print(synset_el.get_glosses(['nl']))

        synonyms = list(instance.les_lemma_synonyms("fiets"))[0:10]
        if "fiets" in synonyms:
            synonyms.remove("fiets")
        most_occuring_lemmas_with_synonyms.append(
            {"lemma": "fiets", "occurences": lemma[1], "synonyms": synonyms})

    return most_occuring_lemmas_with_synonyms

def getMostOccurringValues(dictValue, dictProperty, minAmount):
    return Counter(dictValue[dictProperty]).most_common(minAmount)

def getMostOccurringLemmaAndPOS(text):
    dictWithLemmasAndPOS = lemmatizeAndPosTagDoc(text)
    most_occurring_pos = getMostOccurringValues(dictWithLemmasAndPOS, "pos_per_sentence", 3)
    most_occuring_lemmas = getMostOccurringValues(dictWithLemmasAndPOS, "lemmas", 3)

    return {"most_occurring_pos": most_occurring_pos, "most_occurring_lemmas": getSynonyms(most_occuring_lemmas)}
