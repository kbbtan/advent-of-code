# Day 24: Crossed Wires

## Star 1

We can trace the series of gates to compute the signal at each output wire.

## Star 2

Our task is to ensure that the logic gates form a [Full Adder Circuit](https://en.wikipedia.org/wiki/Adder_(electronics)). Note that the sequence of outputs follow a pattern (using random intermediate wire names):

```
z00: x00 XOR y00

---

z01: aaa XOR bbb
aaa - x00 AND y00
bbb - x01 XOR y01

---

z02: ccc XOR ddd
ccc - eee OR fff
eee - aaa AND bbb
fff - x01 AND y01
ddd - x02 XOR y02
```

The code provided helps to debug and identify which output bits are incorrect. Then, it is up to you to manually check the input and observe where the above pattern fails. 

Afterwards, you can edit the code in line 113 to swap the output wires and continue checking for more incorrect outputs:
```python
# INSERT HERE TO SWAP GATES MANUALLY.
# Example: gates["z01"], gates["z02"] = gates["z02"], gates["z01"]
```

Note that the given input may pass using **less than four swaps**. In this case, you also need to edit the input bits (`x` and `y`) to test the circuit with other inputs. You can still use the provided code to compare the circuit output with the expected output for other inputs.

Once you have identified eight output wires to swap, add them to the list on line 134 and the code will format your answer to the required format:
```python
# Insert gates swapped here.
swapped = []
return ",".join(sorted(swapped))
```