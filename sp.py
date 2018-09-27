myName="silvester stalon"

for letter in myName:
   print(letter)
   
listitems=["mangoes","fruits","bananas","apples","kiwi"]

for fruit in listitems:
    print(fruit.capitalize())
    print(fruit.upper())

for x in range(1,101):
    if(x%2==1):
        print(x, end=" ")
print("\n")
for x in range(2,101):
    if(x%2==0):
        print(x,end=" ")