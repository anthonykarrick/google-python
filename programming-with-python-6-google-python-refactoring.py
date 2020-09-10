#how to take a sloppy python function and turn it into something simpler and more concise

def calculate(d):
    q = 3.14
    z = q * (d ** 2)
    print z

calculate(5)


#refactored

def circle_area(radius):
    pi = 3.14
    area = pi * (radius ** 2)
    print(area)

circle_area(5)