#triangle callback function 

def area_triangle(base, height):
    return base*height/2


area_a = area_triangle(5,4)

area_b = area_triangle(7,3)

sum = area_a + area_b

print("the sumr of both areas is: " + str(sum))