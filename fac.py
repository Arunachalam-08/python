def factorial(a):
    if a==0:
        return 1
    return a*factorial(a-1)
a=5
print(factorial(a))
