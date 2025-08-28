import math
def add(a,b):
    return a+b

def sub(a,b):
    if a>b:
        return a-b
    else:return b-a

def multi(a,b):
    return a*b

def div(a,b):
    if b!=0 :
        return a/b
    else: print("ERROR")

def power(a,b):
    return a**b

def mod(a,b):
    return a%b   # a>b

def cuberoot(a):
    return a**(1/3)

print(add(2,3))   # 5
print(sub(2,3))   # 1
print(multi(2,3)) # 6
print(div(2,3))   # 0.6667
print(power(2,3))  # 8
print(math.sqrt(36))  # 6
print(math.factorial(5))  # 120
print(mod(27,5))  # 2
print(cuberoot(27))  # 3
