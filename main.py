#Student ID: 010585953
import csv
from package import Package
from hash_table import HashTable
from truck import Truck
from routing import make_route

print("WGUPS Routing Program")

# Time formatting to convert minutes since midnight to time format (HH:MM:SS AM/PM)
def format_time(minutes_since_midnight):
    total_seconds = round(minutes_since_midnight * 60)

    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60

    period = "AM"

    if hours >= 12:
        period = "PM"
    if hours > 12:
        hours -= 12
    if hours == 0:
        hours = 12

    return f"{hours}:{minutes:02d}:{seconds:02d} {period}"

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
trucktest1 = Truck(1, 480)

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
print("Final time:", trucktest1.current_time)

for package_id in trucktest1.route:
    package = packages.get_package(package_id)
    print(
        "Package:",
        package_id,
        "Departure:",
        format_time(package.departure_time),
        "Delivered:",
        format_time(package.delivery_time)
    )

#testing status

package1 = packages.get_package(1)
package28 = packages.get_package(28)

print("Package 1 at 8:05:", package1.get_current_status(485))
print("Package 28 at 9:00:", package28.get_current_status(540))
print("Package 28 at 9:10:", package28.get_current_status(550))