"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here

    for values in items:
        key = str(values)

        if key in frequencies.keys():
            frequencies[key] += 1
        else:
            frequencies[key] = 1


    return frequencies


print(frequencies([100, 'Hello', '100', '100', 100]))
