#Task 3: 
import csv 

with open ("../csv/employees.csv", newline= "") as csvfile: 
        reader = csv.reader(csvfile)
        employees = list(reader)

names = [row[1] + " " + row[2] for row in employees[1:]]
print(names)

names_with_e = [name for name in names if "e" in name.lower()]
print(names_with_e)
