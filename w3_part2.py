### Part 2: Alarm plus 24 hour clock

# Loop until the user enters a valid number
while True:
    try:
        # prompt user for time in hours
        time_input = input("Please enter the current time in hours: ")

        # first check if the input is a number
        if not time_input.isdigit():
            raise ValueError("Please enter an integer.")
        
        # input defaults to string. cast to int and check it
        time = int(time_input)

        # next make sure time is valid, between 0 and 23
        if time < 0 or time > 23:
            raise ValueError("Time must be between 0 and 23, inclusive.")

        break
    
    # since we we can raise a ValueError above, we define it here
    except ValueError as e:
        # note that 'e' is the error string above
        print(e)
        # we just want to keep prompting if the input is incorrect
        continue

while True:
    try:
        # print user for number of hours to wait
        wait_input = input("Please enter the number of hours to wait: ")

        # check that wait is also an integer
        if not wait_input.isdigit():
            raise ValueError("Please enter an integer.")

        wait = int(wait_input)

        # check that the wait time is a positive number
        if wait < 0:
            raise ValueError("Wait time must be a positive integer.")

        # add them together
        sum = time + wait

        # since there are 24 hours in a day, we want the modulus of 24
        alarm = sum % 24

        # print
        print(f"The alarm will go off at {alarm:d}.")

        break

    # since we we can raise a ValueError above, we define it here
    except ValueError as e:
        # note that 'e' is the error string above
        print(e)
        # we just want to keep prompting if the input is incorrect
        continue