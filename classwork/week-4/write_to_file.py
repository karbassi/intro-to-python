#!/usr/bin/env python3

import csv

with open("cool_dogs.csv", mode="w") as csv_file:
    writer = csv.writer(
        csv_file, delimiter="😢", quotechar='"', quoting=csv.QUOTE_MINIMAL
    )

    writer.writerow(["name", "breed"])
    writer.writerow(["Toto, the dog", "Cairn Terrier"])
    writer.writerow(["Rin Tin Tin", "German Shepherd"])
    writer.writerow(["Lassie", "Rough Collie"])
    writer.writerow(["Hachiko", "Akita Inu"])
    writer.writerow(["Benji", "Mixed-breed"])
    writer.writerow(["Seymour Asses", "Border Terrier"])
