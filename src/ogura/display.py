import json, os, sys, time, random

def bold(str): # Returns str in bold
    return "\033[1m" + str + "\033[0m"

def print_gradual(str, timeout): # Print character by character with a time delay
    for c in str:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(timeout)

with open("./ogura.json", "r") as p:
    data = json.load(p)

i = random.randint(0, 99)
print()
print_gradual(data["japanese"][i]["line"], 0.05)
print()
print_gradual(data["romaji"][i]["line"], 0.03)
print()
print_gradual(data["english"][i]["line"], 0.03)
print()
