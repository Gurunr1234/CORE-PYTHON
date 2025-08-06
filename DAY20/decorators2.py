def print_msg():
    msg = "Hello everyone"
    return msg

def outer(print1):
    print("Entering outer")
    def inner():
        print("Entering inner")
        ref1 = print1
        msg2 = ref1()
        new_v = msg2.upper()
        print(new_v)
        print("leaving inner")
    return inner

ptr1 = outer(print_msg)
ptr1()
print("Program ended")