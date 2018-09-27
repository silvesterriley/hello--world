message="python"
print(message)

#variables to hold my names
firstname="aivah"
middlename="Nonny"
lastname="honey bee"
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

#number of voters and who are not voting
a=890
b=67
c=230
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
Age=20
while(Age!=18):
    Age=int(input("enter your age or 27 to exit \n"))
    if(Age>=18):
        print("if you are {0} years old then you are able to vote".format(Age))
    else:
        print("if you are {0} years old then you are not able to vote".format(Age))




    
