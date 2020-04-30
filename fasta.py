### fasta.py
### Yanni Chen
### 4/29/2020

################################################################
#1. Argparse to read in fasta file “dIul.fa” AND the taxon name “dIul”
#2. Determine how many records are in the file
#3. What is the shortest record? What is the longest record? 
#4. Run your GC function on each record sequence
#5. Plot a histogram of GC content (Hint: may need to save the results first)
#6. Which record has most GC content? Which record has least GC content?
#7. Translate each record
#8. Which record has most Stop codons? Which record has least Stop codons?

################################################################
import argparse
import random
import pandas as pd
import matplotlib.pyplot as plt
from Bio.Seq import Seq
from Bio import SeqIO

print("################################################################")
print('#1. Argparse to read in fasta file “dIul.fa” AND the taxon name “dIul”')

#for i in SeqIO.parse("dIul.fa", "fasta"):
#	print(i.id)
i_id = [i.id for i in SeqIO.parse("dIul.fa","fasta")]
print("Argparsed file stored in 'i_id'.")



print("################################################################")
print("#2. Determine how many records are in the file")

# grep '>' dIul.fa | wc -l (need to be outside python)
print("There are " + str(len(i_id)) + " of reads in the file.")



print("################################################################")
print("#3. What is the shortest record? What is the longest record? ")

i_len = [len(i) for i in SeqIO.parse("dIul.fa","fasta")]
print("The shortest record is: ", min(i_len))
print("The longest record is: ", max(i_len))



print("################################################################")
print("#4. Run your GC function on each record sequence")

#def GC_content(input_seq):
#	"""This function is used to calculate the GC content of each input sequence"""
#	dna_count = input_seq.count('A') + input_seq.count('T') + input_seq.count('G') + input_seq.count('C') 
#	gc_count = input_seq.count('G') + input_seq.count('C') 
#	gc_content = gc_count / dna_count
#	return(gc_content)

#i_seq = [repr(i.seq) forh i in SeqIO.parse("dIul.fa", "fasta")]

#seq_1 = [seq[i:i+1] for i in rang(0, len(seq),1)]

#i_seq = [i.seq for i in SeqIO.parse("dIul.fa", "fasta")]
#i_seq[1].count("G")

#gc_each = [GC_content(i) for i in SeqIO.parse("dIul.fa","fasta")]

#g_count= [i.seq.count("G") for i in SeqIO.parse("dIul.fa", "fasta")]

#for i in SeqIO.parse("dIul.fa","fasta"):
#	g_count = i.seq.count("G")
#	c_count = i.seq.count("C")
#	a_count = i.seq.count("A")
#	t_count = i.seq.count("T")
#	gc_count = g_count + c_count
#	dna_count = gc_count + a_count + t_count
#	gc_each = gc_count / dna_count
#	print(gc_each)


#g_count = [i.seq.count("G") for i in SeqIO.parse("dIul.fa", "fasta")]
#c_count = [i.seq.count("C") for i in SeqIO.parse("dIul.fa", "fasta")]
#a_count = [i.seq.count("A") for i in SeqIO.parse("dIul.fa", "fasta")]
#t_count = [i.seq.count("T") for i in SeqIO.parse("dIul.fa", "fasta")]
		
gc_each = [(i.seq.count("G") + i.seq.count("C")) / (i.seq.count("G") + 
			i.seq.count("C") + i.seq.count("A") + i.seq.count("T")) for i in 
			SeqIO.parse("dIul.fa", "fasta")]
print("GC content of each record stored in 'gc_each'.")



print("################################################################")
print("#5. Plot a histogram of GC content")
n, bins, patches = plt.hist(x=gc_each, bins='auto', color='#0504aa',alpha = 0.7, rwidth = 0.85)
plt.grid(axis='y', alpha=0.75)
plt.xlabel('GC content')
plt.ylabel('Frequency')
plt.title('My GC content Histogram')
plt.text(25,45, r'$\mu=15, b = 3$')
maxfreq = n.max()
#plt.show()
plt.savefig('gc_hist.png')
print("The figure save as 'gc_hist.png'.")

print("################################################################")
print("#6. Which record has most GC content? Which record has least GC content?")

gc_min = [i for i,x in enumerate(gc_each) if x == min(gc_each)]
gc_max = [i for i,x in enumerate(gc_each) if x == max(gc_each)]

print("The most GC content is in positon: ", [(i_id[i]) for i in gc_max])
print("The least GC content is in position: ", [(i_id[i]) for i in gc_min])

print("################################################################")
print("#7. Translate each record")
i_translate = [i.translate for i in SeqIO.parse("dIul.fa","fasta")]
print("Translate record stored in i_translate.")


print("################################################################")
print("#8. Which record has most Stop codons? Which record has least Stop codons?")

i_stop = [i.seq.translate().count('*') for i in SeqIO.parse("dIul.fa","fasta")]
i_stop_min = [i for i,x in enumerate(i_stop) if x == min(i_stop)]
i_stop_max = [i for i,x in enumerate(i_stop) if x == max(i_stop)]

print("The record has most Stop codon is/are: ", [(i_id[i]) for i in i_stop_max])
print("The record has least Stop codon is/are: ", [(i_id[i]) for i in i_stop_min])




