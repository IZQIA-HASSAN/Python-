#import sys
#print(sys.version)
##  IDENTATION IN PYTHON ;
# it is basically spacing at the begining of the code line 
#identation is for readibility of the code 
#it is also used to determine the scope of loops and function etc
#idenatation is also used to indicate a block of code 

# PRINTING IN PYTHON :

#end=" "  -> this will help to merge two print() statements into one
"""print("good night" , end=" ")
print("i will be sleeping")
print('i am ' , 18 , 'years old')"""

# COMMENTS IN PYTHON :
 
 #this is a comment 

"""
  this is a multiline comment
"""

# VARIABLES IN PYTHON :
# variables are containers fr storing data 

"""x = 5
y = 'john'
print(x)
print(y)
"""

#x = 4
#x = 5
#print(x)

# CASING IN VARIABLES
# if you want to specify the data type of variable you can do that

"""x = str("meer")
y = int(45)
z = float(34.5)"""

#we can know the type of the variable by using type() function

#z = 45.5
#print(type(z))
#_ = "hello i am an underscore"
#print(_)

# assigining multiple  variables 
"""x ,y ,z = "izqia" , "ul", "hassan"
print(x , end="")
print(y , end='')
print(z)
"""

"""x=y=z="one value to multiple variables "
print(x)
print(y)
print(z)
"""

#unpacking a list or tuple

"""fruits = ["apple " , "orange" ,"pomegranate"]
x,y,z = fruits
print(x)
print(y)
print(z)
"""

"""x = "x"
y = "y"
z = "z"
print(x,y,z)
"""

# GLOBAL VARIABLES IN PYTHON :
 
"""x = "python is awesome"

def myfunction():
    global x
    x = "hello"
    print("hey!" + x)

myfunction()
 
print(x)
"""

# DATA TYPES IN PYTHON :

# python has following data types built-in by default
# python has 15 built-in data types 

#text type : str
#Numeric Types : int , float , complex
#Sequence Types : list , tuple , range
#Mapping Types : dict
#Set Types : set , frozenset
#Boolean Types : bool
#Binary Types : bytes , bytearray , memoryview
#None Type : NoneType

"""x = 23.43
y = 1j
z = ["CS" , "BS" , "MS"]
a = {"king" , "queen" , "hand"}
b = ("hello" , "world" , "mello")
c = {"name" : "john" , "fame" : "song"}
d = b"programmer"
e = bytearray(5)
f = memoryview(bytes(2))
g = None
print(type(x))
print(type(y))
print(type(z))
print(type(a))
print(type(b))
print(type(c))
print(d)
print(e)
print(f)
print(g)
"""

#we can also specify the data types by writing its type before it like e.g

"""x = float(34.5) 
y = 10
print(x , y)"""

#PYTHON NUMBERS :

# there are three numeric types in python 
# 1. int 
# 2. float 
# 3. complex
 
 #inetegr values are of unlimited length
"""y = -348374974932843984937493
x = 1111243333333333333356777777777777
print(x)
print(y)
#z = 1/0 #this will give zero division error and its type will not be given by the interpreter
#rint(type(z))

c = 5e2
d = 12E4
z = -20.7e2
# any value of e like e2 wil move the point upto two places to  the right
print(d)
print(c)
print(z)
"""

#complex number s

"""x = 3 + 9j
y = -5j
print(x , y)
"""

#type conversion 

"""x = 23
y = 78.34
z =4j

a = float(x)
b = int(y)
c = complex(x)

print(type(a))
print(type(b))
print(type(c))

print(a)
print(b)
print(c)
"""
#complex number cannot be converted into any other type 


# RANDOM NUMBER IN PYTHON :

"""import random
#rint(random.randrange(0,100))

x = random.randrange(0,10)
print(x)
"""

# CASTING IN PYTHON :

# casting is same as type conversions . we can chane the type of any variable by specifying the type we want like 

"""x = float(31) """
#now x will be 31.0

# PYTHON STRINGS :
#a = """hi this is my lenove laptop,
#i bought it for 30k,
#ts amazing"""
#print(a)

#-> strings are arrys 
"""a = "milky way "
print(a[2])
print(a[5])"""

#-> looping through strings
"""a = "technology"
for x in 'apple':
    print(x)


print(len(a))

text = "change is permenant !"
print("mange" in text)#used to check wether a word is present in the string or not 

if "change" in text:
    print("yes change is present")
else:
    print("no change is not present")"""

#-> SLICING IN STRING :

"""
b = 'HELLO WORLD'
print(b[2:7])
print(b[:5])
print(b[1:])
print(b[-5:-2])
"""

"""a = " HASSAN "
print(a.lower())
print(a.upper())
print(a.strip())#this strip method returns the string by removing the white spaces from it .
print(a.replace("H" , 'W')) #-> replace method repace the string 


b = "hello , world"
print(b.split(","))

#concatenating strings in python 

a = "sheryar"
b = "khan"
c = a + b
print(c)
#to add a space between strings add ""
d = a + ' ' + b
print(d)
name = "hassan "
print("my name is " , name)

#-. formatting in strings
# strings can b e formatted by using f-method

age = 18
text = f"my name is izqia and i am {2*9} years old"
print(text)

print("i would love to watch  \'interstellar\' from christopher nolan ")
h = "hello"
print(h.translate())
"""

# BOOLEAN IN PYTHON ;
"""print(20 > 21)
print(1 == 1.0)

a = 20
b = 30

if a > b :
    print("a is greater than b")
else:
    print("a is not greater than b")


print(bool("helo"))
print(bool(12))
"""

# PYTHON OPERATORS :

"""
python arithematic operator includes the following :
-> addition
-> subtraction
->multiplication
->Division
->Modulus
->exponentiation
->Floor division"""#(return an inetger)

"""x =15
y = 2
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x // y)
print(x ** y)"""

# ASSIGNMENT OPERATOR IN PYTHON :
# -> assignment operators are used to assign value to the variables 
"""

=
+=
-=
*=
/=
%=
//=
**=
&=
|=
^=
>>=
<<=
:= (Walrus operator)
"""


# walrus operator 
#-> it is used to assign an expressin to a variable 

#like 

"""number = [1,2,3,4,5]
count = len(number)

if(count > 2):
    print(f'there number of elements are {count}')

if(count := len(number)) > 2 :
    print(f'the number of elements are {count}')

"""
#COMPARISON OPERATOR :

"""

==
!=
>
<
>=
<=
"""
#chaining comparison :
"""x = 5

print(1 < x < 10)

print(1 < x and x < 10)"""

#LOGICAL OPERATORS IN PYTHON :
#-> logical operators are used to combine conditional statements
"""
-> and 
->or
->not
"""

"""x = 5 
if(x > 0 and x < 10):
    print(' x lies between 1 -10')

print(x < 5 or x > 10)

print(not(x > 3 and x < 10))"""

# IDENTITY OPERATOR IN PYTHON :

#-> is -> returns true if both the variable are the same object 
#-> isnot ->returns true if both varibles are not the same 

"""x = ["apple" , "bannana"]
y = ["orange" , "plum"]
z= x

print(x is z)
print(x == z)
print(x is not y)"""

#MEMBERSHIP OPERATOR IN PYTHON :

# in ->
# not in ->
"""
fruits = ["apple" , "banana" ,"mango"]
print("banana" in fruits)
print("apple" not in fruits)
"""

# BITWISE OPERATOR IN PYTHON :
# Bitwise operator in python are used to compare (binary) numbers ;

"""
& -> AND 
| -> OR
^ -> XOR
~ -> NOT
<< -> zero fill left shift
>> -> signed right shift

"""

# LIST IN PYTHON :
#list are used to store multiple items in a single variable .

"""mylist = ["apple" , "banana","cherry"]
print(len(mylist))

list2 = ["abc" , "123" , True, "male"]
print(list2)
print(type(list2))

thislist = list(("apple","catchy","merger","almond","walnut","pistachio"))
print(thislist)
print(thislist[0:3])
print(thislist[0:])

if "pistachio" in thislist:
    print("yes , available")

thislist[1] = "machine" 
print(thislist)

thislist = ["shiekh" , "non-shiekh" ,"clean-shiekh","pure-shiekh","mutant-shiekh"]
thislist[1:3] = ["non-pta" , "non-pta"]
print(thislist)
thislist[1:2] = ["ahmed" , "muhammad"]
print(thislist)
thislist[1:3] = ["watermelon"]
print(thislist)
"""
#->insert() , this method is used to insert any value at the specified location .
"""
list = ['one' , 'two' , 'three']
list.insert(2,"two.two")
#print(list)

#-> we can also add items at any wanted location , like we can specify the index where we want to add the item .

list.insert(0 , "zero")
#print(list)

#-> to add an item at the end of the list we will use append() method

list.append("four")
#print(list)

#-> to append items from another list to the list use extend() method to do so , 

list1 = ["ali ", "ahmed" ,"raza"]
list2 = ["animal" , "bird" ,"saregamapa"]
list2.extend(list1)
#print(list2)

#-> we can add extend tuples ,dictionaries , sets etc ;

list3 = {"set" , "null" ,"super"}
list2.extend(list3)
#print(list2)

#-> removing list item : use remove() method to do so ,

list4 = ["laptop","pc","macos","android","laptop"]
#list4.remove("pc")
#print(list4)

#-> if there are two similar elements then the first occurence will be removed .

#list4.remove("laptop")
#print(list4)

#-> the pop ,ethos removes the specified index items 

#list4.pop(2)
#print(list4)

#-> if item is not specified the last item will be removed automatically 

#-> del keyword is also used to remove or delete the items.

del list4[0]
print(list4)

listing = ["one" ,'two',"three"]
del listing #this delete the list now the list nomore exist.

#-> clear() method clears the list , the list still exist but there are no items in it .

my_list = ["1" ,"2",'3']
my_list.clear()
print(my_list)
"""

#-> today enough start from looping throug list .

#-> looping through list 

"""list = ["apple","orange","pine"]
for x in  list:
    print(x)

for i in range(len(list)):
    print(list[i])

i = 0
while i < len(list):
    print(list[i])
    i = i + 1

#-> comprehension methos to loop through list;

this_list = ["1" ,"2" ,"3","4"]
[print(x) for x in this_list]

#-> list comprehension :

# for example if w want to make a new list having items form another list starting from a specific alphabet we can do it by using following wway.

newlist = ["ahmed","asghar","ali","murtaza","shahab"]

newlist2 =[]

for x in newlist:
    if "a" in x:
        newlist2.append(x)

print(newlist2)

newlist2 = [x for x in newlist if x != "ali"]
print(newlist2)

newlist2 = [x for x in newlist]
print(newlist2)

newlist2 = [x.upper() for x in list]
print(newlist2
"""

# -> sorting in lists 

"""thislist = ["pummpy" ,"yumpy","yumpkin","cuppycake"]
thislist.sort()
print(thislist)

numerical = [100,200,100.5,232,545]
numerical.sort()
numerical.sort(reverse = True)
print(numerical)

#-> Sorting through functions ;

def myfun(n):
    return abs(n-100)

mylist = [100,50,65,82,23]
mylist.sort(key = myfun)
print(mylist)

#-> Case-sensitive sorting can give unexpected results : 

ourlist = ["apple" , "orange" ,"Kiwi","plum"]
ourlist.sort()
print(ourlist)

#-> if you want case-insensitive sorting , tehn use str.lower as a key function :

listing = ["banana","apple","pine-apple"]
listing.sort(key = str.lower)
print(listing) 
listing.reverse()
print(listing)

"""

#-> copy list 


thislist = ["bmw","ferrari","legender","bugati","g-wagon"]
mylist = thislist.copy()
print(mylist)
print(thislist)

#-> we can also use list() to make a copy of a list 

mylist2 = list(thislist)
print(mylist2)

# -> we can also make copy by using slice operator 
"""
mylist3 = thislist[:]
print(mylist3)"""

#-> joining two list ;

alpha = [1,2,3,4]
gamma = [5,6,7,8]
"""
list3 = gamma + alpha
print(list3)
"""

# another way 

list1 = [1,2,3,4]
list2 = [5,6,7,8]

"""for x in list1:
    list2.append(x)

print(list2)
"""

list1.extend(list2)
print(list1)

#-> list methods in python :


#-> listing some important methods in python ;
"""

append()
clear()
copy()
count()
extend()
index()
insert()
pop()
remove()
reverse()
sort()

"""



# TUPLES IN PYTHON :
# tuples are used to store multiple items in a single variable .
# it is ordered and unchangeable 


#.. we will be continuning tuple etc after loops and functions 







# -> python conditions ans if statements 

a = 23 
b = 45
if a < b :
    print("23 is greater than b ")
    print("python is gorgeous")
    print("ultimately , python will bw your first love !")


is_logged_in = False
if is_logged_in:
    print("nothing will be printed when your variable is set as false ")



x = 90 
y = 90

if x > y:
    print('x is greater')
elif x == y:
    print("both are exact ")


marks = 70

if marks == 70:
    print("Grade B")
elif marks > 70:
    print("Grade B+")
elif marks > 80:
    print("Grade A")
elif marks > 85:
    print("Grade A+")

username = "izqia"

if len(username) > 2:
    print(f"welcome {username} can be entered")
else:
    print("Error : user name is not of proper length ")


# the use of ternary operator :

my = 3
your = 4

print("my") if my > your else print("your")

# nested if  ,  the code evalutes from outer most condition to inward :

age = 18
has_liscence = True

if age >= 18:
    if has_liscence:
        print("can drive")
    else:
        print("you need a liscence")
else:
    print("you are too young to drive ")



# pass statements in python 
"""
Why Use pass?
The pass statement is useful in several situations:

When you're creating code structure but haven't implemented the logic yet
When a statement is required syntactically but no action is needed
As a placeholder for future code during development
In empty functions or classes that you plan to implement later



pass vs Comments
A comment is ignored by Python, but pass is an actual statement that gets executed (though it does nothing). 
You need pass where Python expects a statement, not just a comment.

"""


score = 85

if score > 90:
  pass 
print("Score processed")


value = 50

if value < 0:
  print("Negative value")
elif value == 0:
  pass # Zero case - no action needed
else:
  print("Positive value")



# -> LOOPING IN PYTHON :

# While loop

i =1 
while i <= 10:
    print(i)
    i+=1
else:
    print("now i will not be printed , beacuse i is no longer greater than 10 ")

# xe = 1
# while xe < 6:
#     print(xe)
#     if xe == 5:
#         break
#     xe+=1





