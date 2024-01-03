

pizzaPrice = {"S": (7.99, 0.50), "M":(9.99, 0.75), "L":(11.99, 1), "XL":(13.99, 1.25)}
# the size along with the price of the pizza and extra toppings are all stored here so we can call the variable and its positions.
def generateReceipt(pizzaOrder):


    sub_Total = 0
    # total without tax.
    counter = 1
    # counter to know which pizza we are on.
    total = 0
    # total variable takes total including subtotal and tax.
    extraToppings = 0
    # holds the amount for extra toppings in each different sized pizza.
    pizPrice = 0
    # holds the price for each different pizza size.
    if len(pizzaOrder) == 0:
        print("You did not order anything")
        quit()
        # if the length of pizzaorder variable is 0 this would mean the user entered nothing therefore did not order.
    print("Your order:")
    # this prints above all the order details to indicate this is what the customer ordered.
    for pizza in pizzaOrder:
        # a forloop to run through each element in the list (size then the toppings).
        if pizza[0] == "S":
            pizPrice = 7.99
            sub_Total = sub_Total +  pizPrice
            extraToppings = 0.50
            # if the first item is "S" it will give the price of 7.99 and 0.50 for every extra topping.
        elif pizza[0] == "M":
            pizPrice = 9.99
            sub_Total = sub_Total + pizPrice
            extraToppings = 0.75
            # if the first item is "M" it will give the price of 9.99 and 0.75 for every extra topping.
        elif pizza[0] == "L":
            pizPrice = 11.99
            sub_Total = sub_Total + pizPrice
            extraToppings = 1.00
            # if the first item is "L" it will give the price of 11.99 and 1.00 for every extra topping.
        elif pizza[0] == "XL":
            pizPrice = 13.99
            sub_Total = sub_Total +pizPrice
            extraToppings = 1.25
            # if the first item is "XL" it will give the price of 13.99 and 1.25 for every extra topping.
        print("Pizza {}: {}                {}".format(counter, pizza[0], pizPrice))
        # this prints a statement giving the pizza number (counter is pizza number), size (pizza [position]) and the price of it (pizPrice).
        for toppings in pizza[1]:
            print("-", toppings)
            # this will go through each topping in the order list and print it each time.
        if (len(pizza[1]) > 3):
            # if the length of the list is greater than 3 (4 items/size and three toppings)this means there is more than three toppings meaning we need to charge them extra for toppings.
            for i in range(len(pizza[1])-3):
                # we know that since range(len) is already greater than 3 this means we must subtract 3 (4 items from the list) to see how many of them are extra toppings.
                sub_Total = sub_Total + extraToppings
                print("Extra Topping ({})         {}".format(pizza[0],("%.2f"%pizzaPrice.get(pizza[0])[1])))
        counter+=1
        # this counter adds one to so after every finished order the pizza number is updated.

    tax = (sub_Total *1.13) - sub_Total
    total = sub_Total + tax
    # these two variables calculate the tax and total of the orders.

    print("Tax:                       {}".format(("%.2f" %tax)))
    print("Total:                    {}".format(("%.2f" %total)))
    # calculates the tax and total to two decimals points.
