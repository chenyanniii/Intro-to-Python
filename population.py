#Population calculation
#Yanni Chen
#1/29/2020

#import module
#add any variable
#ask for input
#calculation
#print

initial_pop = 307357870
days_year = 356
sec_year = days_year * 24 * 60 * 60
birth_rate = int (sec_year / 7)
death_rate = int (sec_year / 13)
immigration_rate = int (sec_year / 35)

print(sec_year)
print("Birth Rate:", birth_rate, "per year")
print("Death Rate:", death_rate, "per year")
print("Immagration Rate:", immigration_rate, "per year")

#Inputs
year_input = input("How many years for population change?")

year_int = int(year_input)

population = initial_pop + (birth_rate + immigration_rate) * year_int - death_rate * year_int

print("After", year_int, "population is", population)
