   
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



    
    
    