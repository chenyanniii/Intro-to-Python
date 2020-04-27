### Calculate the GC content for a DNA sequence
### Yanni Chen
### 4/27/2020

##################################################
# 1. Create a random DNA sequence that is 5,000 bp long
# 2. Break the sequence into smaller sequences 100 bp long
# 3. Creat a GC function to calculate GC content
# 4. Use the GC function to calculate GC content of each fragment
##################################################


print("##################################################") 
print("# 1. Create a random DNA sequence that is 5,000 bp long")
import random
bases = ['A', 'T', 'G', 'C']
random_bases =  random.choices(bases, k=5000)
seq =','.join(random_bases).replace(',', '')
print(seq)

print("##################################################") 
print("# 2. Break the sequence into smaller sequences 100 bp long")
x=100
seq_100 = [seq[i:i+100] for i in range(0, len(seq), x)]

print(seq_100)

print("##################################################") 
print("# 3. Creat a GC function to calculate GC content")

def GC_content(input_seq):
	"""This function is used to calculate the GC content of each input sequence"""
	dna_count = input_seq.count('A') + input_seq.count('T') + input_seq.count('G') + input_seq.count('C') 
	gc_count = input_seq.count('G') + input_seq.count('C') 
	gc_content = gc_count / dna_count
	print(gc_content)
	
print("##################################################") 
print("4. Use the GC function to calculate GC content of each fragment")
gc_each = [GC_content(i) for i in seq_100]
