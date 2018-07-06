import requests
from nltk.corpus import wordnet as wn
import spacy
from wordasso.phoneasso import PAV


ml_url = "https://api.datamuse.com/words?ml={w}"
nlp = spacy.load('en_core_web_sm')
NE_TYPES = ["PERSON", "NORP", "ORG", "GPE", "LOC", "PRODUCT", "WORK_OF_ART", "LANGUAGE"]


def syn_words(word):
    """
    query means like words of the key word from datamuse API, return those have synonym tag with the key word
    :param word: the key word
    :return: means like words which has "syn" in tags list
    """
    r = requests.get(ml_url.format(w=word))
    syn = [item["word"] for item in r.json() if "tags" in item and "syn" in item["tags"]]
    return syn


def pho_words(word, L=10):
    """
    query means like words of the key word from datamuse API, then return those most sound like the key word
    :param word: the key word
    :return:
    """
    r = requests.get(ml_url.format(w=word))
    pho = [(item["word"], PAV(word, item["word"])) for item in r.json()]
    pho = [item for item in pho if item[1] is not None]
    pho = sorted(pho, key=lambda x: x[1], reverse=True)
    pho = [item[0] for item in pho]
    return pho[:L]


def contain_ne(word):
    """
    query synsets in Wordnet for the given word, achieve definition sentence of each synset
    if any definition sentence contains Named Entity, then this given word is related with Named Entity
    :param word: the given word
    :return: True of False
    """
    synsets = wn.synsets(word)
    for syn in synsets:
        def_sentence = syn.definition()
        doc = nlp(def_sentence)
        named_ents = [ent for ent in doc.ents if ent.label_ in NE_TYPES]
        if len(named_ents) > 0:
            return True
    else:
        return False


def ent_words(word):
    """
    query means like words of the key word from datamuse API, then return those words which are named entities
    :param word: the key word
    :return:
    """
    r = requests.get(ml_url.format(w=word))
    ml_words = [item["word"] for item in r.json()]
    contain_ne_words = [w for w in ml_words if contain_ne(w)]
    return contain_ne_words
