import json
import pkg_resources
import random
from .display import print_gradual


def main():
    with open(pkg_resources.resource_filename(__name__, "ogura.json"), "r") as p:
        data = json.load(p)

    i = random.randint(0, 99)
    print()
    print_gradual(data["japanese"][i]["line"] + "\n", 0.05)
    print_gradual(data["romaji"][i]["line"] + "\n", 0.03)
    print_gradual(data["english"][i]["line"] + "\n", 0.03)
