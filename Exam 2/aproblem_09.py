def myfunc(x):
    a = 1
    print(x)

a = 5
myfunc(a)
print(a)

"""
a in myfunc is a local variable and will not influence the a outside. '5\n5' is printed out.
"""