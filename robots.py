valid_stasuses = ("vacuuming", "charging", "dumping")
valid_rooms = ("living room", "kitchen", "play room", "bathroom")

class Sensor:
    """
    Represents a sensor with a sensor type and what it detects.

    Attributes:
        sensor_type (str): What kind of sensor it is
        detects (str): What it detects/senses
    """
    def __init__(self, sensor_type, detects):
        """
        Initializes a sensor with a type and what it detects

        Args:
            sensor_type (str): What kind of sensor it is
            detects (str): What it detects/senses
        """
        
        self._sensor_type = sensor_type
        self._detects = detects

    def __str__(self):
        """Returns a formatted f-string of the sensor, with the type and what it detects"""
        
        return f"{self._sensor_type} (detects {self._detects})"

class Robot:
    """
    Represents a robot with a name, battery %, waste tank fill %, task status, and room its in.

    Attributes:
        name (str): Robot's name
        battery (int): Battery % full
        waste_tank (int): Waste tank % full
        status (str): Current task its doing
        room (str): Which room the robot is currently in
    """
    
    def __init__(self, name, battery, waste_tank, status, room):
        """
        Initializes a robot with a name, battery %, waste tank %, status, and room

        Args:
            name (str): Robot's name
            battery (int): Battery % full
            waste_tank (int): Waste tank % full
            status (str): Current task its doing
            room (str): Which room the robot is currently in
        """
        
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
        """Returns the robot's name"""
        
        return self._name

    def get_battery(self):
        """Returns the robot's battery %"""
        return self._battery

    def set_battery(self, value):
        """Sets a new value for the battery %"""
        if value < 0 or value > 100:
            raise ValueError("Battery cannot be negative or higher than 100.")
        self._battery = value

    def get_waste_tank(self):
        """Returns the robot's waste tank %"""
        return self._waste_tank

    def set_waste_tank(self, value):
        """Sets a new value for the waste tank %"""
        if value < 0 or value > 100:
            raise ValueError("Waste tank cannot be negative or higher than 100.")
        self._waste_tank = value

    def get_status(self):
        """Returns the robot's task/status"""
        return self._status
    
    def set_status(self, status):
        """Sets a new status for the robot's status"""
        if status not in valid_stasuses:
            raise ValueError(f"Status must be one of: {', '.join(valid_stasuses)}.")
        self._status = status

    def get_room(self):
        """Returns the robot's current room"""
        return self._room
 
    def set_room(self, room):
        """Sets a new room for the robot's location"""
        if room not in valid_rooms:
            raise ValueError(f"Room must be one of: {', '.join(valid_rooms)}.")
        self._room = room
 
    def get_sensors(self):
        """Returns the robot's sensors list"""
        return list(self._sensors)

    # Methods
    def get_activity(self):
        """Returns the robot's task/status"""
        return self._status

    def tick(self):
        """Sets a new value for the robot's battery and waste tank % as time passes"""
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
        """Returns an f-string description of the robot's task and current location"""
        return f"{self._name} is currently {self.get_activity()} in the {self._room}."

    def display(self):
        """Returns an f-string description of the robot's current status, room, battery %, and waste tank %"""
        return (f"{self._name}: {self.get_activity()} in {self._room}. "
                f"Battery: {self._battery}%, Waste Tank: {self._waste_tank}%")

    def __str__(self):
        """Returns the f-string description of status, room, battery, and waste tank when printed"""
        return self.display()


class MopRobot(Robot):
    """
    Represents a Mop Robot subclass of Robot with a name, battery, waste tank, status, and room, with a new sensor and alternate status to the base 'vacuuming'

    Attributes:
        name (str): Robot's name
        battery (int): Battery % full
        waste_tank (int): Waste tank % full
        status (str): Current task its doing
        room (str): Which room the robot is currently in
    """
    
    def __init__(self, name, battery, waste_tank, status, room):
        """
        Initializes a robot with a name, battery %, waste tank %, status, and room
        
        Args:
            name (str): Robot's name
            battery (int): Battery % full
            waste_tank (int): Waste tank % full
            status (str): Current task its doing
            room (str): Which room the robot is currently in
        """
        
        super().__init__(name, battery, waste_tank, status, room)
        self._sensors.append(Sensor("Moisture sensor", "wet floors"))

    def get_activity(self):
        """Returns mopping to override status from vacuuming"""
        if self._status == "vacuuming":
            return "mopping"
        return super().get_activity()

class PickUpRobot(Robot):
    """
    Represents a Pick-Up Robot subclass of Robot with a name, battery, waste tank, status, and room, with a new sensor and alternate status to the base 'vacuuming'

    Attributes:
        name (str): Robot's name
        battery (int): Battery % full
        waste_tank (int): Waste tank % full
        status (str): Current task its doing
        room (str): Which room the robot is currently in
    """
    
    def __init__(self, name, battery, waste_tank, status, room):
        """
        Initializes a robot with a name, battery %, waste tank %, status, and room
        
        Args:
            name (str): Robot's name
            battery (int): Battery % full
            waste_tank (int): Waste tank % full
            status (str): Current task its doing
            room (str): Which room the robot is currently in
        """
        
        super().__init__(name, battery, waste_tank, status, room)
        self._sensors.append(Sensor("Camera", "toys"))

    def get_activity(self):
        """Returns picking up to override status from vacuuming"""
        if self._status == "vacuuming":
            return "picking up"
        return super().get_activity()