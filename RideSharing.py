ride_req = []
driver_info = {}
unique_loc = set()
matched_rides = []

def login():
    password = "kashish@123"
    userpass = input("Enter the password:")
    if userpass == password:
        print("Access granted")
        return True
    else:
        print("Access denied")
        return False
# adding all information

def add_rider():
    print("\n----Add rider request----")
    rider_name = input("Enter rider name:")
    start_location = input("Enter start location:")
    end_location = input("Enter end location:")
    preferred_time = input("Enter preferred time:")
    number_of_passengers = int(input("Enter number of passengers:"))
    request = {"rider_name":rider_name,
               "start":start_location,
               "end":end_location,
               "preferred_time":preferred_time,
               "passengers":number_of_passengers}
    ride_req.append(request)
    unique_loc.add(start_location)
    unique_loc.add(end_location)

def add_driver():
    print("\n----Add driver details----")
    driver_id = input("Enter driver ID: ")
    name = input("Enter driver name: ")
    cap = int(input("Enter vehicle capacity: "))
    loc = input("Enter current location: ")
    routes = input("Enter available routes (comma separated): ").split(",")
    available_routes = []
    for route in routes:
        available_routes.append(route.strip())

    driver_info[driver_id] = {
        "driver_name": name,
        "vehicle_capacity": cap,
        "current_location": loc,
        "available_routes":available_routes}
    unique_loc.add(loc)

# modifying

def mod_rider_req():
    name = input("Enter the rider information you want to modify:")
    for rider in ride_req:
        if rider["rider_name"]==name:
            rider["start"] = input("Enter new start location:")
            rider["end"] = input("Enter new end location:")
            rider["preferred_time"] = input("Enter new preferred time:")
            rider["passengers"] = int(input("Enter new number of passengers:"))
            print("Ride request updated")
    print("Rider not found")

def mod_driver_info():
    driver_id = input("Enter driver ID you want to modify:")
    if driver_id in driver_info:
        driver_info[driver_id]["driver_name"] = input("Enter the name of new driver:")
        driver_info[driver_id]["vehicle_capacity"] = int(input("Enter the new capacity:"))
        driver_info[driver_id]["current_location"] = input("Enter new  current location:")
        routes = input("Enter new available routes (separated by commas)").split(",")
        available_routes = []
        for route in routes:
            available_routes.append(route.strip())
        driver_info[driver_id]["available_routes"] = available_routes
        print("Driver info updated")
    else:
        print("Driver not found")

# deleting

def del_rider_req():
    name = input("Enter the rider name you want to delete:")
    for request in ride_req:
        if request["rider_name"] == name:
            ride_req.remove(request)
            print("Ride request deleted")
            return
    print("Rider not found")

def del_driver():
    driver_id = input("Enter driver ID to delete:")
    if driver_id in driver_info:
        del driver_info[driver_id]
        print("Driver deleted")
    else:
        print("Driver not found")

# search

def search():
    print("Search by:")
    print("1. Location")
    print("2. Driver Availability")
    choice = input("Enter choice: ")

    if choice == "1":
        location = input("Enter location to search: ")
        print("\nRides starting or ending at", location)
        for req in ride_req:
            if req["start_location"] == location or req["end_location"] == location:
                print(req)

    elif choice == "2":
        print("\nAvailable drivers:")
        for dri_id, d in driver_info.items():
            print(f"{dri_id} - {d['driver_name']} at {d['current_location']}")

# matching

def match_routes():
    for ride in ride_req:
        for d_id, d in driver_info.items():
            if (ride["start"] in d["available_routes"] and
                    ride["end"] in d["available_routes"] and
                    ride["passengers"] <= d["vehicle_capacity"]):
                route_segment = (ride["start"], ride["end"])
                matched_rides.append((ride["rider_name"], d["driver_name"], route_segment))
                print(f"Matched {ride['rider_name']} with {d['driver_name']} on route {route_segment}")

# reports

def show_reports():
    print("\n--- Reports ---")
    print(f"Pending Ride Requests: {len(ride_req)}")
    print(f"Available Drivers: {len(driver_info)}")
    print("\nMatched Rides:")
    for matched in matched_rides:
        print(matched)

def menu():
    print("----Ride Sharing Pool Planner----")
    print("1.Add Ride Request\n"
          "2.Add Driver Info\n"
          "3.Modify Ride Request\n"
          "4.Modify Driver Info\n"
          "5.Delete Ride Request\n"
          "6.Delete Driver info\n"
          "7.Show reports\n"
          "8.Search Location or Driver\n"
          "9.Match the Routes\n"
          "0.Exit")

if login():
    while True:
        menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_rider()
        elif choice == "2":
            add_driver()
        elif choice == "3":
            mod_rider_req()
        elif choice == "4":
            mod_driver_info()
        elif choice == "5":
            del_rider_req()
        elif choice == "6":
            del_driver()
        elif choice == "7":
            show_reports()
        elif choice == "8":
            search()
        elif choice == "9":
            match_routes()
        elif choice == "0":
            print("Exiting program")
            break
        else:
            print("Invalid choice, please try again.")
