str = input("enter a string: ")

if(str.isalpha()):
    print("str contains only char")
elif(str.isdigit()):
    print("str contains only digit")
elif(str.isalnum()):
    print("str contains both")