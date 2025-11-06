

def decorate(func):
    def wrapper(a,b):
        print("starting addition")
        func(a,b)
        print("addition done")
    return wrapper



@decorate
def addition(a,b):
    print(f" the sum is:- {a+b}")


addition(70,90)