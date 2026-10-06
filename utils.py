import json
import os

def loadRules() -> dict:
    with open('rules.json', 'r') as f:
        rules = json.load(f)
        if rules is not None:
            return rules