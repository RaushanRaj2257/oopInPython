
def decorator(func):
    def wrapper():
        print("*********************")
        func()
        print("*********************")
    return wrapper
def hello():
    print("Hello, sir")

a=decorator(hello)
a()