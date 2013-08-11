import sys
import os
import subprocess

import git_mnemonic.translate as t

def debug(msg, obj):
    if os.environ.get('GIT_DEBUG', False):
        print msg, obj

def encode(rev, abbrev=8):
    "Take a git revision and turn it into a mnemonic"
    revision = clean_revision(rev, abbrev=abbrev)
    chars = list(revision)
    mnemonic = []
    while len(chars):
        # Attempt to encode the longest chunk we can each time
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
    short = "".join(map(t.raw_decode, mnemonic.split(" ")))
    return clean_revision(short)

def clean_revision(revision, abbrev=None):
    command = ["git", "rev-parse"]
    if abbrev:
        command.append("--short=%d" % abbrev)
    command.extend(["--verify", revision])
    debug("command", command)
    rev_parse = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    returncode = rev_parse.wait()

    if returncode != 0:
        raise Exception("git revision not found: %s" % revision)

    return rev_parse.stdout.read().strip()