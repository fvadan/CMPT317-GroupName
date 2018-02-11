#!/bin/sh

for i in `ls tests/test_cases`; do
    echo "\n\n--------------------\n$i\n"
    python3 search.py 1 < "tests/test_cases/$i"
    echo "Finished $i" 1>&2
done

