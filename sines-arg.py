### SINE-ARGPARSE.py
### Yanni Chen
### 4/27/2020

import pandas as pd
import argparse
argp = argparse.ArgumentParser()
argp.add_argument("-r", "--READS", required=True, help="Please attach the path of your input file")
argp.add_argument("-f", "--FAMILY", required=True, type = str, help="Please retaing the SINE family")
argp.add_argument("-g", "--GENOME", required=True, type = int, help="Please intering the genome size of input")
args=vars(argp.parse_args())

#########################################################
#1. Import data
#2. Find families in the data frame
#3. Build new data frame using only family "SINE"
#4. Drop column "Strand" and "Score"
#5. Create new column "Length" and "Proportion"
#7. Determine min, max, and mean for all SINEs
#8. Determine min, max, and mean length for each sub-family of SINE (metulj and ZenoSINE)

#########################################################
### 1. Import data
col = ("Scaffold","Start","Stop","Element","Score", \
"Strand","Family","Sub-Family","Divergence")
df = pd.read_csv(args["READS"], names = col, sep = "\t")

##############################################################################################
### 2. Find families in the data frame
print("There are " + str(len(df.Family.unique())) + " unique families.")

##############################################################################################
### 3. Build new data frame using only family "SINE"
df_SINE = df[df["Family"] == args["FAMILY"]]

##############################################################################################
### 4. Drop column "Strand" and "Score"
df_simple = df_SINE.drop(["Strand","Score"],axis=1)

##############################################################################################
### 5. Create new column "Length" and "Proportion"
df_simple["Length"] = df_simple["Stop"] - df_simple["Start"]
df_simple["Proportion"] = df_simple["Length"] / args["GENOME"]

##############################################################################################
### 6-8 Determin min, max and mean
print("The minmum length in SINE is " + str(df_simple["Length"].min()) + ".")
print("The maximum length in SINE is " + str(df_simple["Length"].max()) + ".")
print("The mean length in SINE is " + str(df_simple["Length"].mean()) + ".")

print("The minmum sequence proportion in SINE is " + str(df_simple["Proportion"].min()) + ".")
print("The maximum sequence proportion in SINE is " + str(df_simple["Proportion"].max()) + ".")
print("The mean proportion in SINE is " + str(df_simple["Proportion"].mean()) + ".")

df_metulj = df_simple[df_simple["Sub-Family"] == "metulj"]
df_ZenoSINE = df_simple[df_simple["Sub-Family"] == "ZenoSINE"]

print("The minmum length in metulj is " + str(df_metulj["Length"].min()) + \
", and in ZenoSINE is " + str(df_ZenoSINE["Length"].min()) + ".")
print("The maximum length in metulj is " + str(df_metulj["Length"].max()) + \
", and in ZenoSINE is " + str(df_ZenoSINE["Length"].max()) + ".")
print("The mean length in metulj is " + str(df_metulj["Length"].mean()) + \
", and in ZenoSINE is " + str(df_ZenoSINE["Length"].mean()) + ".")

##############################################################################################
###9 Save the SINEs dataframe as “aVan.csv”
df_simple.to_csv("aVan.csv", sep='\t')
