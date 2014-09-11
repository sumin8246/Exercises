# it was an in-class exercise

d1 = input("what is your vector 1? ")
d2 = input("what is your vector 2? ")


def magnitude(a):
    import math
    mag = math.sqrt(a[0]**2+a[1]**2+a[2]**2)
    return mag

def dot_product(a,b):
    c = a[0]*b[0] + a[1]*b[1] + a[2]*b[2]
    return c


print magnitude(d1)
print magnitude(d2)
print dot_product(d1,d2)
