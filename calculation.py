def get_addition(a,b):
    add = a + b
    print(f"Addition of {a} and {b} is {add}")
    return add


# here we created one function for multilication 
def get_multiplication(x,y):
    mul = x * y
    print(f"Multiplication of {x} and {y} is {mul}")
    return mul

if __name__ == "__main__":
    get_addition(10,20)
    get_addition(100,200)
    get_multiplication(4,7)