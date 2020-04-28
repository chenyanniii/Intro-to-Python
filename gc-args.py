### GC-content with Argparse
### Yanni Chen
### 4/27/2020

##################################################
# 1. Create a random DNA sequence with argparse
# 2. Break the sequence into smaller sequences with argparse
# 3. Create a histogram of GC-content distribution in fragments"
##################################################

import argparse
import random
import pandas as pd
import matplotlib.pyplot as plt

argp = argparse.ArgumentParser()
argp.add_argument("-l", "--LENGTH", required=True, type = int, help="Please enter the length of your input sequence (bp)")
argp.add_argument("-f", "--FRAGMENT", required=True, type = int, help="Please enter the fragment size of your post process sequence (bp)")
args=vars(argp.parse_args())

print("##################################################") 
print("# 1. Create a random DNA sequence with argparse")


bases = ['A', 'T', 'G', 'C']
random_bases =  random.choices(bases, k=args["LENGTH"])
seq =','.join(random_bases).replace(',', '')
print(seq)

print("##################################################") 
print("# 2. Break the sequence into smaller sequences with argparse")
x=args["FRAGMENT"]
seq_x = [seq[i:i+x] for i in range(0, len(seq), x)]
print(seq_x)

print("##################################################") 
print("# 3. Create a histogram of GC-content distribution in fragments")

### 3-1 GC content function
def GC_content(input_seq):
	"""This function is used to calculate the GC content of each input sequence"""
	dna_count = input_seq.count('A') + input_seq.count('T') + input_seq.count('G') + input_seq.count('C') 
	gc_count = input_seq.count('G') + input_seq.count('C') 
	gc_content = gc_count / dna_count
	return(gc_content)
	
### 3-2 Calculate GC content
gc_each = [GC_content(i) for i in seq_x]

### 3-3 Plot GC content in histgram
n, bins, patches = plt.hist(x=gc_each, bins='auto', color='#0504aa',alpha = 0.7, rwidth = 0.85)
plt.grid(axis='y', alpha=0.75)
plt.xlabel('GC content')
plt.ylabel('Frequency')
plt.title('My GC content Histogram')
plt.text(25,45, r'$\mu=15, b = 3$')
maxfreq = n.max()
plt.show()
