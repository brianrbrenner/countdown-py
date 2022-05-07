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
