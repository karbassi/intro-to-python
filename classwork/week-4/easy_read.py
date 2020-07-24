#!/usr/bin/env python3

import pandas

# df is short for DataFrame
df = pandas.read_csv(
    "students.csv", index_col="preferred_first_name", parse_dates=["birthday"]
)

# print(df["preferred_first_name"][7])
print(df["birthday"]["Eddie"])
