#Implementation of the Truck object

class Truck:
    def __init__(self, truck_id, departure_time):
        self.truck_id = truck_id
        self.departure_time = departure_time
        self.package_ids = []  # package IDs assigned to the truck
        self.route = []  # the route the truck will take

        self.current_location = "HUB" #Starting location
        self.miles= 0.0  # mileage counter for the truck
        self.current_time = departure_time  # tracks current time for the truck, starts at departure time

    #function to add a package to the truck, if there is room for it.
    # Max load is 16 packages per truck.

    def add_package(self, package_id):
        if package_id in self.package_ids:
            return False # Package already on the truck, do not add it again.
        if len(self.package_ids) < 16:
            self.package_ids.append(package_id)
            return True
        
        return False # Truck is full
    