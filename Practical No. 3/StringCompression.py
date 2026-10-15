# 23.	String Compression 
# ●	Compress repeated characters and return the original string if compression does not reduce the length. 
Str=input("Enter a string: ")
compressed=""
count=1
for i in range(len(Str)-1):
    if Str[i]==Str[i+1]:
        count+=1
    else:
        compressed+=Str[i]+str(count)
        count=1


compressed+=Str[-1]+str(count)


if len(compressed) >= len(Str):
    print(Str)
else:
    print(compressed)