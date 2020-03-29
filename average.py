##  average.py 
# Calculate average from 1 to 20
#Part 1
total = 0
for i in range (1,21): 
	total = i + total
print(total)
print("The average from 1 to 20 is " + str(total/len(range(1,21))) + ".")

	
#Part 2
x = list(range(1,21))
y = sum(x)
print("The average from 1 to 20 is " + str(y/len(range(1,21))) + ".")
