#!/usr/bin/env bash

set -e

. ~/.virtualenvs/python2.7/bin/activate
PYTHONPATH=. python -m pystache.command.test
