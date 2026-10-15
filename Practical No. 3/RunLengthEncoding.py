# 22.	Run-Length Encoding
# ●	Compress a string by counting consecutive repeated characters. 
# ●	Example:
# 	Input: aaabbccccd
# 	Output: a3b2c4d1

Str=input("Enter a string: ")
count=1
see=""
for i in range(len(Str)-1):
    if Str[i]==Str[i+1]:
        count+=1
    else:
        see+=Str[i]+str(count)
        count=1

# Append the last character and its count
see+=Str[-1]+str(count)
print(see)