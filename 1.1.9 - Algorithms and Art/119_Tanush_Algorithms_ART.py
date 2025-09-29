import turtle
import random

# Seting up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Large Galaxy Spiral")

#---------------------------------------------------------
# Turtle Custom create
galaxy = turtle.Turtle()
galaxy.shape("turtle")
galaxy.speed(0)  


#---------------------------------------------------------
#Color creater
colors = ["white", "yellow", "lightblue", "violet", "pink"]


#---------------------------------------------------------
# My crteating Custom function: tell to draw a star
def draw_star(size, color):
    galaxy.fillcolor(color)
    galaxy.begin_fill()
    for _ in range(5):
        galaxy.forward(size)
        galaxy.right(144)  # Star angle ask mainhardt
    galaxy.end_fill()


#---------------------------------------------------------
#User question/input part
arms = int(screen.numinput("galaxy setting", "How many arms for the spiral", 5,2,10))