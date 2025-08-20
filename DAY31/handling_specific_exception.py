try:
    print("Enter a value1")
    a = int(input())
    print("Enter a value2")
    b = input()
    res = a/b
    print(res)

except ValueError as e:
    print("it is VE")

except ZeroDivisionError as e:
    print("it is ZDE")

except Exception as e:
    print("it is error")