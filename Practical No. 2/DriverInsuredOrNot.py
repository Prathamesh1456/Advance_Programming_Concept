marital_status=input("Enter Y for Married and N for Unmarried: ").lower()
if marital_status=='y':
    print("Driver is Insured")
elif marital_status=="n":
    age=int(input("Enter your age: "))
    Gender=input("Enter M for Male and F for Female: ").lower()
    if (Gender=='m' and age>30):
        print("Driver is Insured")
    elif (Gender=='f' and age>25):
        print("Driver is Insured")
    else:
        print("Driver is Not Insured")
else:
    print("Invalid Marital Status")

