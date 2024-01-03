import pizzaReceipt

list_Toppings = ("ONION", "TOMATO", "GREEN PEPPER", "MUSHROOM", "OLIVE", "SPINACH", "BROCCOLI", "PINEAPPLE", "HOT PEPPER", "PEPPERONI", "HAM", "BACON", "GROUND BEEF", "CHICKEN", "SAUSAGE")
def pizza_world():
    list2 = []
    finalToppings = []
    pizza_sizes = ["S", "M", "L", "XL"]
    welcome = (input("Do you want to order pizza: "))
    while welcome.lower() != ("no") and welcome.lower() != ("q"):
        pizzas_input = input("Choose a size: S, M, L, or XL: ")

        if pizzas_input.upper() in pizza_sizes:
            topping = input("Type in one of our toppings to add it to your pizza. To see the list of toppings, enter \"LIST\". When you are done adding toppings, enter \"X\"\n").upper()
            list2 = []
            while topping.upper() != "X":
                if topping.upper() in list_Toppings:
                    list2.append(topping.upper())
                    print(f"Added {topping.upper()} to your pizza")
                elif topping.upper() == "LIST":
                    print(list_Toppings)
                elif topping.upper() not in list_Toppings:
                    print("Invalid Topping")
                topping = input("Type in one of our toppings to add it to your pizza. To see the list of toppings, enter \"LIST\". When you are done adding toppings, enter \"X\"\n").upper()

        pizzaOrder1 = (pizzas_input.upper(), list2)
        finalToppings.append(pizzaOrder1)
        welcome = input("Do you want to continue ordering? ")
    return finalToppings

pizzaReceipt.generateReceipt(pizza_world())

