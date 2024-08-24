# Q:01=> Calculate your age based on the current year and your birth year.

# import datetime

# def calculate_age(birth_year):
#   """Calculates the age based on the birth year.

#   Args:
#     birth_year: The year you were born.

#   Returns:
#     Your calculated age.
#   """

#   current_year = datetime.date.today().year
#   age = current_year - birth_year
#   return age

# # Get user input for birth year
# birth_year = int(input("Enter your birth year: "))

# # Calculate age
# age = calculate_age(birth_year)

# # Print the calculated age
# print("Your age is:", age)


# Q:02 =>  - Write a program that calculates the area of a rectangle using length and width variables.

# def calculate_rectangle_area(length, width):
#   """Calculates the area of a rectangle.

#   Args:
#     length: The length of the rectangle.
#     width: The width of the rectangle.

#   Returns:
#     The calculated area of the rectangle.
#   """

#   area = length * width
#   return area

# # Get user input for length and width
# length = float(input("Enter the length of the rectangle: "))
# width = float(input("Enter the width of the rectangle: "))

# # Calculate the area
# area = calculate_rectangle_area(length, width)

# # Print the calculated area
# print("The area of the rectangle is:", area)

#Q 3: - Write a program that calculates the area of a circle.

# import math

# def calculate_circle_area(radius):
#   """Calculates the area of a circle.

#   Args:
#     radius: The radius of the circle.

#   Returns:
#     The calculated area of the circle.
#   """

#   area = math.pi * (radius ** 2)
#   return area

# # Get user input for radius
# radius = float(input("Enter the radius of the circle: "))

# # Calculate the area
# area = calculate_circle_area(radius)

# # Print the calculated area
# print("The area of the circle is:", area)

# Q 4:Write a program that calculates the area of the cube.

# def calculate_cube_surface_area(side_length):
#   """Calculates the surface area of a cube.

#   Args:
#     side_length: The length of one side of the cube.

#   Returns:
#     The calculated surface area of the cube.
#   """

#   surface_area = 6 * (side_length ** 2)
#   return surface_area

# # Get user input for side length
# side_length = float(input("Enter the length of a side of the cube: "))

# # Calculate the surface area
# surface_area = calculate_cube_surface_area(side_length)

# # Print the calculated surface area
# print("The surface area of the cube is:", surface_area)

#Q 5: Create a program that converts a temperature from Fahrenheit to Celsius and vice versa using a variable.

# def convert_temperature(temperature, unit):
#   """Converts temperature between Fahrenheit and Celsius.

#   Args:
#     temperature: The temperature value to convert.
#     unit: The unit of the input temperature ('F' for Fahrenheit, 'C' for Celsius).

#   Returns:
#     The converted temperature value.
#   """

#   if unit == 'F':
#     celsius = (temperature - 32) * 5 / 9
#     return celsius
#   elif unit == 'C':
#     fahrenheit = (temperature * 9 / 5) + 32
#     return fahrenheit
#   else:
#     return "Invalid unit. Please enter 'F' for Fahrenheit or 'C' for Celsius."

# # Get user input for temperature and unit
# temperature = float(input("Enter the temperature: "))
# unit = input("Enter the unit (F for Fahrenheit, C for Celsius): ")

# # Convert temperature
# converted_temperature = convert_temperature(temperature, unit)

# # Print the converted temperature
# print("The converted temperature is:", converted_temperature)

#Q 6: Convert a given number of seconds into minutes and seconds using variables.

# def convert_seconds_to_minutes_seconds(seconds):
#   """Converts a given number of seconds into minutes and seconds.

#   Args:
#     seconds: The number of seconds to convert.

#   Returns:
#     A tuple containing the minutes and seconds.
#   """

#   minutes = seconds // 60
#   remaining_seconds = seconds % 60
#   return minutes, remaining_seconds

# # Get user input for seconds
# seconds = int(input("Enter the number of seconds: "))

# # Convert seconds to minutes and seconds
# minutes, seconds = convert_seconds_to_minutes_seconds(seconds)

# # Print the result
# print(f"{seconds} seconds is equal to {minutes} minutes and {seconds} seconds.")

#Q 7:Write a program that calculates the percentage.

# def calculate_percentage(part, whole):
#   """Calculates the percentage of a part to a whole.

#   Args:
#     part: The part to calculate the percentage of.
#     whole: The whole to which the part belongs.

#   Returns:
#     The calculated percentage.
#   """

#   percentage = (part / whole) * 100
#   return percentage

# # Get user input for part and whole
# part = float(input("Enter the part: "))
# whole = float(input("Enter the whole: "))

# # Calculate the percentage
# percentage = calculate_percentage(part, whole)

# # Print the calculated percentage
# print(f"{part} is {percentage:.2f}% of {whole}.")

#Q 8: Write a program that calculates the BMI using height (in meters) and weight (in kilograms) variables.

# def calculate_bmi(height, weight):
#   """Calculates the BMI based on height and weight.

#   Args:
#     height: Height in meters.
#     weight: Weight in kilograms.

#   Returns:
#     The calculated BMI.
#   """

#   bmi = weight / (height ** 2)
#   return bmi

# # Get user input for height and weight
# height = float(input("Enter your height in meters: "))
# weight = float(input("Enter your weight in kilograms: "))

# # Calculate BMI
# bmi = calculate_bmi(height, weight)

# # Print the calculated BMI
# print("Your BMI is:", bmi)

#Q 9:- Write a program that calculates the volume of a cylinder using the formula .

# import math

# def calculate_cylinder_volume(radius, height):
#   """Calculates the volume of a cylinder.

#   Args:
#     radius: The radius of the cylinder's base.
#     height: The height of the cylinder.

#   Returns:
#     The calculated volume of the cylinder.
#   """

#   volume = math.pi * (radius ** 2) * height
#   return volume

# # Get user input for radius and height
# radius = float(input("Enter the radius of the cylinder: "))
# height = float(input("Enter the height of the cylinder: "))

# # Calculate the volume
# volume = calculate_cylinder_volume(radius, height)

# # Print the calculated volume
# print("The volume of the cylinder is:", volume)