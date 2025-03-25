import math

while True:
    try:
        number = float(input("Enter a number: "))

        if number < 0:
            print("Please enter a positive number")
        elif number == 0:
            print("Please enter a non-zero number")
        else:
            print(f"The square root of {number} is {math.sqrt(number)}")

        while True:
            repeat = input("Do you want to try again? (y/n): ").strip().lower()
            if repeat == "n":
                exit()
            elif repeat == "y":
                break
            else:
                print("Invalid input. Please enter 'y' or 'n'.")
    
    except ValueError:
        print("Please enter a number")