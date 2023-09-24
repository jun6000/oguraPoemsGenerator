import sys
import time


def print_gradual(str, timeout):
    for c in str:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(timeout)
