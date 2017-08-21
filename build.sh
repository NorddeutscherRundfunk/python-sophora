#!/bin/bash

if [ ! -d venv ] ; then
    python3 -m venv venv
fi

source venv/bin/activate

echo "installing from requirements.txt"
pip -q install -r requirements.txt
