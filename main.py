#Student ID: 010585953
import csv
from package import Package
from hash_table import HashTable

print("WGUPS Routing Program")

package_test1= Package(
    1,
    "1 abc st",
    "Bergenfield",
    "NJ",
    "07621",
    "8:00 AM",
    "7",
    "Nothing"
)

print(package_test1)

test_hash_table = HashTable()
#Testing with a real package object
test_hash_table.insert(package_test1.package_id, package_test1)
print(test_hash_table.get_package(1))  # Should print the package_test1 details

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

load_packages("packages.csv", test_hash_table)
for i in range(1, 41):  # Print all packages from 1 to 40
    print(test_hash_table.get_package(i))