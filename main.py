#Student ID: 010585953
import csv
from package import Package
from hash_table import HashTable
from truck import Truck
from routing import get_next_package, make_route

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

packages = HashTable()  # Create a package hash table to store the Package objects
load_packages("packages.csv", packages)

#Testing the routing algorithm with truck and package data
trucktest1 = Truck(1, "08:00 AM")

for package_id in [1, 3, 4, 5]:
    trucktest1.add_package(package_id)

addresses, distances = load_distances("distances.csv")

make_route(
    trucktest1,
    packages,
    addresses,
    distances,
    get_distance
)

print("Route:", trucktest1.route)
print("Miles:", trucktest1.miles)
print("Final location:", trucktest1.current_location)