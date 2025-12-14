'''Instructions:

    Start with Function Definitions:
        Define two functions: square and circle.
        Each function should take one parameter (side for square, radius for circle).

    Write the square Function:
        Calculate the area as side * side and display the result: "The area of the square is [result] square units."

    Write the circle Function:
        Calculate the area using the formula: area = π * radius * radius. Use 3.14 for π.
        Display the result: "The area of the circle is [result] square units."

    Test Your Functions:
        Call square and circle with sample values.
'''

# functon definitions for square and circle  to take one parameter
def square(side):
  area = side * side
  print("The area of the square is", area, "square units.")

# calculating area of circle function 
def circle(radius):
  area = 3.14 * (radius * radius)
  print("the area of the circle is: ", area, "square units")

# doing with user input 

side = float(input("Enter length of side"))
radius = float(input("Enter the radius of the circle")) 

#calling the functions side and radius 

square(side)
circle(radius)
