#This is the routing algorithm for WGUPS.
#It is based on the Nearest Neighbor Algorithm - a greedy algorithm that finds the closest unvisited location.

def get_next_package(current_location, package_ids, packages, addresses, distances, get_distance):
    closest_package_id = None
    closest_distance = float('inf')

    for package_id in package_ids:
        package = packages.get_package(package_id)

        distance = get_distance(current_location, package.address, addresses, distances)
        if distance < closest_distance:
            closest_distance = distance
            closest_package_id = package_id

    return closest_package_id, closest_distance

def make_route(truck, packages, addresses, distances, get_distance):
    #list that will keep track of packages that havent been delivered yet
    undelivered_packages = truck.package_ids.copy()

    while undelivered_packages:
        next_package_id, distance = get_next_package(truck.current_location, undelivered_packages, packages, addresses, distances, get_distance)

        next_package = packages.get_package(next_package_id)

        truck.route.append(next_package_id)  # Add the package to the truck's route
        truck.miles += distance  # Update mileage
        truck.current_location = next_package.address  # Update current location

        undelivered_packages.remove(next_package_id)  # Remove the package from the undelivered list