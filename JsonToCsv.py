import json
import csv


with open("shopping.json") as file:
    data = json.load(file)

    fname = "arquivo_gerado.csv"

with open(fname,"w") as file:
    csv_file = csv.writer(file)
    csv_file.writerow(["Id","Name","Description","Quantity","Value"])
    for item in data["order"]:
        csv_file.writerow([item['id'],item['name'],item['description'],item['quantity'],item['value']])

