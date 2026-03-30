# Huma_Safdar_LA3.py
# Student Name: Huma Safdar
# Version: 1.0
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines as set forth by the
# instructor and the class syllabus.
#-------------------------------------------------------------------------------
# References: Module resources and lab hints
#-------------------------------------------------------------------------------
# Notes to grader: Fully implemented
#-------------------------------------------------------------------------------
# Code starts below this line
#-------------------------------------------------------------------------------

first_name = input("Enter first name: ")

last_name = input("Enter last name: ")

age = int(input("Enter age: "))

temps = []

counter = 1

while counter <= 3:
    temp = input("Enter temperature for day {}: ".format(counter))
    
    temp = float(temp)

    temps.append(temp)

    counter = counter + 1

average = sum(temps) / len(temps)

# label based on average temperature

if average < 95.0:
    label = "Hypothermia"
    
elif average <= 99.5:
    label = "Normal"
    
elif average < 104.0:
    label = "Fever/Hyperthermia"
    
elif average < 105.8:
    label = "Hyperpyrexia"
    
else:
    label = "Invalid Range"

print("\nResult")

print("Name: {} {}".format(first_name, last_name))

print("Age: {}".format(age))

print("Temperatures: {}".format(temps))

print("Average: {:.2f}".format(average))

print("Condition: {}".format(label))

