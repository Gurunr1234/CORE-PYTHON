a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))
# print(a/b)
try:
    res = a/b
    print(res)

except Exception as e:
    print("error in program ")
else:
    print("no error occured")
print("Program ended")