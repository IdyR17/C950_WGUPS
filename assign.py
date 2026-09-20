#Package Assigning Algorithm for WGUPS
#  To make the route, we also have to take the constraints into consideration. The following logic will be implemented on top of Nearest Neighbor:
# Truck 1: early deadline / group that needs to be delivered together
# Truck 2: Truck 2 ONLY packages. Package delayed with early delivery
# Truck 3: Package 9 (waiting for correct address), packages delayed with EOD deliveries, other packages to choose, as needed
# To be able to deliver in less miles, a greedy distance approach to assign the package to the closest truck

def assign_packages(truck1,truck2,truck3,packages,total_packages,addresses,distances,get_distance):

    # Truck 1 - packages that must be delivered together
    truck1_packages = [13, 14, 15, 16, 19, 20]

    # Truck 2 - Truck 2 only and delayed early-deadline packages
    truck2_packages = [3, 6, 18, 25, 36, 38]

    # Truck 3 - wrong address and delayed EOD packages
    truck3_packages = [9, 28, 32]

    # Load packages
    for package_id in truck1_packages:
        truck1.add_package(package_id)

    for package_id in truck2_packages:
        truck2.add_package(package_id)

    for package_id in truck3_packages:
        truck3.add_package(package_id)

    # Assign remaining packages based on distance
    for package_id in range(1, total_packages + 1):
        if package_id in (truck1.package_ids+truck2.package_ids+truck3.package_ids): 
            continue
        package = packages.get_package(package_id)

        # Only assign deadline packages right now
        if package.deadline != "EOD":
            closest_truck = find_closest_truck(
                package,
                [truck1, truck2],
                packages,
                addresses,
                distances,
                get_distance
        )

            closest_truck.add_package(package_id)
    # Assign the remaining EOD packages to the closest truck
    for package_id in range(1, total_packages + 1):

        # Skip packages that are already assigned
        if package_id in (truck1.package_ids + truck2.package_ids + truck3.package_ids):
            continue

        package = packages.get_package(package_id)

        closest_truck = find_closest_truck(
            package,
            [truck1, truck2, truck3],
            packages,
            addresses,
            distances,
            get_distance
        )

        if closest_truck is not None:
            closest_truck.add_package(package_id)    


#Algorithm for finding the closest truck using a greedy distance approach
def find_closest_truck(package, trucks, packages, addresses, distances, get_distance):
    closest_truck = None
    closest_distance = float("inf")

    for truck in trucks:

        # Skip if full
        if len(truck.package_ids) >= 16:
            continue

        # Compare with packages already assigned to this truck
        for assigned_id in truck.package_ids:
            assigned_package = packages.get_package(assigned_id)

            distance = get_distance(
                package.address,
                assigned_package.address,
                addresses,
                distances
            )

            if distance < closest_distance:
                closest_distance = distance
                closest_truck = truck

    return closest_truck