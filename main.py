#Student ID: 010585953
import csv
from package import Package
from hash_table import HashTable

print("WGUPS Routing Program")

#Load package data from the csv file into the hash table

def load_packages(csv_file, hash_table):
    with open(csv_file, "r", encoding="utf-8-sig") as file:
        package_data = csv.reader(file)

        for row in package_data:
            #skip non-package rows (if there's no package ID in the first column)
            if not row[0].isdigit():
                continue

            package_id = int(row[0])
            address = row[1]
            city = row[2]
            state = row[3]
            zip_code = row[4]
            deadline = row[5]
            weight = row[6]
            special_notes = row[7]

            package = Package(package_id, address, city, state, zip_code, deadline, weight, special_notes)
            hash_table.insert(package_id, package)

package_table = HashTable()  # Create a package hash table to store the Package objects
load_packages("packages.csv", package_table)
for i in range(1, 41):  # Print all packages from 1 to 40
    print(package_table.get_package(i))