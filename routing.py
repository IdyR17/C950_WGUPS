#This is the routing algorithm for WGUPS.
#It is based on the Nearest Neighbor Algorithm - a greedy algorithm that finds the closest unvisited location.

def get_next_package(current_location, package_ids, packages, addresses, distances, get_distance):
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

    # Nearest Neighbor
    for package_id in packages_to_check:
        package = packages.get_package(package_id)

        distance = get_distance(
            current_location,
            package.address,
            addresses,
            distances
        )

        if distance < closest_distance:
            closest_distance = distance
            closest_package_id = package_id

    return closest_package_id, closest_distance

# To make the route, we also have to take the constraints into consideration. The following logic will be implemented on top of Nearest Neighbor:
# Truck 1: early deadline / group that needs to be delivered together
# Truck 2: Truck 2 ONLY packages. Package delayed with early delivery
# Truck 3: Package 9 (waiting for correct address), packages delayed with EOD deliveries, other packages to choose, as needed

def make_route(truck, packages, addresses, distances, get_distance):
    #list that will keep track of packages that havent been delivered yet
    undelivered_packages = truck.package_ids.copy()

    while undelivered_packages:
        next_package_id, distance = get_next_package(truck.current_location, undelivered_packages, packages, addresses, distances, get_distance)

        next_package = packages.get_package(next_package_id)

        truck.route.append(next_package_id)  # Add the package to the truck's route
        truck.miles += distance  # Update mileage

        #calculate the travel time in minutes, truck speed is 18 miles per hour.
        travel_minutes = (distance / 18) * 60
        truck.current_time +=travel_minutes  # Update current time

        truck.current_location = next_package.address  # Update current location

        #Update the package's delivery time
        next_package.delivery_time = truck.current_time
        next_package.departure_time = truck.departure_time

        undelivered_packages.remove(next_package_id)  # Remove the package from the undelivered list

    #Return truck to Hub
    hub_distance=get_distance(truck.current_location, "HUB", addresses, distances)
    truck.miles += hub_distance

    travel_minutes = (hub_distance /18) *60
    truck.current_time += travel_minutes

    truck.current_location= "HUB"