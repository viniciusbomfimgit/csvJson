
import csv, json

csvFilePath = "shopping.csv"
jsonFilePath = "data.js"


with open(csvFilePath) as file:
    reader = csv.DictReader(file)
    rows = list(reader)


with open(jsonFilePath, "w") as file:
    json.dump(rows, file, indent=5)


