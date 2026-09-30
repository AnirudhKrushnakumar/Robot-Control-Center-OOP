from robots import MopRobot, PickUpRobot, Robot, valid_rooms, valid_stasuses

def ask_number(prompt, low = 0, high = 100):
    """Prints a question for an input number range, and accounts for bounds"""
    while True:
        try:
            value = int(input(prompt))
            if low <= value <= high:
                return value
            print(f"Please enter a number from {low} to {high}.")
        except ValueError:
            print("Please enter a whole number.")

def choose(title, options):
    """Sets up and prints a user input UI for a list of options"""
    print(f"{title}:")
    for number, option in enumerate(options, start = 1):
        print(f"{number}. {option}")
    while True:
        pick = input(f"Choose (1-{len(options)}): ").strip()
        if pick.isdigit() and 1 <= int(pick) <= len(options):
            return options[int(pick) - 1]
        print("Please choose a number form the list.")

def view_fleet(fleet):
    """Prints fleet overview"""
    print("Fleet:")
    for robot in fleet.values():
        print(f"{robot.display()}")

def pick_robot(fleet):
    """Returns a user input to select a robot for inspection/modification"""
    view_fleet(fleet)
    return fleet[input("Robot name: ").strip().lower()]

def set_task(fleet):
    """Prints an updated f-string overview for a modified robot's status and room"""
    robot = pick_robot(fleet)
    robot.set_status(choose("Task", valid_stasuses))
    robot.set_room(choose("Room", valid_rooms))
    print(f"{robot.perform_task()}")

def add_robot(fleet):
    """Sets up and prints user inputs + overview for a robot being added to the fleet by the user"""
    name = input("Robot name: ").strip()
    if not name:
        raise ValueError("Name can't be empty.")
    if name.lower() in fleet:
        raise ValueError(f"A robot named '{name}' already exists.")

    kinds = {"Vacuum": Robot, "Mop": MopRobot, "Pick-up": PickUpRobot}
    kind = choose("Robot type", list(kinds))
    battery = ask_number("Battery % (0-100): ")
    waste_tank = ask_number("Waste Tank % (0-100): ")
    status = choose("Starting task", valid_stasuses)
    room = choose("Room", valid_rooms)

    robot = kinds[kind](name, battery, waste_tank, status, room)
    fleet[name.lower()] = robot
    print(f"Added: {robot}")

def edit_robot(fleet):
    """Sets up and prints user inputs for editing attributes of a robot instance"""
    robot = pick_robot(fleet)
    while True:
        print(f"{robot.display()}")
        print("1. Battery, 2. Waste Tank, 3. Room, 4. Done")
        choice = input("Edit which (1-4)?").strip()
        if choice == "1":
            robot.set_battery(ask_number("New battery % (0-100): "))
        elif choice == "2":
            robot.set_waste_tank(ask_number("New waste tank % (0-100): "))
        elif choice == "3":
            robot.set_room(choose("Room", valid_rooms))
        elif choice == "4":
            return
        else:
            print("Please choose 1-4.")

def check_sensors(fleet):
    """Prints an f-string overview for a robot's sensors"""
    for robot in fleet.values():
        print(f"{robot.get_name()}:")
        for sensor in robot.get_sensors():
            print(f"- {sensor}")

def pass_time(fleet):
    """Sets up and prints user input for time passing"""
    steps = ask_number("How many time steps (1-20): ", 1, 20)
    for _ in range(steps):
        for robot in fleet.values():
            robot.tick()
    view_fleet(fleet)