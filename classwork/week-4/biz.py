#!/usr/bin/env python3

import pandas

# pandas.set_option("max_rows", None)

df = pandas.read_csv("Business_Owners.csv")

print(df["Account Number"].value_counts().plot())

# print(df["Account Number"])
