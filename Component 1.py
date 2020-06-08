# write code asking what the user is making and check it is not blank


# Not blank Function goes here:
def not_blank(question):
    error = "Your item name has numbers in it."

    valid = False
    while not valid:
        response = input(question)
        has_errors = "yes"

        # look at each character in string and if it's a number complain
        for letter in response:
            if letter.isdigit():
                has_errors = "yes"
                break

        if response == "":
            continue
        elif has_errors != "":
            print(error)
            continue
        else:
            return response


# Main Routine goes here
print = (" Item Name ")

print("You are selling {}".format(item_name))

