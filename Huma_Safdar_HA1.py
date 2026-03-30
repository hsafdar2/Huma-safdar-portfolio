#-------------------------------------------------------------------------------
# HA1
# Student Name: Huma Safdar
# Submission Date: 02/15/2026
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines as set forth by the
# instructor and the class syllabus.
#-------------------------------------------------------------------------------
# References: 
#-------------------------------------------------------------------------------
# Notes to grader: 
#-------------------------------------------------------------------------------

total = 0
tax_rate = 0.043

print("*********** Welcome to Salad Bar ***********")

while True:

    print("\n1. Order Salad")
    print("2. Checkout")
    print("3. Quit")

    option = int(input("Select your option (1-3): "))

    # Option 1 - Order Salad
    if option == 1:

        print("\nSalad Menu")
        print("1. Vegetarian - $10.99")
        print("2. Seafood - $16.99")
        print("3. Protein - $14.99")

        salad_choice = int(input("Enter your salad selection (1-3): "))

        if salad_choice == 1:
            total += 10.99
            print("One veggie salad added to your cart.")

        elif salad_choice == 2:
            total += 16.99
            print("One seafood salad added to your cart.")

        elif salad_choice == 3:
            total += 14.99
            print("One protein-based salad added to your cart.")

        else:
            print("Invalid option. Returning to main menu.")

    # Option 2 - Checkout
    elif option == 2:

        print("Checking out...")
        print("Your total before tax:", total)

        tax = total * tax_rate
        print("Total tax (4.3%):", tax)

        final_total = total + tax
        print("Your total after tax:", final_total)
        print("**** Thanks for using Salad Bar ***********")

    # Option 3 - Quit
    elif option == 3:
        print("Exiting the program.")
        break

    # Invalid main menu option
    else:
        print("Invalid option. Returning to main menu.")
