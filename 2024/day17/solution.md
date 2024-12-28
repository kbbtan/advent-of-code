# Day 17: Chronospatial Computer

## Star 1

We can build the virtual computer using the set of instructions given to us (like building our own assembly-like compiler) and run the given program to output the results.

## Star 2

By decoding the program, we can observe that each additional digit of `A` in octet produces one output. Furthermore, each output only depends on its corresponding octet digit and its more significant digits. We can therefore build all possible `A`s from its most significant octet digit onwards, and compare them to find the smallest `A` possible.