max_size = 2
words = [
'any',
'bear',
'club',
'ding',
'end',
'for',
'grab',
'hi',
'imp',
'jam',
'kin',
'line',
'met',
'no',
'on',
'pot',
'quit',
'rich',
'sit',
'tin',
'up',
'vat',
'will',
'xray',
'yes',
'zoo',
'axe',
'bee',
'cat',
'deer',
'elk',
'fire',
'gym',
]

char2word = dict( (hex(i)[2:], w) for (i, w) in enumerate(words) )
word2char = dict( (v, k) for (k, v) in char2word.iteritems() )

def raw_encode(char):
    return char2word.get(char, False)
def raw_decode(word):
    return word2char.get(word, False)