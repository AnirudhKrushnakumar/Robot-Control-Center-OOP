class Robot:
    def __init__(self, name, battery, waste_tank, status):
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