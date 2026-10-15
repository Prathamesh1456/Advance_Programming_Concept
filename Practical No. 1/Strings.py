String="Computer science "
Course="Engineering"
#Conversions
print(String.upper())   #COMPUTER SCIENCE 
print(String.lower())   #computer science
print(String.capitalize())  #Computer science 
print(String.replace("e","u"))  #Computur sciuncu
print(String.title())   #Computer Science 
print(String.swapcase())    #cOMPUTER SCIENCE 
#Counting
print(len(String))  #17
print(String.count("e"))    #3
#Concatenation
print(String+Course)    #Computer science Engineering
#Validations
print(String.isalnum()) 
print(String.isalpha())
A="123"
print(A.isnumeric())
B="A123"
print(B.isalnum())
