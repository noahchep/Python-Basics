#functions
from idlelib.multicall import r
from turtledemo.chaos import h


def greet():
    print("Hello Welcome to Python")



def greeting(user):
    print(f"Hello {user}, Welcome to python")

greeting("Jim")
greeting("Ahmed")
greet()


def area_circle(radius, precision =3):
    a = 22/7 *radius * radius
    result =round(a, precision)

    print(result)

area_circle(2.9, 2)
area_circle(6.11, 0)
area_circle(8)


def volume_cylinder(r, h):
    v = 22/7 * r * r * h
    return v

print(volume_cylinder(8.5, 12.8))

res = volume_cylinder(6, 19)
print(round(res))






#named params
# area_circle(precision=2, radius=11)





