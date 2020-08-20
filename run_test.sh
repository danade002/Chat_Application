#!/usr/bin/env bash

chmod u+r+x run_test.sh
    ./run_test.sh
    
set -e

. ~/.virtualenvs/python2.7/bin/activate
PYTHONPATH=. python -m pystache.command.test
