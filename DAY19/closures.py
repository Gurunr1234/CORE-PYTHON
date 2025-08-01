def outer():
    print("Inside outer")
    def inner():
        print(" inside Inner")
    return inner

ref = outer()
print(ref)
ref()