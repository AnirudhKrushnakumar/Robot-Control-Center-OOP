class Robot:
    def __init__(self, model, dof, purpose, inventor):
        self._model = model
        self._dof = dof
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





def main():
    catalog = {

    }
    valid = False
    while not valid:
        choice = input("Would you like to Document or search a robot? Choose 'done' if you'd like to exit. (d/s/done): ")
        if choice == "d" or choice == "s" or choice == "done":
            valid = True
            if choice == "d":
                name = input("Robot name: ")
                model = input("Technical Model name: ")
                dof = int(input("Degrees of Freedom: "))
                purpose = input("Purpose: ")
                inventor = input("Inventor: ")

                name = Robot(model, dof, purpose, inventor)
                catalog[name] = name
                print(catalog)

            elif choice == "s":
                pass
            elif choice == "done":
                break
        else:
            print("Please choose a valid option.")

main()