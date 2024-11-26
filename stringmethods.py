a = "BITCH AS STAR"
print(a.lower())
c= a.casefold()  #casefold is used to convert string to lower case .
print(c)  
d = a.center(40) ### place of center to string 
print(d)

e = a.count("A") ## count the number of word  ### the number of times a specified value occurs in a string
print(e)

 #indicates that the string is now in bytes format, prefixed with b.
 ###The encode() method converts the string into a bytes object using the specified encoding (default is 'utf-8').
#UTF-8 is a standard encoding format for text.

f = a.encode()  # Encode the string using UTF-8
print(f)

g = a.endswith("R")   ##if it ends with R then true otherwise false .
print(g) 

txt = "H\te\tl\tl\to"
h = txt.expandtabs(6)
print(h) 
print(txt)
print(txt.expandtabs())
print(txt.expandtabs(2))
print(txt.expandtabs(4))
print(txt.expandtabs(10))

txt1 = "Hello, welcome to my world."

x = txt1.find("welcome")             ## word found then finds the first occurrence of the specified value then 0 
# if not found then it return -1 .
print(x) # output will be at the 7th position first letter of welcome word .


txt2 = "Hello, welcome to my world."

x = txt2.find("e", 0, 10)  ### 5 index to  in between 7 index position .

print(x)


txt3 = "Hello, welcome to my world."

x = txt3.find("e", 5, 9)  ### 5 index to  in between 7 index position .

print(x)

txt4 = "For only {price:.2f} dollars!" ## 2f is a decimal .
print(txt4.format(price = 49))

# input stored in variable a. 
z= {'x':'John', 'y':'Wick'} 
  
# Use of format_map() function 
print("{x}'s last name {y}".format_map(z))
print(z)


txt6 = "Demo"

x = txt6.isidentifier()  ### is identifier true or false .

print(x)

txt8 = "1234"

x = txt8.isdecimal()  ### is decimal() then true .

print(x)

txt7 = "50800"

y = txt7.isdigit()   ## isdigit() then true .

print(y)

#### swapcase()	Swaps cases, lower case becomes upper case and vice versa
txt10 = "Hello My Name Is PETER"

c = txt10.swapcase()

print(c)
###join()	Joins the elements of an iterable to the end of the string

myTuple = ("John", "Peter", "Vicky")

x = "#".join(myTuple)

print(x) 

myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"          

j= mySeparator.join(myDict)   ####Joins the elements of an iterable to the end of the string

print(j)
         
           ####### python boolean 
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")        


###Evaluate a string and a number:

print(bool("Hello"))
print(bool(15))

x = "Hello"
y = 15

print(bool(x))
print(bool(y))

print(10>9)


print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))



print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

# Almost any value is evaluated to True if it has some sort of content.

# Any string is True, except empty strings.

# Any number is True, except 0.

# Any list, tuple, set, and dictionary are True, except empty ones.


# Input: isinstance([1, 2, 3], list)
# Output: True
# Explanation: The first parameter passed is of list type.
# Input: isinstance(10, str)
# Output: False
# Explanation: The first parameter, 10 is an integer and not a string.



#Syntax: 


#isinstance(obj, class)


# Parameters :


# obj : The object that need to be checked as a part of class or not.
# class : class/type/tuple of class or type, against which object is needed to be checked.

# Returns : True, if object belongs to the given class/type if single class is passed 
# or any of the class/type if tuple of class/type is passed, else returns False.


numbers = [1, 2, 3, 4, 2, 5]
 
# Check if 'numbers' is an instance of a list
result = isinstance(numbers, list)
 
if result:
    print("The variable 'numbers' is an instance of a list.")
else:
    print("The variable 'numbers' is not an instance of a list.")
    
    
    



# declaring classes
class gfg1:
    a = 10
 
# inherited class
class gfg2(gfg1):
    string = 'GeeksforGeeks'
 
 
# initializing objects
obj1 = gfg1()
obj2 = gfg2()
print(obj1)
print(obj2)

 #checking instances
print("Is obj1 instance of gfg1? : " + str(isinstance(obj1, gfg1)))
print("Is obj2 instance of gfg2? : " + str(isinstance(obj2, gfg2)))
print("Is obj1 instance of gfg2? : " + str(isinstance(obj1, gfg2)))
 
 
# check inheritance case
# return true
print("Is obj2 instance of gfg1? : " + str(isinstance(obj2, gfg1)))

                 #  Python divides the operators in the following groups:

# Arithmetic operators
# Assignment operators
# Comparison operators
# Logical operators
# Identity operators
# Membership operators
# Bitwise operators


 ###  7 arithmetic operation 
# +,-,*,/,**,//,%

# Assignment operators are used to assign values to variables:

#  += x = x+3
x = 0  # Initialize x with a value
x = x + 3
print(x)


#        6   Comparison operators are used to compare two values:

# Operator	Name	Example	Try it

# ==	Equal	        x == y	
# !=	Not equal	    x != y	
# >	   Greater than	    x > y	
# <    Less than	    x < y	
# >=   Greater than or equal to	     x >= y	
# <=   Less than or equal to	     x <= y


# Logical Operators
# and or not 

##Returns True if both statements are true
# Returns True if one of the statements is true
###	Reverse the result, returns False if the result is true

# Identity Operators
# is identify operator 
# is not identify operator

x = 3
y = 3
x = z

print(x is z) 
print(x is y)
print(x==y)












