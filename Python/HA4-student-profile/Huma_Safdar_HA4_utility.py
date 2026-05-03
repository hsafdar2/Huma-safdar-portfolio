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
def add(k, v, students_dict):
    if k not in students_dict:
        students_dict[k] = v
        print("Student information added successfully.")
    else:
        print("Student ID already exists.")


def display(students_dict):
    print("****** Current Student Profile *******")

    for ID in students_dict:
        print(ID + "-" + students_dict[ID][0] + "-" + students_dict[ID][1] + "-" + students_dict[ID][2])


def search(ID, students_dict):
    if ID in students_dict:
        return students_dict[ID]
    else:
        return "Student ID was not found."


def update(ID, update_item, updated_info, students_dict):
    if ID in students_dict:
        update_item = update_item.lower()

        if update_item == "name":
            students_dict[ID][0] = updated_info
            print("Information updated successfully.")

        elif update_item == "email":
            students_dict[ID][1] = updated_info
            print("Information updated successfully.")

        elif update_item == "major":
            students_dict[ID][2] = updated_info
            print("Information updated successfully.")

        else:
            print("Invalid update option.")
    else:
        print("Student ID was not found.")


def delete(ID, students_dict):
    if ID in students_dict:
        del students_dict[ID]
        print("Information deleted")
    else:
        print("Student ID was not found.")

# Implemented under open learning context.
