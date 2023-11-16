import os
from faker import Faker
import random
import csv

root_directory = os.path.dirname(os.path.abspath(__file__))

people_directory = os.path.join(root_directory, "people")
os.makedirs(people_directory, exist_ok=True)

faker = Faker()

header = ["name", "b_day", "active", "po"]

file_counts = {
    "b2b": 7,
    "b2c": 6
}

for file_type, count in file_counts.items():
    for i in range(1, count + 1):
        with open(os.path.join(people_directory, f"{file_type}_{i}.csv"), "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(header)
            for _ in range(100):
                writer.writerow(
                    [faker.name(),
                     faker.date_of_birth(),
                     random.choice(['yes', 'no']),
                     random.randint(1, 100)]
                )
