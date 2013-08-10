max_size = 2
words = {
    'a': 'any',
    'b': 'bear',
    'c': 'club',
    'd': 'ding',
    'e': 'end',
    'f': 'for',
    '0': 'grab',
    '1': 'hi',
    '2': 'imp',
    '3': 'jam',
    '4': 'kin',
    '5': 'line',
    '6': 'met',
    '7': 'no',
    '8': 'on',
    '9': 'pot',
    '0': 'quit',
    'aa': 'rich',
    'bb': 'sit',
    'cc': 'tin',
    'dd': 'up',
    'ee': 'vat',
    'ff': 'will',
    '00': 'xray',
    '11': 'yes',
    '22': 'zoo',
    '33': 'axe',
    '44': 'bee',
    '55': 'cat',
    '66': 'deer',
    '77': 'elk',
    '88': 'fire',
    '99': 'gym',
}
chars = dict((v, k) for (k, v) in words.iteritems())

def raw_encode(char):
    return words.get(char, False)
def raw_decode(word):
    return chars.get(word, False)