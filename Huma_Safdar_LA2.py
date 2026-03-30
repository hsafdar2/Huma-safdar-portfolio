#-------------------------------------------------------------------------------
# LA2.py
# Student Name: Huma S Safdar
# Version: 
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that 
#                       violates the ethical guidelines as set forth by the
#                       instructor and the class syllabus.
#-------------------------------------------------------------------------------
# References: 
#-------------------------------------------------------------------------------
# Any notes to grader: For example: fully implemented
#-------------------------------------------------------------------------------
# Code starts below this line 
#----------------------------------------------------------------------------
# A simple counter to record how many times a while loop runs:
counter = 0

while True:
    counter += 1
    print("This is how many times the loop is runs:", counter)

    if counter == 5:
        break

print('program ends!')

# Stopping condition setup:
# while True:
#     stop_word = input("Please enter -1 to exit the while loop: ")

#     if stop_word == '-1':
#         break

# print("You have end the while loop!")

# Do not initialize the loop variable inside the loop:
# counter = 0

# while True:
#     counter = 0 # the counter will be reset to 0 in every loop
#     counter += 1
#     print("This is how many times the loop is runs:", counter)

#     if counter == 5:
#         break
