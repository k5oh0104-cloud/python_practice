# declare variable 
# variable_name = value to assign
# =(equal sign) means assign not equal 
temp = 25
name = "sensor_A"
print(temp)
print(name)

x = 10
print("x when first assigned:",x)
x = 15
print("x after reassignment:",x)
x = x + 5 # assign x using previous x value
print("x after calculation:",x)

## rules of variable name
# can not begin with a number, (_) is the only special character allowed
# snake case is recommended in python 
# should not contain spaces
# 2sensor = 10 > cannot start with a number
sensor_count = 3 
sensorCount = 3, # an example of a camel case 
print(sensor_count,sensorCount)
temp2 = 25
print(temp2)

#if = 15 #Reserved words like for, if, false cannot be used as a variable name

## lower and upper case in variable names are distinguished
temp = 10
Temp = 100
print("temp, Temp",temp, Temp)

score = 50
score = 75
score = 90
print("score:",score)

## store a value from another variable 
# alt + shift + (up,down)
a = 10
b = a
a = 11
print("a:",a)
print("b:",b)

## assign multiple variables in a single line
width, height = 4,3
print("width: ",width)
print("height: ",height)
print("the area of a rectangle: ", width*height)



