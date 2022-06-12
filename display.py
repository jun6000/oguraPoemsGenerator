import json, os, sys, time

def print_gradual(str, timeout): # Print character by character with a time delay
    for c in str:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(timeout)

with open("ogura.json", "r") as p:
    data = json.load(p)

for i in range(100):
    print_gradual(data["japanese"][i]["line"], 0.05)
    print()
    print_gradual(data["romaji"][i]["line"], 0.03)
    print()
    print_gradual(data["english"][i]["line"], 0.03)
    print()