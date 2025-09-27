import numpy as np


# # simple 2-Dimensional vector's representation in matrix format:
# vect1 = np.matrix([2,4], int) #Horizontal Representation
# print(vect1)
# # OR
# vect2 = np.matrix([[2],[4]], int) #Vertical Representation
# print(vect2)

# # simple 3-Dimensional vector's representation in matrix format
# vect3 = np.matrix([2,6,8], int) #Horizontal Representation
# print(vect3)
# # OR
# vect4 = np.matrix([[2],[6],[8]], int) #Vertical Representation
# print(vect4)

"""The first number shows the x-coordinate and the second number shows the y-coordinate 
    (In 2D plane) and 3rd number shows extra z-coordinate (In 3D Plane)
    
    For 2D vectors:-
        - If both numbers are positive, the vector lies in 1st quadrant of graph
        - If x-coordinate is negative and y-coordinate, the vector lies in 2nd quadrant of graph
        - If both numbers are negative, the vector lies in 3rd quadrant of graph
        - If y-coordinate is negative and x-coordinate, the vector lies in 4th quadrant of graph
        - If x-coordinate is 0 the vector is drawn on the y-axis and vice-versa (the sign of the x or y coordinate in this case decides the direction of vector on the axis)
        - If both are 0, the vector is at origin"""

