def outer():
    print("entering outer")
    def inner():
        print("entering inner")
        print("processing")
        print("leaving inner")
    inner()
outer()
print("program ended")