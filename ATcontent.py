###ATcontent
########################################################################
#1. Write a program that will print out AT content of this DNA sequence.
#2. calculate numbers of AT content in Python.

########################################################################
#1. Input the DNA sequence
#2. Count base pair for each type
#3. Calculate the AT content (percentage)

########################################################################

seq = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
dna_count = seq.count("A") + seq.count("T") + seq.count("G") + seq.count("C")
at_count = seq.count("A") + seq.count("T")
at_content = at_count / dna_count

print("The AT content for this sequence is " + str(at_content) + ".")
