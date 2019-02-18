#comment creating pig latin program
original="INCENT"
pgy="ay"
pgy2="oveglay"

word=original.lower()

#check for starting letter using regular expressions
#crustacean
#areway
first=word[0]
if first in 'aeiou':
   newword=word +pgy2
   print(newword)
else:
    newword= word + first + pgy
    print(newword[1:])  
