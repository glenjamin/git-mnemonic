import os

max_size = 2
wordfile = os.path.join(os.path.dirname(__file__), 'words.txt')
words = open(wordfile, mode='r')

char2word = {}
i = 0
for line in words.readlines():
    word = line.strip()
    if word:
        char2word[hex(i)[2:]] = word
        i += 1

word2char = dict( (v, k) for (k, v) in char2word.items() )

def raw_encode(char):
    return char2word.get(char, False)
def raw_decode(word):
    try:
        return word2char[word]
    except KeyError:
        raise Exception("%s is not valid in a mnemonic" % word)