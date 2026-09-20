#Student ID: 010585953
import csv
from ui import main_menu, format_time
from package import Package
from hash_table import HashTable
from truck import Truck
from routing import make_route
from assign import assign_packages

print("WGUPS Routing Program")


#Normalizing addresses (South=S, East = E, North = N, West = W) so that the package and distance table match
fix_address = lambda address:(
    address.replace("South", "S")
    .replace("East", "E")
    .replace("North", "N")
    .replace("West","W") 
)


#Load package data from the csv file into the hash table

def load_packages(csv_file, hash_table):
    with open(csv_file, "r", encoding="utf-8-sig") as file:
        package_data = csv.reader(file)

        for row in package_data:
            #skip non-package rows (if there's no package ID in the first column)
            if not row[0].isdigit():
                continue

            package_id = int(row[0])
            address = fix_address(row[1])
            city = row[2]
            state = row[3]
            zip_code = row[4]
            deadline = row[5]
            weight = row[6]
            special_notes = row[7]

            package = Package(package_id, address, city, state, zip_code, deadline, weight, special_notes)
            hash_table.insert(package_id, package)
#Function to load distance data from csv
def load_distances(csv_file):
    addresses = []
    distances = []
    with open(csv_file, "r", encoding="utf-8-sig") as file:
        distance_data = csv.reader(file)
        
        for row_number, row in enumerate(distance_data): #skip the non-distance rows
            if row_number <8:
                continue
            addresses.append(fix_address(row[1].split("\n")[0].strip())) #clean up address
            distances.append(list(filter(None, row[2:])))  # Filter out empties
        return addresses, distances

def get_distance(a,b,addresses, distances):
    #calculate between two addresses
    index_a=addresses.index(a)
    index_b=addresses.index(b)

    return float(distances[max(index_a,index_b)][min(index_a,index_b)])

packages = HashTable()  # Create a package hash table to store the Package objects
load_packages("packages.csv", packages)
addresses, distances = load_distances("distances.csv")

#Assigning logic

truck1 = Truck(1, 480)   # 8:00 AM Returns to Hub for truck change
truck2 = Truck(2, 545)   # 9:05 AM
truck3 = Truck(3, 620)   # 10:20 AM. To be changed after Truck 1 returns

assign_packages(
    truck1,
    truck2,
    truck3,
    packages,
    40,
    addresses,
    distances,
    get_distance
)

print("Truck 1:", truck1.package_ids)
print("Truck 1 count:", len(truck1.package_ids))

print("Truck 2:", truck2.package_ids)
print("Truck 2 count:", len(truck2.package_ids))

print("Truck 3:", truck3.package_ids)
print("Truck 3 count:", len(truck3.package_ids))

make_route(
    truck1,
    packages,
    addresses,
    distances,
    get_distance,
    to_hub=True
)

make_route(
    truck2,
    packages,
    addresses,
    distances,
    get_distance
)

# Truck 3 will leave when driver returns
truck3.departure_time=max(620, truck1.current_time)

#correct Package 9 address:
truck3.current_time=truck3.departure_time
package9 = packages.get_package(9)
package9.address = fix_address("410 S State St")

make_route(
    truck3,
    packages,
    addresses,
    distances,
    get_distance
)

print("\nTRUCK 1")
print("Route:", truck1.route)
print("Miles:", round(truck1.miles, 2))
print("Return:", format_time(truck1.current_time))

for package_id in truck1.route:
    package = packages.get_package(package_id)
    print(
        "Package:", package_id,
        "Delivered:", format_time(package.delivery_time),
        "Deadline:", package.deadline
    )

print("\nTRUCK 2")
print("Route:", truck2.route)
print("Miles:", round(truck2.miles, 2))
print("Return:", format_time(truck2.current_time))

for package_id in truck2.route:
    package = packages.get_package(package_id)
    print(
        "Package:", package_id,
        "Delivered:", format_time(package.delivery_time),
        "Deadline:", package.deadline
    )

print("\nTRUCK 3")
print("Route:", truck3.route)
print("Miles:", round(truck3.miles, 2))
print("Return:", format_time(truck3.current_time))

for package_id in truck3.route:
    package = packages.get_package(package_id)
    print(
        "Package:", package_id,
        "Delivered:", format_time(package.delivery_time),
        "Deadline:", package.deadline
    )

####################################
#Calculate total miles
total_miles = truck1.miles+truck2.miles+truck3.miles

#User Interface for WGUPS
main_menu(packages, 40, total_miles)