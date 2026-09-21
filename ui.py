# User Interface for WGUPS
# Handles the display and lookup of packages by the user, as well as status checks at a requested time, and total mileage
# Task 2-B Look-Up Functions - see show_package() and HashTable.get_package(), this UI displays the result.


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


# Function to convert user input into minutes since midnight


def convert_time_input(time_s):
    time, period = time_s.upper().split()

    hour, minute = time.split(":")
    hour = int(hour)
    minute = int(minute)

    if period == "PM" and hour != 12:
        hour += 12
    if period == "AM" and hour == 12:
        hour = 0

    return hour * 60 + minute


# Displays a package to display in the UI as requested by the user, at a requested time.
def show_package(package, req_time):
    status = package.get_current_status(req_time)

    # For Address change on package 9
    if package.package_id == 9 and req_time < 620:
        display_address = package.previous_address
        display_zip = package.previous_zip
    else:
        display_address = package.address
        display_zip = package.zip_code
    print("\n" + "=" * 107)
    print("\nPackage ID:", package.package_id)
    print("\n" + "=" * 107)
    print("Address:", display_address)
    print("City:", package.city)
    print("State:", package.state)
    print("ZIP:", display_zip)
    print("Deadline:", package.deadline)
    print("Weight:", package.weight)
    print("Status at", format_time(req_time) + ":", status)

    if status == "Delivered":
        print("Delivery Time:", format_time(package.delivery_time))


# Display a list of all the packages and status at the requested time, this includes truck assignment, and delivery time
def show_all_packages(packages, total_packages, req_time, truck1, truck2, truck3):

    print("\n" + "=" * 107)
    print(f"WGUPS PACKAGE STATUS AT {format_time(req_time)}")
    print("=" * 107)

    print(
        f"{'ID':<5}"
        f"{'TRUCK':<8}"
        f"{'ADDRESS':<40}"
        f"{'ZIP':<13}"
        f"{'DEADLINE':<13}"
        f"{'STATUS':<13}"
        f"{'DELIVERY TIME':<15}"
    )

    print("-" * 107)

    for package_id in range(1, total_packages + 1):
        package = packages.get_package(package_id)
        status = package.get_current_status(req_time)

        # Show package 9's original address before 10:20 AM
        if package.package_id == 9 and req_time < 620:
            display_address = package.previous_address
            display_zip = package.previous_zip
        else:
            display_address = package.address
            display_zip = package.zip_code

        if status == "Delivered":
            delivery_time = format_time(package.delivery_time)
        else:
            delivery_time = "-"

        if package_id in truck1.package_ids:
            truck_number = 1
        elif package_id in truck2.package_ids:
            truck_number = 2
        else:
            truck_number = 3

        print(
            f"{package.package_id:<5}"
            f"{truck_number:<8}"
            f"{display_address:<40}"
            f"{display_zip:<13}"
            f"{package.deadline:<13}"
            f"{status:<13}"
            f"{delivery_time:<15}"
        )

    print("=" * 107)


# Main user interface loop. The user can look up one package, view all the packages at a given time, view total miles, or exit the program
def main_menu(packages, total_packages, truck1, truck2, truck3):
    while True:
        print("\n" + "=" * 50)
        print("\n   Welcome to the WGUPS Delivery System")
        print("\n" + "=" * 50)
        print(" Please choose an option by using the keyboard (1-4)")
        print("" + "-" * 50)
        print("1. Find a package")
        print("2. View all packages")
        print("3. Display total miles")
        print("4. Exit")
        print("\n" + "=" * 50)

        choice = input("Choose an option(1-4): ")

        if choice == "1":
            package_id = int(input("Enter package ID: "))
            time_input = input("Enter time in HH:MM AM/PM format (eg: 9:15 AM): ")
            req_time = convert_time_input(time_input)
            package = packages.get_package(
                package_id
            )  # retrieves the Package object from the custom hash table

            show_package(package, req_time)
            input("\nPress Enter to continue...")

        elif choice == "2":
            time_input = input("Enter time (example: 9:15 AM): ")
            req_time = convert_time_input(time_input)

            show_all_packages(
                packages, total_packages, req_time, truck1, truck2, truck3
            )
            input("\nPress Enter to continue...")

        elif choice == "3":
            total_miles = truck1.miles + truck2.miles + truck3.miles

            print("\n" + "=" * 40)
            print("            TRUCK MILEAGE")
            print("=" * 40)
            print(f"Truck 1: {truck1.miles:.1f} miles")
            print(f"Truck 2: {truck2.miles:.1f} miles")
            print(f"Truck 3: {truck3.miles:.1f} miles")
            print("-" * 40)
            print(f"TOTAL:   {total_miles:.1f} miles")
            print("=" * 40)

            input("\nPress Enter to continue...")

        elif choice == "4":
            print("Thank you for using WGUPS. Goodbye!")
            break

        else:
            print("Input not valid. Please select 1, 2, 3, or 4 to continue")
