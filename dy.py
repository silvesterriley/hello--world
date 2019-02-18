   
days=["monday","tuesday","wednesday","thursday","friday"]

for day in days:
    print(day.capitalize())
    

for x in range(1,11):
    print("{0:2d} {1:3d} {2:4d}" .format(x,x*x,x*x*x*x))


#reading data from text file using python
f=open("C:/Users/silvester/Music/fm.txt","r")
if f.mode=="r":
    contents=f.read()
    print(contents)
f.close()

#reading data from the text file and spliting them into a list
with open("C:/Users/silvester/Music/fm.txt","r") as f:
    data=f.readlines()

for line in data:
    words=line.split()
    print(words)

f.close()

f=open("C:/Users/silvester/Documents/burj.txt" ,"r") 

if f.mode=="r":
    contents=f.read()
    print(contents)
f.close()

#reading data from the text file and spliting them into a list
with open("C:/Users/silvester/Documents/burj.txt" ,"r") as f:
     data=f.readlines()

for line in data:
    words=line.split()
    print(words)

f.close()


#writing data into a text file
with open("C:/Users/silvester/Documents/burj.txt" ,"a") as f:
    for i in range(1,1001):
        f.write("data is been writen from python %d \n"%i)
f.close()


#test string methods
testString="brook forester"
print(len(testString))

print("the length of my string is ", len(testString))

capitals=testString.upper()

print(capitals)

print(testString[0:])

#comment creating pig latin program

py='ay'
original="Brook"
word=original.lower()
first=word[0]
new=word+first
final=new+py

print(final[6:])
myname="brook forester"
First=myname[0]
Last=myname[6]

initials=First+Last

print("my initials are",initials.upper())



#tuples in python
months=('January','february' ,'march', 'April', 'May','June', 'July', 'August', 'September', 'October','November', 'December')
print(months)
for month in months:
    print(month.upper())

print(months[2:6])
print(months[::2])


#list in python
months_list=['January','february' ,'march', 'April', 'May','June', 'July', 'August', 'September', 'October','November', 'December']
print (months_list)

months_list[0]="Jan"
print (months_list)
months_list.append("Dec")
print (months_list)
months_list.pop()

print (months_list)

months_list.reverse()
print (months_list)

months_list.remove("August")
print (months_list)
months_list.insert(4,"Aug")
print (months_list)

#dictionaries in python
shopping_list ={
    "Mango":20.50,
    "Fruit":100.00,
    "Banana":50.00,
    "Apple":30.00,
    "Guava":15.23
}
total =0
for item,price in shopping_list.items():
    total+=price
    print("This {0} costs Kshs {1}".format(item,price))
    
print("Total is = ",total)
print(shopping_list)
print(shopping_list.values())
print(shopping_list.keys())


    
    
#functions in python
def addTwo (x,y,z):
    return x+y+z 
sum=addTwo(2,6,8)
print("the sum is = ",sum) 

#function that can calculate Area of a circle
def AreaOfCircle(r):
    pI=3.142
    return pI*(r**2)

Area=AreaOfCircle(14)
print("the area =",Area)




#calculate Area of perimeterof Rectangule
def PerimeterOFRectangule (L,w):
    return (L+w)*2

perimeter=PerimeterOFRectangule (4,6)
print("perimeter=",perimeter)

#recusive functions in python recursin is where a function calls itself
def fact(n):
    if(n==0):
        return 1
    else:
        return n * fact(n-1)
print(fact(5))
print(fact(9))

#fibonacci sequence
def fibo(n):
    if(n==0):
        return 0
    elif n==1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
x=150
if x<=0:
    print("wrong number")
else:
    for i in range(x):
        print(fibo(i),end=" ")


#classes in python
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def my_results(self):
        print("i am called {0} and my age is {1}".format(self.name,self.age))
p1=person("samantha", 50)
p2=person("judy",40)

p1.my_results()

p2.my_results()