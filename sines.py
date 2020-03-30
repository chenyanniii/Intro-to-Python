### sines
### reorganize the data by Pandads.

#########################################################
#1. Download the data avan_rm.bed from HPCC.
#2. Name the column names.
#3. Find families in the data frame
#4. Build new data frame using only family "SINE"
#5. Drop column "Strand" and "Score"
#6. Create new column "Length"
#7. Determine min, max, and mean for all SINEs
#8. Determine min, max, and mean length for each sub-family of SINE (metulj and ZenoSINE)

#########################################################
import pandas as pd

col = ("Scaffold","Start","Stop","Element","Score", \
"Strand","Family","Sub-Family","Divergence")
df = pd.read_csv("aVan_rm.bed", names = col, sep = "\t")
print("There are " + str(len(df.Family.unique())) + " unique families.")

df_SINE = df[df["Family"] == "SINE"]
df_simple = df_SINE.drop(["Strand","Score"],axis=1)
df_simple["Length"] = df_simple["Stop"] - df_simple["Start"]

print("The minmum length in SINA is " + str(df_simple["Length"].min()) + ".")
print("The maximum length in SINA is " + str(df_simple["Length"].max()) + ".")
print("The mean length in SINA is " + str(df_simple["Length"].mean()) + ".")

df_metulj = df_simple[df_simple["Sub-Family"] == "metulj"]
df_ZenoSINE = df_simple[df_simple["Sub-Family"] == "ZenoSINE"]

print("The minmum length in metulj is " + str(df_metulj["Length"].min()) + \
", and in ZenoSINE is " + str(df_ZenoSINE["Length"].min()) + ".")
print("The maximum length in metulj is " + str(df_metulj["Length"].max()) + \
", and in ZenoSINE is " + str(df_ZenoSINE["Length"].max()) + ".")
print("The mean length in metulj is " + str(df_metulj["Length"].mean()) + \
", and in ZenoSINE is " + str(df_ZenoSINE["Length"].mean()) + ".")
