#bats.py
species1=input("What is your species1")
species2=input("What is your species2")
species3=input("What is your species3")

sp1genus = species1.split(" ")[0][:3].upper()
sp1species = species1.split(" ")[1][:3].upper()
sp1code = sp1genus+sp1species
sp2genus = species2.split(" ")[0][:3].upper()
sp2species = species2.split(" ")[1][:3].upper()
sp2code = sp2genus + sp2species
sp3genus = species3.split(" ")[0][:3].upper()
sp3species = species3.split(" ")[1][:3].upper()
sp3code = sp3genus+sp3species
