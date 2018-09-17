import pandas


# datafile = pandas.read_csv('employee_data.csv')
# print(datafile)
#
#
# print(type(datafile['Hire Date'][1]))
#
#
# datafile = pandas.read_csv('employee_data.csv', index_col='Name')
# print(datafile)
#
# datafile = pandas.read_csv('employee_data.csv', index_col='Name', parse_dates=['Hire Date'])
# print(datafile)
# # print(type(datafile['Hire Date'][0]))

### Changing the colums names in the first line

datafile = pandas.read_csv('employee_data.csv',
                    index_col='Employee',
                    parse_dates=['Hired'],
                    header=0,
                    names=['Employee', 'Hired', 'Salary', 'Sick days'])

# print(datafile)

# Writing CSV file with pandas

datafile = pandas.read_csv('employee_data.csv',
                    index_col='Employee',
                    parse_dates=['Hired'],
                    header=0,
                    names=['Employee', 'Hired', 'Salary', 'Sick days'])
datafile.to_csv('employeeModified.csv')
