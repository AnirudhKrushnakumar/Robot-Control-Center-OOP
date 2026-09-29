class Robot:
    def __init__(self, name, battery, waste_tank, status, room):
        self._name = name
        self._battery = battery
        self._waste_tank = waste_tank
        self._status = status

    def get_name(self):
        return self._name

    def get_battery(self):
        return self._battery

    def set_battery(self, value):
        if value < 0 or value > 100:
            raise ValueError("Battery cannot be negative or higher than 100.")
        else:
            self._battery = value

    def get_waste_tank(self):
            return self._waste_tank
    
    def set_waste_tank(self, value):
            if value < 0 or value > 100:
                raise ValueError("Waste tank cannot be negative or higher than 100.")
            else:
                self._waste_tank = value

    def get_status(self):
        return self._status

    def perform_task(self):
        return f"Robot is currently {self._status}"


"""
Planned ideas:
main menu options = view fleet, set task, add robot, edit robot, check sensors
view fleet gives an overview of the fleet (battery, names, status, waste tank, room)
set task lets you set the status and what room of a specified robot
add robot lets you add a new robot instance
edit robot lets you modify and existing robot instance
check sensors gives an overview of each robot's sensors

statuses include vacuming, charging, dumping
sub types include mop robot and pick up robot
mop robot overrides vacuming to mopping, and pick up overrides vacuming to picking

rooms include living room, kitchen, play room, bathroom

battery degrades over time, reducing charge. can be filled by setting status/task to charging

waste tank fills up over time, setting status/task to dumping empties it
"""
vac1 = Robot("vac1", 72, 19, "Cleaning")
