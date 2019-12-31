from textblob import TextBlob
from textblob import Word

wiki = TextBlob('until further notice')
print(wiki.correct())

w = Word('repective')

print(w.spellcheck())
print(len(w.spellcheck()))

for i in range(len(w.spellcheck())):
    print(w.spellcheck()[i][0])