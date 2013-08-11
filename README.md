git mnemonic
============

Speakable, rememberable translations for git ref hashes

Usage
-----

From inside a git repository

    # Defaults to HEAD
    $ git mnemonic
    end line grab ding

    # Can be given a specific revision
    $ git mnemonic origin/master
    line pot end bear

    # Will translate back to the full git hash
    $ git mnemonic line pot end bear
    4b63bf41e0c2369c76b6e3ce3ea40ed5fa0977c3

Install
-------

TODO