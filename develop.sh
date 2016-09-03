#!/bin/bash

virtualenv -p /usr/bin/python3.5 ve
. ve/bin/activate
pip install -U pip
pip install -r requirements.txt
pip install -r dev-requirements.txt
pip install -e .
