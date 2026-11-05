import csv
with open("sports_scores.csv", newline="") as file:
    for row in csv.DictReader(file):
        print(row)