import csv
import pandas


# How  to read a csv file
with open('employee_birthday.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Columns names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} works at {row[1]} department, and was born in {row[2]}')
            line_count += 1
    print(f'Processed {line_count} lines')
#
#
# ##### Reading a CSV file into a Dictionary with csv

with open('employee_birthday.txt', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Columns names are {", ".join(row)}')
            line_count += 1

        print(f'\t{row["name"]} works at {row["department"]} department,and was born in {row["birthday month"]}')
        line_count += 1
    print(f'Processed {line_count} lines')



############## WRITING CSV FILES with csv

with open('employee_file.csv', mode='w') as employee_file:
    employee_writer = csv.writer(employee_file,delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)

    employee_writer.writerow(['John Smith', 'Accounting', 'November'])
    employee_writer.writerow(['Erica Meyers', 'IT', 'March'])

with open('employee_file2.csv', mode='w') as csv_file:
    fieldnames = ['emp_name', 'dept', 'birth_month']
    writer = csv.DictWriter(csv_file,fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'emp_name': 'Oloyede Paul', 'dept': 'Business Administration', 'birth_month': 'April'})
    writer.writerow({'emp_name': 'Oloyede Silas', 'dept': 'Theatre Art', 'birth_month': 'February'})
