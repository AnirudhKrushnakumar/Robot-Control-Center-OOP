class Robot:
    def __init__(self, model, dof, purpose, inventor):
        self._model = model
        self.set_dof(dof)
        self._purpose = purpose
        self._inventor = inventor
    
    def get_model(self):
        return self._model
    
    def get_dof(self):
        return self._dof

    def get_purpose(self):
        return self._purpose

    def get_inventor(self):
        return self._inventor

    def set_dof(self, freedoms):
        if freedoms <= 0:
            raise ValueError("Degrees of Freedom can't be 0 or negative.")
        else:
            self._dof = freedoms

def ask_for_dof():
    while True:
            try:
                dof = int(input("Degrees of Freedom: "))
                if dof <= 0:
                    print("Degrees of Freedom can't be less than or equal to 0.")
                else:
                    return dof
            except ValueError:
                print("Please enter a whole number.")

def document_robot(catalog):
    name = input("Robot name: ")
    model = input("Technical Model name: ")
    dof = ask_for_dof()
    purpose = input("Purpose: ")
    inventor = input("Inventor: ")
    
    robot = Robot(model, dof, purpose, inventor)
    catalog[name] = robot
    print(catalog)

def ask_for_search_query():
    while True:
        query = input("\nSearch using one of these formats:\n"
            "  <number> dof      (e.g. 28 dof)\n"
            "  name <text>       (e.g. name atlas)\n"
            "  model <text>      (e.g. model ur5)\n"
            "  purpose <text>    (e.g. purpose welding)\n"
            "  inventor <text>   (e.g. inventor mit)\n"
            "Search: ").strip().lower()

        words = query.split()

        if len(words) == 2 and words[1] == "dof" and words[0].isdigit():
            return "dof", int(words[0])
        elif len(words) >= 2 and words[0] in ("name", "model", "purpose", "inventor"):
            return words[0], " ".join(words[1:])
        else:
            print("Please enter a valid search in one of the formats shown.")

def find_matches(catalog, field, value):
    results = []
    for name, robots in catalog.items():
        if field == "dof":
            if robot.get_dof() == value:
                results.append((name, robot))
        elif field == "name":
            if value in name.lower():
                results.append((name, robot))
        elif field == "model":
            if value in robot.get_model().lower():
                results.append((name, robot))
        elif field == "purpose":
            if value in robot.get_purpose().lower():
                results.append((name, robot))
        elif field == "inventor":
            if value in robot.get_inventor().lower():
                results.append((name, robot))
    return results

def search_robots(catalog):
    pass

def main():
    catalog = {

    }

    while True:
        choice = input("Would you like to Document or search a robot? Choose 'done' if you'd like to exit. (d/s/done): ")
        if choice == "d":
            document_robot(catalog)
        elif choice == "s":
            search_robots(catalog)
        elif choice == "done":
            break
        else:
            print("Please choose a valid option.")

main()