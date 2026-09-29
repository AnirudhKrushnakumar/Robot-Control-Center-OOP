from features import (add_robot, check_sensors, edit_robot, pass_time, set_task, view_fleet)
from robots import MopRobot, PickUpRobot, Robot

menu = """
Robot Vacuum Fleet:
1. View fleet   4. Edit robot
2. Set task     5. Check sensors
3. Add robot    6. Pass time
0. Exit
_________________________________"""

def build_starting_fleet():
    robots = [
        Robot("vac1", 72, 19, "vacuuming", "living room"),
        MopRobot("mop1", 83, 2, "charging", "kitchen"),
        PickUpRobot("pickup1", 37, 99, "vacuuming", "play room"),
    ]
    return {robot.get_name().lower(): robot for robot in robots}

def main():
    fleet = build_starting_fleet()
    actions = {"1": view_fleet, "2": set_task, "3": add_robot, "4": edit_robot, "5": check_sensors, "6": pass_time}

    while True:
        print(menu)
        try:
            choice = input("Choose a menu option: ").strip()
            if choice == "0":
                break
            if choice not in actions:
                raise ValueError(f"'{choice}' isn't a menu option. Choose 0-6.")
            actions[choice](fleet)
        except ValueError as error:
            print(f"Error: {error}")
        except KeyError as error:
            print(f"Error: no robot named {error}")
        except (KeyboardInterrupt, EOFError):
            print()
            break

    print("Shutting Down.")


if __name__ == "__main__":
    main()