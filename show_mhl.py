#! /usr/bin/env python
"""
stampa il file .mhl usato come argomento

"""

import xmltodict
import json
import argparse

# gestisce argomenti
parser = argparse.ArgumentParser()
parser.add_argument("file", help="file mhl da leggere")
args = parser.parse_args()

# nome del file
filepath = args.file

with open(filepath, 'r') as myfile:
    obj = xmltodict.parse(myfile.read())
print(json.dumps(obj, sort_keys=True, indent=4))