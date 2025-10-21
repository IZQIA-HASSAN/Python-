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

number = [1,2,3,4,5]
count = len(number)

if(count > 2):
    print(f'there number of elements are {count}')

if(count := len(number)) > 2 :
    print(f'the number of elements are {count}')


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

fruits = ["apple" , "banana" ,"mango"]
print("banana" in fruits)
print("apple" not in fruits)


