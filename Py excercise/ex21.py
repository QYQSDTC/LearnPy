# define the mathe functions
def add(a,b):
    print(f"add {a} + {b}")
    return a + b

def substract(a,b):
    print(f"substract {a} - {b}")
    return a - b

def multiply(a,b):
    print(f"multiply {a} * {b}")
    return a * b

def divide(a,b):
    print(f"divide {a} / {b}")
    return a / b


print("Let's try our functions to do some mathe")
print("Input 2 number you like and them will define you.")
A = input("a >") # it is a str variable
B = input("b >")
a = float(A)
b = float(B)
age = add(a,b)
height = substract(a,b)
weight = multiply(a,b)
iq = divide(a,b)

print(f"Now here is my data. Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")


# here is a puzzle

print("Here is a puzzle")

what = add(age,substract(height,(multiply(weight,divide(iq,2)))))
print(f"It becomes: ",what,"Can you do it by hand?")
