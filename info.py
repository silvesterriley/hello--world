message="hello python"
print(message)

#variables to hold my names
firstname="cassandra"
middlename="Ndanu"
lastname="Nduati"
Age=24


#i want to print my details
print("My first name is", firstname)
print("My middle name is" ,middlename)
print("My last name is" ,lastname)
print(Age,"years old")


#printing all variables in one line
print("My first name is {0} and My middle name is {1} and last name is {2} {3} years of age".format(firstname,middlename,lastname,Age))

#printing all variables in one line using percentage
print("My first name is %s and My middle name is %s and last name is %s %d years of age" %(firstname,middlename,lastname,Age))

#simple calculation 
a=6
b=10
total = a+b
print(total)

#Area of rectangle
#calculate 
Length= 20
width= 10
area=(Length * width)
perimeter=(Length + width)*2

#output
print("the length is = {0} and width is ={1} thus the area is={2}".format(Length,width, area))
print("the length is %d and width is %d thus the area is %d thus be perimeter" %(Length,width,perimeter))