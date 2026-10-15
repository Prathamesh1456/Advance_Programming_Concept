str=input("Enter a string: ")
new=""
for i in str:
    if i not in new:
        print("The count of ",i," : ",str.count(i))
        new=new+i