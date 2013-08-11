#!/bin/bash

# Strict mode
set -e

# Application tests
./tests.py

# Check that the package is installable
python setup.py sdist
echo 'tarball contents:'
tar tzf `ls dist/*.gz`
pip install `ls dist/*.gz`


echo 'Testing executable'

out=$(git mnemonic)
echo "mnemonic for HEAD: $out"
rt=$(git mnemonic $out)
echo "mnemonic decoded again: $rt"
if [ "$rt" != `git rev-parse HEAD` ]; then
  echo "ERROR: Hash did not decode correctly"
  exit 1
fi