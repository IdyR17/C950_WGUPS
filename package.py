# Package Object that stores all package properties and delivery information
class Package:
    # Initialize the object's atributes when a new package is created
    def __init__(
        self,
        package_id,
        address,
        city,
        state,
        zip_code,
        deadline,
        weight,
        special_notes,
    ):
        self.package_id = package_id
        self.previous_address = address  # for address change. Copy of original address
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.previous_zip = zip_code  # for address change. copy of original zip
        self.deadline = deadline
        self.weight = weight
        self.special_notes = special_notes

        # set up default values for delivery and departure time.
        # These will be set later when routes are calculated
        self.delivery_time = None
        self.departure_time = None

    def __str__(
        self,
    ):  # string representation of the package object to print out the package information in string format
        return (
            f"Package ID: {self.package_id},"
            f"Address: {self.previous_address}, "
            f"Address: {self.address}, "
            f"City: {self.city}, "
            f"State: {self.state}, "
            f"Zip Code: {self.zip_code}, "
            f"Zip Code: {self.previous_zip}, "
            f"Deadline: {self.deadline}, "
            f"Weight: {self.weight}, "
            f"Special Notes: {self.special_notes}, "
            f"Delivery Time: {self.delivery_time}, "
            f"Departure Time: {self.departure_time}, "
        )

    def get_current_status(
        self, status_time
    ):  # Function to get the status of the package
        if "Delayed on flight" in self.special_notes and status_time < 545:
            # if the package is delayed on flight and is not yet at Hub
            return "Delayed"
        if self.departure_time is None or status_time < self.departure_time:
            # If truck hasn't left, then package is still at Hub
            return "At Hub"
        if self.delivery_time is not None and status_time >= self.delivery_time:
            # if the time requested is at or after delivery, package has been delivered
            return "Delivered"
        else:
            # Otherwise, the package has left the Hub and is on its way to the destination
            return "En Route"
