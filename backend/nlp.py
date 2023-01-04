import spacy;
from spacy.lang.nl.examples import sentences
from OpenDutchWordnet import Wn_grid_parser
from flask import jsonify

from collections import Counter

nlp = spacy.load("nl_core_news_md")

def extract_most_used_lemmas_and_pos(doc):

    lemmas = []
    pos_per_sentence = []
    sentence = ""

    for token in doc:
        #word = {"text": token.text, "POS": token.pos_, "DEP": token.dep_}
        sentence += "," + token.pos_

        if token.pos_ == "PUNCT":
            pos_per_sentence
            pos_per_sentence.append(sentence[1:])
            sentence = ""
        elif any(token.pos_ in pos for pos in ["NOUN", "VERB"]):
            lemmas.append(token.lemma_)

    return { "pos_per_sentence": pos_per_sentence, "lemmas": lemmas}        


def process_text(text):
    doc = nlp(text);
    instance = Wn_grid_parser(Wn_grid_parser.odwn);
    result = extract_most_used_lemmas_and_pos(doc);
    most_occurring_pos = Counter(result["pos_per_sentence"]).most_common(3)
    most_occuring_lemmas = Counter(result["lemmas"]).most_common(3)
    most_occuring_lemmas_with_synonyms = []

    for lemma in most_occuring_lemmas:
        synonyms = instance.les_lemma_synonyms(lemma[0])
        most_occuring_lemmas_with_synonyms.append({"lemma": lemma[0], "occurences": lemma[1], "synonyms": list(synonyms)[0:10]})
        
    print(most_occuring_lemmas_with_synonyms);

    return {"most_occurring_pos": most_occurring_pos, "most_occurring_lemmas": most_occuring_lemmas_with_synonyms}