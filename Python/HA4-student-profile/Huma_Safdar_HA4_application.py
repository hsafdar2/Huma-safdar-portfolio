#-------------------------------------------------------------------------------
# Student Name: Huma Safdar
# Assignment: HA4
# Python version:
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines as set forth by the
# instructor and the class syllabus.
#-------------------------------------------------------------------------------
# References: Textbook, Python Documentation
#-------------------------------------------------------------------------------
# Notes: Any general comments to the grader
#-------------------------------------------------------------------------------
# importing utility file
import Huma_Safdar_HA4_utility as u


# this function reads the file and returns all lines
def read_file():
    fp = open('studentProfile.txt', 'r')
    students = fp.readlines()
    fp.close()
    return students


# this function converts file data into a dictionary
def create_dict(students):
    students_dict = {}

    for line in students:
        line = line.strip()

        # skip empty lines just in case
        if line != '':
            parts = line.split('|')

            # ID is key, rest is list
            ID = parts[0]
            name = parts[1]
            email = parts[2]
            major = parts[3]

            students_dict[ID] = [name, email, major]

    return students_dict


# writes updated dictionary to new file
def write_file(students_dict):
    fp = open('studentProfileupdated.txt', 'w')

    for ID in students_dict:
        info = students_dict[ID]
        line = ID + "|" + info[0] + "|" + info[1] + "|" + info[2] + "\n"
        fp.write(line)

    fp.close()


def main():
    # get data from file
    students = read_file()

    # convert to dictionary
    students_dict = create_dict(students)

    menu = "\n\n1. Add\n2. Search\n3. Update\n4. Delete\n5. Display\n6. Exit"
    choice = "0"

    while choice != "6":
        print(menu)
        choice = input("\nEnter your choice (1-6): ")

        # ADD
        if choice == "1":
            ID = input("Enter student ID to add: ")
            name = input("Enter full name: ")
            email = input("Enter email address: ")
            major = input("Enter major: ")

            u.add(ID, [name, email, major], students_dict)

        # SEARCH
        elif choice == "2":
            ID = input("Enter student ID: ")
            result = u.search(ID, students_dict)
            print(result)

        # UPDATE
        elif choice == "3":
            ID = input("Enter student ID to update: ")
            item = input("Which one to update (name/email/major)? ")
            new_value = input("Enter updated info: ")

            u.update(ID, item, new_value, students_dict)

        # DELETE
        elif choice == "4":
            ID = input("Enter student ID to delete: ")
            u.delete(ID, students_dict)

        # DISPLAY
        elif choice == "5":
            u.display(students_dict)

        # EXIT
        elif choice == "6":
            print("Exiting application, writing updated info to file...")
            write_file(students_dict)

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

# Implemented under open learning context.
