#!/bin/bash

TEST_DIR="../tests/test_cases/"

for i in `ls $TEST_DIR`; do
    echo -e "\n\n________________________________________________________\n$i\n"
    python3 search.py "--run-bfs" < "$TEST_DIR$i"
    echo -e "\nFinished $i\n" 1>&2
done

