#Write a python comment saying 'Day 2: 30 Days of python programming'
#'Day 2: 30 days of python programming'
#Declare a first name variable and assign a value to it
first_name = "Mukul"
#Declare a last name variable and assign a value to it
last_name  = "Chaudhari"
#Declare a full name variable and assign a value to it
full_name = first_name + last_name
#Declare a country variable and assign a value to it
country = "United States"
#Declare a city variable and assign a value to it
city = "Los Angeles"
#Declare an age variable and assign a value to it
age = 29
#Declare a year variable and assign a value to it
year = 1994
#Declare a variable is_married and assign a value to it
is_married = False
#Declare a variable is_true and assign a value to it
is_true = True
#Declare a variable is_light_on and assign a value to it
is_light_on = True
#Declare multiple variable on one line
first_name,last_name,country = "Mukul","Chaudhari","United States"

################################################################
##Exercises: Level 2
################################################################\

#Check the data type of all your variables using type() built-in function
print(type(first_name))
print(type(last_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

#Using the len() built-in function, find the length of your first name
print(len(first_name))

#Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4

#Add num_one and num_two and assign the value to a variable total
total = num_one+num_two
print(total)

#Subtract num_two from num_one and assign the value to a variable diff
diff = num_one-num_two
print(diff)
#Multiply num_two and num_one and assign the value to a variable product
product = num_one*num_two
print(product)
#Divide num_one by num_two and assign the value to a variable division
division = num_one/num_two
print(division)
#Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = num_one%num_two
print(remainder)
#Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_one**num_two
print(exp)
#Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_divison = num_one//num_two
print(floor_divison)
#The radius of a circle is 30 meters.
#Calculate the area of a circle and assign the value to a variable name of area_of_circle
r = 30
pie = 3.14
area_of_cricle = pie*r**2
print(area_of_cricle)
#Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
circum_of_circle = 2*pie*r
print(circum_of_circle)
#Take radius as user input and calculate the area.
radius = float(input('radius of the circle'))
area = pie*radius**2
print(area)
#Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
first_name = input('What is your name: ')
last_name = input("your last name : ")
age = input('How old are you? ')
print(first_name)
print(last_name)
print(age)