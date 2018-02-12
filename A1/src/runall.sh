#!/bin/bash

TEST_DIR="../tests/test_cases/"

for i in `ls -1 $TEST_DIR | grep -v "3422.txt"`; do
    echo -e "\n\n________________________________________________________\n$i\n"
    python3 search.py "--run-bfs" < "$TEST_DIR$i"
    echo -e "\nFinished $i\n" 1>&2
done

echo -e "\n\n________________________________________________________\n3422.txt\n"
python3 search.py < "$TEST_DIR""3422.txt"
echo -e "\nFinished 3422.txt\n" 1>&2
