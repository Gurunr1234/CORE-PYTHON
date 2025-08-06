def outer():
    print("entering outer")
    def inner():
        print("entering inner")
        print("processing")
        print("leaving inner")
    return inner
ref1 = outer()
print("after executing outer")
ref1()
print("after executing inner or ref1")