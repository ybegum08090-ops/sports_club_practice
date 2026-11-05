import csv
with open("archive_sports.csv", newline="") as file:
    for row in csv.DictReader(file):
        print(row)