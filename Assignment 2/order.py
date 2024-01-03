import pizzaReceipt
# List of toppings that the user can select from.
LIST_TOPPINGS = ("ONION", "TOMATO", "GREEN PEPPER", "MUSHROOM", "OLIVE", "SPINACH", "BROCCOLI", "PINEAPPLE", "HOT PEPPER", "PEPPERONI", "HAM", "BACON", "GROUND BEEF", "CHICKEN", "SAUSAGE")
def pizza_world():
    list2 = []
    # list2 will contain toppings the user selects.
    finalToppings = []
    # final toppings contains the list of pizza size and toppings all together.
    PIZZA_SIZES = ["S", "M", "L", "XL"]
    # user selects from these sizes.
    welcome = (input("Do you want to order pizza: "))
    # the first prompt the user will get.
    while welcome.lower() != ("no") and welcome.lower() != ("q"):
        pizzas_input = input("Choose a size: S, M, L, or XL: ")
        # based on what the user enters they will either have the program end or continue to choose their pizza size.
        if pizzas_input.upper() in PIZZA_SIZES:
            topping = input("Type in one of our toppings to add it to your pizza. To see the list of toppings, enter \"LIST\". When you are done adding toppings, enter \"X\"\n").upper()
            list2 = []
            # list2 is where the customer toppings are put while it runs through the while loop.
            while topping.upper() != "X":
                # if the user enters X it exits the while loop.
                if topping.upper() in LIST_TOPPINGS:
                    list2.append(topping.upper())
                    print(f"Added {topping.upper()} to your pizza")
                    # if user enters a topping in the list, it will be valid and added to the list.
                elif topping.upper() == "LIST":
                    print(LIST_TOPPINGS)
                    # if user enters "LIST" then the list of avalaible toppings will appear
                elif topping.upper() not in LIST_TOPPINGS:
                    print("Invalid Topping")
                    # any invalid entry will tell the user.
                topping = input("Type in one of our toppings to add it to your pizza. To see the list of toppings, enter \"LIST\". When you are done adding toppings, enter \"X\"\n").upper()


            welcome = input("Do you want to continue ordering? ")
            # after the user is done ordering and types "X" it returns to the new welcome variable here to ask the customer if they want to continue ordering.

            pizzaOrder1 = (pizzas_input.upper(), list2)
            # makes a tuple of the pizza size and its toppings
            finalToppings.append(pizzaOrder1)
            # makes a new list of the 'pizzaOrder1' tuple.
    return finalToppings
    # returns the finaToppings list every time the function gets run through.
pizzaReceipt.generateReceipt(pizza_world())

