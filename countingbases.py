#countingbases.py
import random
bases = ["A", "C", "T", "G"]
sequence = random.choices(bases, k=100)
print(sequence)

print(sequence.count("G"))
print(sequence.count("A"))
print(sequence.count("A") + sequence.count("C"))
