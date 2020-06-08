# Ask how many items and check it is not blank

# To Do
# Allow users to specify a custom error message
# Allow users to specify whether numbers are allowed
# Tell users not have numbers

# Not Blank Function goes here
def not_blank(question, error_msg, num_ok,):
    error_msg = error_msg


    valid = False
    while not valid:
        response = input(question)
        has_errors = ""

        if num_ok != "yes":
            # Look at each character in string and if it's a letter, complain
            for letter in response:
                if letter.isdigit() is True:
                    has_errors= "yes"
                    break

        if response == "":
            print(error_msg)
            continue
        elif has_errors != "":
            print(error_msg)
            continue
        else:
            return response
    valid = False
    while not valid:
     break


def num_check(type, question):

    if type == "int":
        error = "Please enter an integer  more than zero"
    else:
        error = "Please enter a number more than zero"

    valid = False
    while not valid:
        try:
            response = type(input(question))

            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)

# Main Routine goes Here
item_name = not_blank("what are you making",
                      "this can not be blank / contain letters",
                      "no"
                      )
how_many = num_check(int, "How many items are you making? ")


print("You are making {} {}" .format(how_many, item_name))
