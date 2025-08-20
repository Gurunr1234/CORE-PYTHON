def fun1():
    print("Entering fun1")
    try:
        fun2()
    except Exception as e:
        print("error in fun1")
    print("leaving fun1")

def fun2():
    print("Entering fun2")
    try:
        res = 10/0
        print(res)
    except Exception as e:
        print("leaving fun2")
        print("======================")
        print(e)
    raise e

print("program started")
fun1()
print("program ended")

