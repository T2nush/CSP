import turtle
import random

#Create Turtle
star_shape = (
(0, 0),
(10, 40),
(20, 0),
 (-10, 25),
(30, 25),
)


# Seting up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Large Galaxy Spiral")

#---------------------------------------------------------


#---------------------------------------------------------
#Color creator
colors = ["white", "yellow", "lightblue", "violet", "pink"]


#---------------------------------------------------------
# My crteating Custom function, tell to draw a star
def draw_star(size, color):
    galaxy.fillcolor(color)
    galaxy.begin_fill() 
    for _ in range(5):
        galaxy.forward(size)
        galaxy.right(145)  # Star angle ask mainhardt
    galaxy.end_fill()


#---------------------------------------------------------
#User question/input part
arms = int(screen.numinput("galaxy setting", "How many arms for the spiral", 5,2,10))
stars_for_each_per_arm = int (screen.numinput)



#Galaxy Drawing 
