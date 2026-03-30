#-------------------------------------------------------------------------------
# LA5.py
# Name: Huma Safdar
# Python Version: 2.XX or 3.XX
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
#                       violates the ethical guidelines as set forth by the
#                       instructor and the class syllabus.
#-------------------------------------------------------------------------------
# References: 
#-------------------------------------------------------------------------------
# Any notes to grader: For example: fully implemented
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
# Code: Code starts here
#-------------------------------------------------------------------------------

def calculate_area(A, B, C):

    S = (A + B + C) / 2
    AREA = (S * (S - A) * (S - B) * (S - C)) ** 0.5

    return AREA


def main():

    N = int(input("How many triangles: "))

    AREAS = []

    for I in range(N):

        print("Triangle # {}".format(I + 1))

        A = float(input("Enter side 1: "))
        B = float(input("Enter side 2: "))
        C = float(input("Enter side 3: "))

        AREA = calculate_area(A, B, C)

        print("Area of the triangle {} is {:.2f}".format(I + 1, AREA))

        AREAS.append(AREA)

    print("Max area is: {:.2f}".format(max(AREAS)))


main()
