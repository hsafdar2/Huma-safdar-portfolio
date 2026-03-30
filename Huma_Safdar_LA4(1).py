#-------------------------------------------------------------------------------
# source_file_name.py
# Student Name: Huma Safdar
# Assignment: LA4
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines as set forth by the
# instructor and the class syllabus.
#-------------------------------------------------------------------------------
# References: (list of web sites, texts, and any other resources used)
#-------------------------------------------------------------------------------
# Note to grader: (a note to the grader as to any problems or uncompleted aspects of
# of the assignment)
#-------------------------------------------------------------------------------
# NOTE: width of source code should be < 80 characters to facilitate printing
#-------------------------------------------------------------------------------
# Source Code: Write your code below
seven_wonders = ["China:Great wall", "Jordan:Petra", \
                     "Brazil:Christ the Redeemer", \
                     "Peru: Machu Picchu", "Mexico:Chichen Itza", \
                     "India:TajMahal", "Italy:Colosseum" ]

hint = 0
found = False 

servicerequest = input("Type a location or a wonder name (press Enter for hint): ")

if servicerequest == "":
    hint = 1
    print("Hint - the wonders are in:")
    print("China, Jordan, Brazil, Peru, Mexico, India, Italy")
    servicerequest = input("Now type the wonder name: ")

for item in seven_wonders:

    location, wonder = item.split(":")

    # checking if user typed location
    if servicerequest.lower() == location.lower() and hint == 0:
        print("Correct! " + wonder + " is located in " + location)
        found = True

    # checking if user typed wonder name
    elif servicerequest.lower() == wonder.lower():
        print("Correct! " + wonder + " is located in " + location)
        found = True

# if nothing matched
if found == False:
    print("Wrong input, the program ends here")
