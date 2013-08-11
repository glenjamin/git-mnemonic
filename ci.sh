#!/bin/bash

# Strict mode
set -e

# Application tests
./tests.py

# Check that the package is installable
python setup.py sdist
pip install `ls dist/*.gz`

echo 'Testing executable'


out=$(git mnemonic)
echo "mnemonic for HEAD: $out"
rt=$(git mnemonic $out)
echo "mnemonic decoded again: $rt"
[ "a$rt" = `git rev-parse HEAD` ] || echo "ERROR: Hash did not decode"