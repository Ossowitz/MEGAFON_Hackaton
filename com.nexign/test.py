import os

root_directory = os.path.dirname(os.path.abspath(__file__))

people_directory = os.path.join(root_directory, "people")
os.makedirs(people_directory, exist_ok=True)
