### Restriction Enzyme
### Write a program which will calculate the size of two fragments after digested by EcoRI.

#######################################################
#1. Input the DNA sequence
#2. Figure out after digested fragments (cutting site: G*AATTC)
#3. Calculate the fragments size

#######################################################
seq = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
cutted_seq = seq.replace("AATTC", "_AATTC").split("_")
for i in range(len(cutted_seq)):
		print("The " + cutted_seq[i-1] + " is " + str(len(cutted_seq[i-1])) + " bp.")
