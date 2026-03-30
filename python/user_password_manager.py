#-------------------------------------------------------------------------------
# HA2
# Student Name: Huma Safdar
# Submission Date: 03/18/2026
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines as set forth by the
# instructor and the class syllabus.
#-------------------------------------------------------------------------------
# Pseudocode: Write your pseudocode below following a # sign
# Step 1: 
#-------------------------------------------------------------------------------
# References: 
#-------------------------------------------------------------------------------
# Notes to grader: 
#-------------------------------------------------------------------------------

upper_case_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lower_case_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
database = ["Jake:A-B-a-b-c-c","Mary:B-z-z-r-R-b","Bob:X-y-a-Z-i-d","Janet:c-d-N-m-h-H","Henry:G-i-K-o-o-e"]

# check password
def check_password(password):
    parts = password.split('-')

    upper = 0
    lower = 0

    # check if 6 parts
    if len(parts) != 6:
        return False, upper, lower

    for x in parts:
        # check single letter
        if len(x) != 1:
            return False, upper, lower

        if x in upper_case_letters:
            upper = upper + 1
        elif x in lower_case_letters:
            lower = lower + 1
        else:
            return False, upper, lower

    # final check
    if upper == 2 and lower == 4:
        return True, upper, lower

    return False, upper, lower


# main
option = 0

while option != 4:

    print("\n--- Menu ---")
    print("1 show")
    print("2 add")
    print("3 update")
    print("4 exit")

    option = int(input("Enter: "))


    # show
    if option == 1:
        print("Showing data")
        for item in database:
            parts = item.split(':')
            print("User:", parts[0], "Pass:", parts[1])


    # add
    elif option == 2:
        print("Add user")
        username = input("username: ")

        exists = False

        for item in database:
            if username == item.split(':')[0]:
                exists = True

        if exists:
            print("already exists")
        else:
            password = input("password: ")

            valid, up, low = check_password(password)

            if valid:
                database.append(username + ":" + password)
                print("added")
            else:
                print("wrong password")
                print("upper:", up, "lower:", low)


    # update
    elif option == 3:
        print("update user")
        username = input("username: ")

        found = False

        for i in range(len(database)):
            parts = database[i].split(':')

            if parts[0] == username:
                found = True

                newp = input("new pass: ")

                valid, up, low = check_password(newp)

                if valid:
                    database[i] = username + ":" + newp
                    print("done")
                else:
                    print("wrong")
                    print("upper:", up, "lower:", low)

        if found == False:
            print("not found")


    # exit
    elif option == 4:
        print("bye")


    # wrong
    else:
        print("wrong option")
