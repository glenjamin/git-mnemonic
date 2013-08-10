import sys
import os
import subprocess

import git_mnemonic.translate as t

def debug(msg, obj):
    if os.environ.get('GIT_DEBUG', False):
        print msg, obj

def encode(ref):
    "Take a git revision and turn it into a mnemonic"
    revision = clean_revision(ref)
    chars = list(revision)
    mnemonic = []
    while len(chars):
        for size in xrange(t.max_size, 0, -1):
            chunk = "".join(chars[0:size])
            debug("trying to match", chunk)
            word = t.raw_encode(chunk)
            if word:
                debug("Matched", word)
                mnemonic.append(word)
                del chars[0:size]
                break

    return " ".join(mnemonic)

def decode(mnemonic):
    "Take a mnemonic and turn it into a git revision"
    return "".join(map(t.raw_decode, mnemonic.split(" ")))

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