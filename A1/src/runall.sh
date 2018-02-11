#!/bin/bash

TEST_DIR="../tests/test_cases/"

for i in `ls $TEST_DIR`; do
    echo -e "\n\n--------------------\n$i\n"
    python3 search.py 1 < "$TEST_DIR$i"
    echo "Finished $i" 1>&2
done

