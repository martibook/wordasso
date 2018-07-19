from wordasso.wordasso import syn_words, pho_words, ent_words
import csv


files = ["../datasets/mc.csv"]


def test_syn_words():
    for f in files:
        with open(f, "r") as inf:
            reader = csv.reader(inf, delimiter=",")
            for row in reader:
                w = row[0]
                print("word: ", w)
                print("containing-synonym-tag related words:")
                print(syn_words(w))
                print("-" * 60)


def test_pho_words():
    for f in files:
        with open(f, "r") as inf:
            reader = csv.reader(inf, delimiter=",")
            for row in reader:
                w = row[0]
                print("word: ", w)
                print("most-sounds-like related words:")
                print(pho_words(w))
                print("-" * 60)


def test_ent_words():
    for f in files:
        with open(f, "r") as inf:
            reader = csv.reader(inf, delimiter=",")
            for row in reader:
                w = row[0]
                print("word: ", w)
                print("Named Entities related to the words:")
                print(ent_words(w))
                print("-" * 60)


if __name__ == '__main__':
    pass