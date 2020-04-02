###GOAL:Determine length of large gene on mRNA strand
### Yanni Chen
### 4/1/2020

#########################################################
#1.Generate a random RNA sequence into a STRING 1000 base pairs long
#2.Create a list of genes that are separated by start codon (AUG)
#3.Create a list of large genes (>50bp)
#4.Determine length of large genes

#########################################################
print("#########################################################")
#1.Generate a random RNA sequence into a STRING 1000 base pairs long
import random
bases = ['A','U','G','C']
random_bases = random.choices(bases, k=1000)
seq = ','.join(random_bases).replace(',','')
print("1. Generated 1000 base pairs long RNA sequence:")
print(seq)
print("#########################################################")

#2.Create a list of genes that are separated by start codon (AUG)
genes = seq.replace('AUG','_AUG').split('_')
print("2. Create a list of genes")
print(genes)
print("#########################################################")

#3.Create a list of large genes (>50 bp)
print("3. Create a list of large genes")
print("###loop for genes > 50 bp")	
genes_50=[]
for i in range(len(genes)):
		if len(genes[i]) > 50:
				print(genes[i]) 
				genes_50.append(genes[i])

print("##final results")	
print(genes_50)
print("#########################################################")
