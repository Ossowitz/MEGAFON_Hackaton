import os

os.makedirs("people", exist_ok=True)

for i in range(1, 8):
    with open(f"people/b2b_{i}.csv", "w") as file:
        file.write("name,b_day,active,po\n")

for i in range(1, 7):
    with open(f"people/b2c_{i}.csv", "w") as file:
        file.write("name,b_day,active,po\n")

for i in range(1, 11):
    with open(f"people/{i}.csv", "w") as file:
        file.write("name,b_day,active,po\n")
