import json, os, sys, time

def print_gradual (str, timeout): # Print character by character with a time delay
    for c in str:
        sys.stdout.write (c)
        sys.stdout.flush ()
        time.sleep (timeout)

with open ("ogura.json", "r") as p:
    data = json.load (p)

print_gradual (data["japanese"][0]["line"], 0.05)
print ("\n")
print_gradual (data["english"][0]["line"], 0.05)
print ("\n")