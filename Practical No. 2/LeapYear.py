#Write a python Program to check a year for leap year
year=int(input("Enter a year: "))
if(year%400==0) or (year%4==0 and year%100!=0):
    print("Given year is a leap year..!!")
else:
    print("Given year is not a leap year")
