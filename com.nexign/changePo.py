# -*- coding: cp1251 -*-
import os
import csv

root_directory = os.path.dirname(os.path.abspath(__file__))
people_directory = os.path.join(root_directory, "people")


def update_name_column(file_path):
    data_rows = []
    with open(file_path, "r", newline="") as file:
        reader = csv.reader(file)
        header = next(reader)
        for row in reader:
            if row[3] == '99':
                row[0] = "Ilya Tikhomirov"
            data_rows.append(row)

    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        for data_row in data_rows:
            writer.writerow(data_row)


for i in range(1, 8):
    file_path = os.path.join(people_directory, f"b2b_{i}.csv")
    if os.path.exists(file_path):
        update_name_column(file_path)

for j in range(1, 7):
    file_path = os.path.join(people_directory, f"b2c_{j}.csv")
    if os.path.exists(file_path):
        update_name_column(file_path)

print("Values updated for 'name' column when 'po' is equal to 99 in all files.")
