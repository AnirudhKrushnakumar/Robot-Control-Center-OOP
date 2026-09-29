valid_stasuses = ("vacuuming", "charging", "dumping")
valid_rooms = ("living room", "kitchen", "play room", "bathroom")

class Sensor:
    def __init__(self, sensor_type, detects):
        self._sensor_type = sensor_type
        self._detects = detects

    def __str__(self):
        return f"{self._sensor_type} (detects {self._detects})"

class Robot:
    def __init__(self, name, battery, waste_tank, status, room):
        if not name.strip():
            raise ValueError("Name can't be empty.")
        self._name = name.strip()

        self.set_battery(battery)
        self.set_waste_tank(waste_tank)
        self.set_status(status)
        self.set_room(room)

        self._sensors = [Sensor("Bumper", "obstacles"), Sensor("Cliff Sensor", "drop-offs")]

    # Getters & Setters
    def get_name(self):
        return self._name

    def get_battery(self):
        return self._battery

    def set_battery(self, value):
        if value < 0 or value > 100:
            raise ValueError("Battery cannot be negative or higher than 100.")
        self._battery = value

    def get_waste_tank(self):
        return self._waste_tank

    def set_waste_tank(self, value):
        if value < 0 or value > 100:
            raise ValueError("Waste tank cannot be negative or higher than 100.")
        self._waste_tank = value

    def get_status(self):
        return self._status
    
    def set_status(self, status):
        if status not in valid_stasuses:
            raise ValueError(f"Status must be one of: {', '.join(valid_stasuses)}.")
        self._status = status

    def get_room(self):
        return self._room
 
    def set_room(self, room):
        if room not in valid_rooms:
            raise ValueError(f"Room must be one of: {', '.join(valid_rooms)}.")
        self._room = room
 
    def get_sensors(self):
        return list(self._sensors)

    # Methods
    def get_activity(self):
        return self._status

    def tick(self):
        if self._status == "vacuuming":
            self._battery = max(0, self._battery - 10)
            self._waste_tank = min(100, self._waste_tank + 10)
            if self._battery == 0:
                self._status = "charging"
            elif self._waste_tank == 100:
                self._status = "dumping"
        elif self._status == "charging":
            self._battery = min(100, self._battery + 25)
        elif self._status == "dumping":
            self._waste_tank = 0

    def perform_task(self):
        return f"{self._name} is currently {self.get_activity()} in the {self._room}."

    def display(self):
        return (f"{self._name}: {self.get_activity()} in {self._room}. "
                f"Battery: {self._battery}%, Waste Tank: {self._waste_tank}%")

    def __str__(self):
        return self.display()


class MopRobot(Robot):
    def __init__(self, name, battery, waste_tank, status, room):
        super().__init__(name, battery, waste_tank, status, room)
        self._sensors.append(Sensor("Moisture sensor", "wet floors"))

    def get_activity(self):
        if self._status == "vacuuming":
            return "mopping"
        return super().get_activity()

class PickUpRobot(Robot):
    def __init__(self, name, battery, waste_tank, status, room):
        super().__init__(name, battery, waste_tank, status, room)
        self._sensors.append(Sensor("Camera", "toys"))

    def get_activity(self):
        if self._status == "vacuuming":
            return "picking up"
        return super().get_activity()