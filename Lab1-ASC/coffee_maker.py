"""
A command-line controlled coffee maker.
"""

import sys

"""
Implement the coffee maker's commands. Interact with the user via stdin and print to stdout.

Requirements:
    - use functions
    - use __main__ code block
    - access and modify dicts and/or lists
    - use at least once some string formatting (e.g. functions such as strip(), lower(),
    format()) and types of printing (e.g. "%s %s" % tuple(["a", "b"]) prints "a b"
    - BONUS: read the coffee recipes from a file, put the file-handling code in another module
    and import it (see the recipes/ folder)

There's a section in the lab with syntax and examples for each requirement.

Feel free to define more commands, other coffee types, more resources if you'd like and have time.
"""

"""
Tips:
*  Start by showing a message to the user to enter a command, remove our initial messages
*  Keep types of available coffees in a data structure such as a list or dict
e.g. a dict with coffee name as a key and another dict with resource mappings (resource:percent)
as value
"""


# My functions
# Closes the program
def exit_machine():
    return True


# Shows available coffees in the menu
def list_coffees():
    print("COFFEE MENU:")
    no_types = len(coffee_names)
    for i in range(no_types):
        print("%s" % coffee_names[i])
    return False


# Makes the coffee you ordered
def make_coffee():
    print("Which coffee would you like?")
    order = sys.stdin.readline().strip("\n")
    # Enough resources?
    can_make_coffee = True
    if order == 'cappuccino':
        selected_type = CAPPUCCINO
    else:
        if order == 'americano':
            selected_type = AMERICANO
        else:
            selected_type = ESPRESSO
    for ing in RESOURCES:
        if RESOURCES[ing] < selected_type[ing]:
            can_make_coffee = False
            print("Can't make coffee. Need more %s. Gonna go to the store" % ing)
            break
    if can_make_coffee:
        for ing in RESOURCES:
            RESOURCES[ing] -= selected_type[ing]
    print("Here is your order: %s" % order)
    return False


# Refills the selected ingredient back to 100%
def refill():
    print("Which resource to refill? Type 'all' for refilling everything")
    resource = sys.stdin.readline().strip("\n")
    if resource in RESOURCES:
        RESOURCES[resource] = 100
    else:
        if resource == ALL:
            for i in RESOURCES:
                RESOURCES[i] = 100
    return False


# Shows the amounts of ingredients
def resource_status():
    for ingredient, status in RESOURCES.items():
        print("%s: %d%%" % (ingredient, status))
    return False


# Shows my commands and what they do
def help_me():
    print('Available commands:\n' +
          '"exit" - stops the coffee maker\n' +
          '"list" - shows available coffees in the menu\n' +
          '"make" - makes the coffee you ordered\n' +
          '"refill" - refills the selected ingredient back to 100%\n' +
          '"status" - shows the available amounts of ingredients')
    return False


# Commands
EXIT = "exit"
LIST_COFFEES = "list"
MAKE_COFFEE = "make"  #!!! when making coffee you must first check that you have enough resources!
HELP = "help"
REFILL = "refill"
RESOURCE_STATUS = "status"
# Create a dict of commands-function
commands = {EXIT: exit_machine, LIST_COFFEES: list_coffees, MAKE_COFFEE: make_coffee,
            REFILL: refill, RESOURCE_STATUS: resource_status, HELP: help_me}

# Coffee examples
ESPRESSO_NAME = "espresso"
AMERICANO_NAME = "americano"
CAPPUCCINO_NAME = "cappuccino"
# Create a list of coffees names
coffee_names = [ESPRESSO_NAME, AMERICANO_NAME, CAPPUCCINO_NAME]

# Resources examples
WATER = "water"
COFFEE = "coffee"
MILK = "milk"
# Added all for the refill
ALL = "all"

# Coffee maker's resources - the values represent the fill percents
RESOURCES = {WATER: 100, COFFEE: 100, MILK: 100}
# Resources for every type of coffee
AMERICANO = {WATER: 10, COFFEE: 10, MILK: 0}
ESPRESSO = {WATER: 5, COFFEE: 10, MILK: 0}
CAPPUCCINO = {WATER: 5, COFFEE: 10, MILK: 10}
# Create a list of coffees resources
coffee_types = [ESPRESSO, AMERICANO, CAPPUCCINO]

"""
Example result/interactions:

I'm a smart coffee maker
Enter command:
list
americano, cappuccino, espresso
Enter command:
status
water: 100%
coffee: 100%
milk: 100%
Enter command:
make
Which coffee?
espresso
Here's your espresso!
Enter command:
refill
Which resource? Type 'all' for refilling everything
water
water: 100%
coffee: 90%
milk: 100%
Enter command:
exit
"""


def main():
    # Initial message
    print("I'm a kinda smart coffee maker")

    # While there was no exit we are gonna go and make coffee
    command_exit = False
    while command_exit is False:
        print("\nEnter command:")
        my_command = sys.stdin.readline().strip("\n")
        if my_command in commands:
            command_exit = commands[my_command]()
        else:
            print("Wrong command! Try again!")


if __name__ == "__main__":
    main()