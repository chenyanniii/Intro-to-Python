## littlelists.py
## Yanni Chen
## 4/8/2020

###############################################
string = 'The quick brown fox jumped over the lazy dog'
print(string)

print("###############################################")
print("#1 Count the number of spaces in the string")
print("The number of spaces in the string is " + str(string.count (" ")) + ".")



print("###############################################")
print("#2 Find all the words that have the letter 'o' in the string.")
words = string.split(" ")
print("#2-1 do it in loop")
words_o_lp = []
for i in words:
		if i.count("o") > 0:
			words_o_lp.append(i)			
print("The words contain 'o' are " + str(words_o_lp) + ".") 

print("#2-2 do it by list comprehension")
words_o_lstcom = [i for i in words if i.count('o') > 0]
print("The words contain 'o' are " + str(words_o_lstcom) + ".") 



print("###############################################")
print("#3 Find all the words that have at least 5 letters in the string.")
print("#3-1 do it in loop")
words_5_lp = []
for i in words:
		if len(i) >= 5:
			words_5_lp.append(i)			
print("The words at least 5 letters are " + str(words_5_lp) + ".") 

print("#3-2 do it by list comprehension")
words_5_lstcom = [i for i in words if len(i) >= 5]
print("The words at least 5 letters are " + str(words_5_lstcom) + ".") 



print("###############################################")
print("#4 Find all the numbers from 1 to 1000 that have a '3' in it.")
num = list(range(1,1001))
print("#4-1 do it in loop")
num_3_lp = []
for i in num:
	if str(i).count("3") > 0:
		num_3_lp.append(i)
print("Please see the numbers include 3 here: " + str(num_3_lp) + ".")

print("#4-2 do it by list comprehension")
num_3_lstcom = [i for i in num if str(i).count("3") > 0]
print("Please see the numbers include 3 here: " + str(num_3_lstcom) + ".")
