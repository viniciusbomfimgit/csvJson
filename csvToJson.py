
import csv, json

csvFilePath = "shopping.csv"
jsonFilePath = "data.js"


with open(csvFilePath) as f:
    reader = csv.DictReader(f)
    rows = list(reader)


with open(jsonFilePath, "w") as f:
    json.dump(rows, f, indent=5)
