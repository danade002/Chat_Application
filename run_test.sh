#!/usr/bin/env bash

chmod +x the_file_name
    
set -e

. ~/.virtualenvs/python2.7/bin/activate
PYTHONPATH=. python -m pystache.command.test
