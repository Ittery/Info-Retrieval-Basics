from collections import defaultdict
import nltk

class InvertedIndex:
    def __init__(self, tokenizer):
        self.tokenizer = tokenizer
        self.index = defaultdict(list)
        self.documents = {}
        self.unique_id = 0

    def termLookup(self, word):
        word = word.lower()
        return [self.documents.get(id, None) for id in self.index.get(word)]

    def retIndex(self):
        return self.index.items()

    def addTerm(self, document):
        for token in [t.lower() for t in nltk.word_tokenize(document)]:
            if self.unique_id not in self.index[token]:
                self.index[token].append(self.unique_id)

        self.documents[self.unique_id] = document
        self.unique_id += 1


invObj = InvertedIndex(nltk.word_tokenize)

corpus = ['a set of documents', 'toby is a cat', 'a set of cans', 'cat likes food in cans'
          'toby is a good name']

# Add Corpus Data to Inverted Index
for c in range(0, len(corpus)):
    invObj.addTerm(corpus[c])

# Imverted Index Lookup
res = invObj.termLookup("cans")
print(len(res))

# View Inverted Index
invIndex = invObj.retIndex()
for k, v in invIndex:
    print("{} ---> {}".format(k, v))
