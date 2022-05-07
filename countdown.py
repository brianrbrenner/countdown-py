# this version of countdown does not use a compliler and is instead interpretted.
# python uses dynamic types vs Rust's static types.
# In both examples however I am able to return tuples of ints back to the main function call.
# In python I do not need a main method and this program can run through my while loop at the bottom. 
# In the rust code the main method is how we run the program like in any C style language.
# Both examples are good examples of functional programming 
# python is arguably an easier arg parser, however, it's runtime is slower due to interpretation.
# Rust has the speed of C without needing dynamic memory allocation due to borrow checking, default immutability, etc...

import time
import argparse

# time conversion
def time_convert(total):
    min = int(total / 60)
    sec = total - min * 60
    return (min, sec)

# use argparse to parse given args as ints for total time
parser = argparse.ArgumentParser()
parser.add_argument('min', type=int)
parser.add_argument('sec', type=int)
args = parser.parse_args()

total = args.min * 60 + args.sec

# loop through total time and print updated time, convert it, then go until 0
while total:
    min, sec = time_convert(total)
    time_left = str(min).zfill(2)+ ":" + str(sec).zfill(2) # zfill to fill 2 columns
    print("count down: " + time_left + "\r", end="")
    time.sleep(1)
    total -= 1

print("\n")
