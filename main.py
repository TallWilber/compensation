
import pandas as pd
import csv

if __name__ == '__main__':
    datafile = input('What is the filename? ')
    lookup_id = input('What is the lookup value? ')

    with open(datafile, 'r') as f:
        csv_file = csv.reader(f, delimiter=",")
    # loop through the csv list
        for row in csv_file:
            # if current rows 2nd value is equal to input, print that row
            if lookup_id == row[0]:
                print(row)
                print(f"Name: {row[1]}, Salary: {row[2]}")

    # pull data from file
    # with open(datafile, 'r') as data:
    #     dict_reader = DictReader(data)
    #     list_of_dict = list(dict_reader)
    #     print(list_of_dict)
    #     df = pd.DataFrame(list_of_dict)

    # perform operation
    #result = df[df['ID'] == lookup_id]
    #if not result.empty:
    #    name = result['Name'].values[0]
    #    salary = result['Salary'].values[0]
    #    print(f"Name: {name}, Salary: {salary}")
    #else:
    #    print("ID not found")
