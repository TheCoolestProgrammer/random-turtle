from turtle import *
import random
r = 0.0
g = 1.0
b = 0.0
r2 = 0
g2 = 0
b2 = 0
speed(13)
speed = 0.01
pensize(5)
setup(1280,720)
while True:

    color(r,g,b)
    a = random.randint(1,3)
    if a == 1:
        if r2 == 0:
            if round(r-speed,2) > 0.0:
                r = round(r - speed, 2)
            else:
                r2 = 1
        else:
            if round(r+speed,2) < 1.0:
                r = round(r+speed,2)
            else:
                r2 = 0
    if a == 2:
        if g2 == 0:
            if round(g-speed,2) > 0.0:
                g = round(g-speed,2)
            else:
                g2 = 1
        else:
            if round(g+speed,2) < 1.0:
                g = round(g+speed,2)
            else:
                g2 = 0
    if a == 3:
        if b2 == 0:
            if round(b-speed,2) > 0.0:
                b = round(b-speed,2)
            else:
                b2 = 1
        else:
            if round(b+speed,2) < 1.0:
                b = round(b+speed,2)
            else:
                b2 = 0

    a = random.randint(10,50)
    z = random.randrange(90,360,90)
    left(z)
    forward(a)
    #if xcor() > 1280:

# две спирали
# for i in range(2000):
#     right(179)
#     forward((i**2)//2)

# 4 спирали
# for i in range(1,2000):
#     #left(125)
#     if i%2 == 0:
#         #forward(i)
#         right(181)
#     else:
#         left(90)
#     forward((i**2)//2)

# крутая звезда
# for i in range(1,2000):
#     right(225)
#     forward(200)
#     left(30)

#роза
# for i in range(1,2000):
#     left(123)
#     if i%2 == 0:
#         forward(i)
#     else:
#         left(47)

#нефиговая звезда
# for i in range(1,2000):
#     #left(125)
#     if i%2 == 0:
#         #forward(i)
#         right(128)
#     else:
#         left(77)
#     forward(i)

# красота
# for i in range(1,2000):
#     if i%2 == 0:
#         right(225)
#     else:
#         left(99)
#     forward(i)