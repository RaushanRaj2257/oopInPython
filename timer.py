import time

def timer(func):
    def wrapper(*args):
        start=time.time()

        func(*args)
        print(f"time taken by {func.__name__}=",time.time()-start," sec")
    return wrapper

@timer
def hello():
    print("Hello, Raushan")

@timer    
def square(a):
    print(a**2)

@timer
def power(a,b):
    print(a**b)


power(4,2)