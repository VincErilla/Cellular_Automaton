import json

def loadRules() -> dict:
    with open('rules.json', 'r') as f:
        rules = json.load(f)
        if rules is not None:
            return rules

def loadState() -> list:
    with open('state.json', 'r') as f:
        grid = json.load(f)
        if grid is not None:
            return grid["grid"]

def saveState(grid: list) -> None:
    data = {"grid": grid}
    with open('state.json', 'w') as f:
        json.dump(f, data)