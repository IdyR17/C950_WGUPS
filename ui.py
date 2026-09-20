# User Interface for WGUPS

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

#Function to convert user input into minutes since midnight

def convert_time_input(time_s):
    time, period = time_s.upper().split()

    hour, minute = time.split(":")
    hour = int(hour)
    minute = int(minute)

    if period == "PM" and hour !=12:
        hour+=12
    if period == "AM" and hour == 12:
        hour = 0

    return hour * 60 + minute

def show_package(package, req_time):
    status=package.get_current_status(req_time)

    print("\nPackage ID:", package.package_id)
    print("Address:", package.address)
    print("City:", package.city)
    print("State:", package.state)
    print("ZIP:", package.zip_code)
    print("Deadline:", package.deadline)
    print("Weight:", package.weight)
    print("Status at", format_time(req_time) + ":", status)

    if status == "Delivered":
        print("Delivery Time:", format_time(package.delivery_time))

def main_menu(packages, total_packages, total_miles):
    while True:
        print("\nWelcome to the WGUPS Delivery System \n Please choose an option by using the keyboard (1-4)")
        print("1. Find a package")
        print("2. View all packages")
        print("3. Display total miles")
        print("4. Exit")

        choice = input("Choose an option(1-4): ")

        if choice == "1":
            package_id = int(input("Enter package ID: "))
            time_input = input("Enter time in HH:MM AM/PM format (eg: 9:15 AM): ")
            req_time = convert_time_input(time_input)
            package = packages.get_package(package_id)

            show_package(package, req_time)

        elif choice == "2":
            time_input = input("Enter time (example: 9:15 AM): ")
            req_time = convert_time_input(time_input)

            for package_id in range(1, total_packages + 1):
                package = packages.get_package(package_id)
                show_package(package, req_time)

        elif choice == "3":
            print("\nTotal Miles: ", round(total_miles, 2))

        elif choice == "4":
            print("Thank you for using WGUPS. Goodbye!")
            break

        else:
            print("Input not valid. Please select 1, 2, 3, or 4 to continue")