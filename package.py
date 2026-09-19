#Package Object with all it's properties and delivery information
class Package:
    #We initialize the object's atributes when a new package is created
    def __init__(self, package_id, address, city, state, zip_code, deadline, weight, special_notes):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.weight = weight
        self.special_notes = special_notes

        #set up default values for delivery and departure time and status, every package starts at the hub before the Truck leaves.
        self.delivery_time = None
        self.departure_time = None        
        self.status = "At Hub"

    def __str__(self):#Override / string method to print out the package information in string format
        return( 
                f"Package ID: {self.package_id},"
                f"Address: {self.address}, "
                f"City: {self.city}, "
                f"State: {self.state}, "
                f"Zip Code: {self.zip_code}, "
                f"Deadline: {self.deadline}, "
                f"Weight: {self.weight}, "
                f"Special Notes: {self.special_notes}, "
                f"Delivery Time: {self.delivery_time}, "
                f"Departure Time: {self.departure_time}, "
                f"Status: {self.status}"
        )