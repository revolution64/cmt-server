import spacy;
from spacy.lang.nl.examples import sentences
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
    print("Hi guys, im here" + text)
    doc = nlp(text);
    result = extract_most_used_lemmas_and_pos(doc);
    most_occurring_pos = Counter(result["pos_per_sentence"]).most_common(3)
    most_occuring_lemmas = Counter(result["lemmas"]).most_common(3)
    return {"most_occurring_pos": most_occurring_pos, "most_occuring_lemmas": most_occuring_lemmas}