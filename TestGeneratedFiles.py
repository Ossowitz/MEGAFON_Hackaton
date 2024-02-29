import unittest
import os
import csv


class TestGeneratedFiles(unittest.TestCase):

    def test_files_creation(self):
        people_directory = os.path.abspath("com.nexign/people")
        expected_header = ["name", "b_day", "active", "po"]

        file_counts = {
            "b2b": 7,
            "b2c": 6
        }

        for file_type, count in file_counts.items():
            for i in range(1, count + 1):
                file_path = os.path.join(people_directory, f"{file_type}_{i}.csv")
                self.assertTrue(os.path.isfile(file_path))  # Проверка наличия файла

                with open(file_path, "r") as file:
                    reader = csv.reader(file)

                    # Проверка заголовка
                    header = next(reader)
                    self.assertEqual(header, expected_header)  # Проверка соответствия заголовка

                    rows = list(reader)
                    self.assertEqual(len(rows), 100)  # Проверка количества строк
