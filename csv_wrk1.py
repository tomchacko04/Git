import csv
with open("example.csv",mode="w", newline="") as file: #it will create and write the file example.csv
    writer = csv.writer(file)
    writer.writerow(["name", "age"])
    writer.writerow(["chacko", "58"])
    writer.writerow(["mathew", "28"])
    
with open("example.csv",mode="r") as file:
    reader = csv.reader(file)
    for row_item in reader:
        print(row_item)