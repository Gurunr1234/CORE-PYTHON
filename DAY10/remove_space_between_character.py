str = input("Enter a string: ")

i = 0
newstr = ""

while i < len(str):
    if str[i] == " ":
        i += 1
    else:
        newstr += str[i]
        i += 1
print(newstr)














# str = "rama and sita"
str = input("Enter a string: ")

newstr = ""

for i in range(len(str)):
    if str[i] == " ":
        continue
        #print()
    else:
        newstr = newstr + str[i]

print("the new string is:", newstr)