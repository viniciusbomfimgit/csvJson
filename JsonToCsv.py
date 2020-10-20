import json
import csv


with open("shopping.json",encoding='utf-8') as file:
    data = json.load(file)

    fname = "arquivo_gerado1.csv"

with open(fname,"w") as file:
    csv_file = csv.writer((file),delimiter='|',quotechar=' ', quoting=csv.QUOTE_MINIMAL)
    csv_file.writerow(["Id","Name","Description","Quantity","Value","Total"])

    
   
    
    for item in data["order"]:
        csv_file.writerow([item['id'],item['name'],item['description'],item['quantity'],item['value']])

    



    csv_file.writerow(["Total"] + [" "] * 4 + [item['value']+ 50.4 + 55.5])




    
