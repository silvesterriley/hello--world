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
a=64
b=10
c=690
total = a+b+c
average = total//3
difference =c-a
remainder =b%a
print("the total of {0} + {1} + {2} is = {3}" .format(a,b,c, total))
print("the difference btwn {0} - {1} is ={2}" .format(c, a, difference))
print("the average of {0} + {1} + {2} is = {3}" .format(a,b,c, average))
print("the remainder of {0} divided by {1}  is = {2}" .format(b, a, remainder))

#test for largest
if(a<b):
    print("{0} is largest".format(b))
else:
    print("{0} is largest".format(a))



    
#test for adult minor 
Age=7
while(Age!=-7):
    Age=int(input("enter your age or -7 to exit \n"))
    if(Age>=18):
        print("if you are {0} years old then you ar an adult".format(Age))
    else:
        print("if you are {0} years old then you ar a Minor".format(Age))




#test for odd and even
number=int(input("enter any number \n"))
if(number%2 ==0):
    print("{0} is even number".format(number))
else:
    print("{0} is odd number".format(number))


#Area of rectangle
#calculate 
Length= 20
width= 10
area=(Length * width)
perimeter=(Length + width)*2

#output
print("the length is = {0} and width is ={1} thus the area is={2}".format(Length,width, area))
print("the length is %d and width is %d thus the area is %d thus be perimeter" %(Length,width,perimeter))