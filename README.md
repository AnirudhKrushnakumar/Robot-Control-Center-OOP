# Robot Control Center OOP
<img width="2002" height="3332" alt="getters setters and methods robot cc oop" src="https://github.com/user-attachments/assets/f7e1ff44-00ef-4b74-b748-992a6b928e09" />

## An Object-Oriented Python project based around a theoretical Robot Control Center.

This project is a terminal based theoretical control center for a fleet of robot vacuums, featuring two subclass types.

To run this program, clone this repo and open in the code editor of your choice (VSCode is recommended). No setup is required, all you need is to have Python installed, and then run the main.py file in terminal.

The program will walk you through how to use it via the terminal UI menus.

## Class Use & Structure
The main classes used are Robot, MopRobot, and PickUpRobot, with Mop and PickUp being subclasses of Robot. The main attributes are name, battery, waste_tank, status, and room. The add robot option allows you to create a new instance of one of the classes of your choice. 

The robots.py file sets up the classes and all robot function related methods, while features.py creates all the functions needed for the general menu terminal UI. The main.py pieces them all together, and holds the main() function which the program runs within.

## Edge Cases
All functions, methods, and classes are built with precautions that raise errors for invalid inputs, and are nested within loops to allow for repeatability without hardcoding the loop amounts.
