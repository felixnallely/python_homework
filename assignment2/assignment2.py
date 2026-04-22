import os 
import custom_module 

#Task 2: 
import csv 
import traceback 

def read_employees():
    data = {}
    rows = []

    try:
        with open("../csv/employees.csv", newline= "") as csvfile:
            reader = csv.reader(csvfile)

            for i, row in enumerate(reader):
                if i == 0:
                    data["fields"] = row
                else:
                    rows.append(row)
        data["rows"] = rows
        return data
    except Exception as e: 
        print("Exception occurred.")
        trace_back = traceback.extract_tb(e._traceback_)
        stack_trace = []
        for trace in trace_back:
            stack_trace.append(
                f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}'
            )
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message: 
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
        exit()
employees = read_employees()
print(employees)


#Task 3: 
def column_index(first_name):
    return employees["fields"].index(first_name)

employee_id_column = column_index("employee_id")


#Task 4: 
def first_name(employee_id):
    employee_id_str = str(employee_id)

    for row in employees["rows"]:
        if row[employee_id_column]== employee_id_str:
            first_name_column = column_index("first_name")
            return row[first_name_column]
        

#Task 5: 
def employee_find(employee_id):
    employee_id_str =str(employee_id)
    def employee_match(row):
        return row[employee_id_column] == employee_id_str
    matches = list(filter(employee_match, employees["rows"]))
    return matches 


#Task 6:
def employee_find_2(employee_id):
    matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id, employees["rows"]))
    return matches 


#Task 7: 
def sort_by_last_name():
    last_name_column = column_index("last_name")

    employees["rows"].sort(
        key= lambda row : row[last_name_column]
    )

    return employees["rows"]


#Task 8: 
def employee_dict(row):
    employee = {}

    for i, field in enumerate(employees["fields"]):
        if field == "employee_id":
            continue
        employee[field] = row[i]
    return employee


# Task 9:
def all_employees_dict():
    all_employees = {}

    employee_id_index = employees["fields"].index("employee_id") 

    for row in employees["rows"]:
        emp_data = employee_dict(row)
        emp_id = row[employee_id_index]
        all_employees[emp_id] = emp_data

    return all_employees

all_employees = all_employees_dict()
print(all_employees)


#Task 10: 
def get_this_value():
    return os.getenv("THISVALUE")


#Task 11:
def set_that_secret(new_secret):
    return custom_module.set_secret(new_secret)

set_that_secret("Hi")
print(custom_module.secret)



#Task 12:
def read_minutes_file(path):
    minutes_dict = {"fields": [], "rows": []}

    with open(path, newline= "") as file:
        reader = csv.reader(file)
        for i, row in enumerate(reader):
            if i == 0:
                minutes_dict["fields"] = row
            else:
                minutes_dict["rows"].append(tuple(row))
    return minutes_dict

def read_minutes():
    minutes1 = read_minutes_file("../csv/minutes1.csv")
    minutes2 = read_minutes_file("../csv/minutes2.csv")
    return minutes1, minutes2

minutes1, minutes2 = read_minutes()
print(minutes1)
print(minutes2)



#Task 13:
def create_minutes_set():
    set1 = set(minutes1["rows"])
    set2 = set(minutes2["rows"])
    return set1 | set2

minutes_set = create_minutes_set()


#Task 14:
from datetime import datetime

def create_minutes_list():
    minutes_list = list(minutes_set)

    convert = map(
        lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_list
        )

    return list(convert)

minutes_list = create_minutes_list()
print(minutes_list)


#Task 15: 
def write_sorted_list():
    sorted_data = sorted(minutes_list, key= lambda x: x[1])
    converted = list(map(
        lambda x: (x[0], datetime.strftime(x[1], "%B %d, %Y")),
        sorted_data
    ))

    with open("./minutes.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(minutes1["fields"])
        writer.writerows(converted)
    return list(converted)

sorted_minutes = write_sorted_list()
print(sorted_minutes)
#converted_list = write_sorted_list()


