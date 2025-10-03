#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.


numTerms = 0
while True:
    try:
        numTerms = int(input('How many terms in the fiboacci sequence: '))
        if numTerms <= 0:
            print('Error, please enter a positive integer value')
        else:
            break
    except:
        print('Error, please enter a positive integer value')

terms = []

for x in range(numTerms):
    if x == 0:
        terms.append(0)
    elif x == 1:
        terms.append(1)
    else:
        terms.append(terms[-1] + terms[-2])

print(*terms)