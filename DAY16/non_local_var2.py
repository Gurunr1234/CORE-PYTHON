def fun1():
    a = 999
    print("from fun1 a is ", a)
    def fun2():
        a = 10
        b = 20
        print("from fun2 b is ", b)
        print("from fun2 a is ", a)

    fun2()
    print("from fun1 a is ", a)
    print("from fun1 b is ", b)

fun1()