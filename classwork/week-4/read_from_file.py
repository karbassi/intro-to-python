#!/usr/bin/env python3

import csv

with open("students.csv", mode="r") as csv_file:
    reader = csv.DictReader(csv_file, delimiter=",")

    line_count = 0

    for row in reader:
        if line_count == 0:
            print(f'Columns are: { ",".join(row) }')
            line_count += 1
        else:
            print(f"{row['preferred_first_name']} was born on {row['birthday']}.")
            line_count += 1

    print(f"There are {line_count} lines in the file.")
