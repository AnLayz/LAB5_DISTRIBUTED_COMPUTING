#!/usr/bin/python3
import sys

current_word = None
current_count = 0
word = None

# Read input from standard input
for line in sys.stdin:
    # Remove whitespace
    line = line.strip()
    
    # Parse the input we got from mapper.py
    try:
        word, count = line.split('\t', 1)
        count = int(count)
    except ValueError:
        continue

    # Setup logic for aggregation
    if current_word == word:
        current_count += count
    else:
        if current_word:
            # Write result to standard output
            print(f"{current_word}\t{current_count}")
        current_word = word
        current_count = count

# Output the last word if needed
if current_word == word:
    print(f"{current_word}\t{current_count}")