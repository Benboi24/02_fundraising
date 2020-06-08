
# Defining 'Variable_subtotal' variable:

variable_subtotal = 0

# Setting 'fixed_subtotal' variable to zero:

fixed_subtotal = 0

# Lists:

fixed_item_cost = []
fixed_costs = []

variable_item_cost = []
variable_costs = []


# Variable Costs



# Ask user for their required number of units

units_required = input("What is your desired amount of number of items? ")

print("Please enter the variable costs associated with your product below:")

# Get inputs and add to the mini list

variable_item = ""

while variable_item.lower() != "xxx":

    variable_item_cost = []

    variable_item = input("What is the name of the variable cost? ")

    # If the user enter the exit code, break the loop

    if variable_item.lower() == "xxx":

        break

    # (Eventually , replace this with a number checking function)

    variable_cost = float(input(" What is the variable cost in NZD? "))

    # add both the item name and cost to the mini list

    variable_item_cost.append(variable_item)
    variable_item_cost.append(variable_cost)

    # Add the mini lists to the master list

    variable_cost.float(variable_item_cost)

# Add the costs of the items from the list into a variable:

for item in variable_costs:

    variable_subtotal += item[1]

# Calculates Subtotal:

calculated_variable_subtotal = variable_subtotal * units_required

# Prints the subtotal

print("The subtotal of the variable costs is ${:.2f}".format(calculated_variable_subtotal))
print()

