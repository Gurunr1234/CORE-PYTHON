print("enter a string:")
str = input()

i = 0
newstr = ""
while i < len(str):
    a = str[i]
    ascii = ord(a) # ord is used to convert character to ascii value
    if (ascii >= 65 and ascii <= 90):  # check if the character is uppercase
        ascii = ascii + 32
        constr = chr(ascii)   # chr is used to convert ascii value to character 
        newstr= newstr + constr
    else:
        ascii = ascii - 32
        constr = chr(ascii)
        newstr = newstr + constr
       

    i = i + 1

print("the new string is:", newstr)