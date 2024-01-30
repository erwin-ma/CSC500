### Part 1: Calculate the total amount of a meal purchased at a restaurant.

# we want the food_charge to be $0 or greater, and must also be a number.
# so, we build a loop with try-except to check for errors
while True:
    try:
        # prompt the user for charge of food
        food_charge = float(input("Please enter the charge for food: "))

        # here's the check for a negative number:
        if food_charge < 0:
            # note that raising a ValueError means it 'skips' down to the 
            # except clause below, and then bounces back up to try
            raise ValueError("Food charge cannot be negative.")

        # calculate tip
        tip = food_charge * 0.18

        # calculate sales tax
        sales_tax = food_charge * 0.07

        # calculate total
        total = food_charge + tip + sales_tax

        print(f"Food charge is: ${food_charge:.2f}")
        print(f"Tip is: ${tip:.2f}")
        print(f"Sales tax is: ${sales_tax:.2f}")
        print(f"Total is: ${total:.2f}")

        # we have to break out of the while loop once we're done
        break

    # since we we can raise a ValueError above, we define it here
    except ValueError as e:
        # note that 'e' is actually defined as the error string above
        print(e)
        # we just want to keep prompting if the input is incorrect
        continue
