def add(x, y, z):
    return x + y + z

res =add (1, 2, 3)
print(res)



def addition(z, *nums):
    total = sum(nums)

    total = 0
    for num in nums:
        total = total +num
    return total

def save(**dat):
    with open("values.txt", "w") as file:
        for key, value in dat.items():
            file.write(f"{key} : {value}\n")


def some_function(name, *scores, **details ):
    pass


def cylinder(r, h):

    """
    calculates the volume and the surface area of a cylinder

    parameters:
    radius and height of the cylinder
    :returns: volume and surface area of the cylinder


    """
    v=22/7 * r * r * h
    sa = 22/7 * r **2 *2 + 22/7 * r * 2 * h
    return sa, v

surf_area, volume = cylinder(7,15)

print(surf_area, volume)



sum([1,2,3,])



#lamda functions

divider = lambda x, y : x/y

area_circle = lambda r: 22/7 * r * r


print(divider(45,7))

res =area_circle(5)





# some_function("Hellen", 10,90,85, gender='Female',course ='Chem')


#save(age=18, dob='2001-12-31',profession = 'Engineer')

# save(dob='2025-01-18', gender='Female', color='Black',name='noah')


# print(addition(9, 10, 100, 67.88, 89, 56, 78))
# print(addition(90,100))



