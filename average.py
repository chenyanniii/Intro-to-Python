##  average.py 
# Calculate sum from 1 to 20
#Part 1
total = 0
for i in range (1,21): 
	total = i + total
print("The sum from 1 to 20 is " + str(total) + ".")
	
#Part 2
x = list(range(1,21))
y = sum(x)
print("The sum from 1 to 20 is " + str(y) + ".")
