# This is the routing algorithm for WGUPS.
# It is based on the Nearest Neighbor Algorithm - a greedy algorithm that finds the closest unvisited location.
# It builds the delivery route for one truck by repeatedly selecting the next package using get_next_package()
# it also updates miles and travel time, package delivery time.
# Continues until each pacakge has been delivered


def get_next_package(
    current_location, package_ids, packages, addresses, distances, get_distance
):
    closest_package_id = None
    closest_distance = float("inf")
    priority_packages = []

    # Find packages that still have an early deadline
    for package_id in package_ids:
        package = packages.get_package(package_id)

        if package.deadline != "EOD":
            priority_packages.append(package_id)

    # Prioritize deadline packages if there are any left
    if priority_packages:
        packages_to_check = priority_packages
    else:
        packages_to_check = package_ids

    # Nearest Neighbor: compare each pacakge and keep the one closest to the truck's current location
    for package_id in packages_to_check:
        package = packages.get_package(package_id)

        distance = get_distance(current_location, package.address, addresses, distances)

        if distance < closest_distance:
            closest_distance = distance
            closest_package_id = package_id

    return closest_package_id, closest_distance


def make_route(truck, packages, addresses, distances, get_distance, to_hub=False):
    # list that will keep track of packages that havent been delivered yet
    undelivered_packages = truck.package_ids.copy()
    # continues choosing the next closest package
    while undelivered_packages:
        next_package_id, distance = get_next_package(
            truck.current_location,
            undelivered_packages,
            packages,
            addresses,
            distances,
            get_distance,
        )

        next_package = packages.get_package(next_package_id)

        truck.route.append(next_package_id)  # Add the package to the truck's route
        truck.miles += distance  # Update mileage

        # calculate the travel time in minutes, truck speed is 18 miles per hour.
        travel_minutes = (distance / 18) * 60
        truck.current_time += travel_minutes  # Update current time

        truck.current_location = next_package.address  # Update current location

        # Update the package's delivery time
        next_package.delivery_time = truck.current_time
        next_package.departure_time = truck.departure_time

        undelivered_packages.remove(
            next_package_id
        )  # Remove the package from the undelivered list

    # Return truck to Hub if needed
    if to_hub:
        hub_distance = get_distance(truck.current_location, "HUB", addresses, distances)
        truck.miles += hub_distance

        travel_minutes = (hub_distance / 18) * 60
        truck.current_time += travel_minutes

        truck.current_location = "HUB"
