#Student ID: 010585953
import csv
from package import Package
from hash_table import HashTable
from truck import Truck

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

def load_distances(csv_file):
    addresses = []
    distances = []
    with open(csv_file, "r", encoding="utf-8-sig") as file:
        distance_data = csv.reader(file)
        
        for row_number, row in enumerate(distance_data): #skip the non-distance rows
            if row_number <8:
                continue
            addresses.append(row[1].split("\n")[0].strip()) #clean up address
            distances.append(list(filter(None, row[2:])))  # Filter out empties
        return addresses, distances

def get_distance(a,b,addresses, distances):
    #calculate between two addresses
    index_a=addresses.index(a)
    index_b=addresses.index(b)

    return float(distances[max(index_a,index_b)][min(index_a,index_b)])

package_table = HashTable()  # Create a package hash table to store the Package objects
load_packages("packages.csv", package_table)
for i in range(1, 41):  # Print all packages from 1 to 40
    print(package_table.get_package(i))

#Testing the truck class
trucktest=Truck(1, "08:00 AM")
for i in range(1, 18):  # Add 17 packages to the truck, last one should fail since the max load is 16 packages
    trucktest.add_package(i)

print(trucktest.package_ids) #last one shouldn't be added
print(trucktest.current_location)  #HUB
print(trucktest.miles) #0 so far

print("Distance testing")
addresses, distances = load_distances("distances.csv")
print(get_distance("HUB", "1060 Dalton Ave S", addresses, distances))
print(get_distance("1060 Dalton Ave S", "HUB", addresses, distances))
print(get_distance("HUB", "1330 2100 S", addresses, distances))
print(get_distance("1060 Dalton Ave S", "1330 2100 S", addresses, distances))