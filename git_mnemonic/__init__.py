import sys
import os
import subprocess

def debug(msg, obj):
    if os.environ.get('GIT_DEBUG', False):
        print msg, obj

def encode(ref):
    "Take a git revision and turn it into a mnemonic"
    revision = clean_revision(ref)
    return " ".join(map(raw_encode, revision))

def decode(mnemonic):
    "Take a mnemonic and turn it into a git revision"
    return "".join(map(raw_decode, mnemonic.split(" ")))

def clean_revision(ref, length=8):
    command = ["git", "rev-parse", "--short=%d" % length, "--verify", ref]
    debug("command", command)
    rev_parse = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    returncode = rev_parse.wait()

    if returncode != 0:
        raise Exception("git revision not found: %s" % ref)

    return rev_parse.stdout.read().strip()

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
}
chars = dict((v, k) for (k, v) in words.iteritems())

def raw_encode(char):
    return words[char]
def raw_decode(word):
    return chars[word]