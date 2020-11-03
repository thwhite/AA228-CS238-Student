import csv

def read_data(data_name):
    with open(data_name) as csv_file:
        medium_reader = csv.reader(csv_file, delimiter=',')
        medium_data = list(medium_reader)
        medium_data.pop(0)
    return medium_data