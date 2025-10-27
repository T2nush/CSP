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
turtle.register_shape("star", star_shape)

#---------------------------------------------------------
# Seting up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Large Galaxy Spiral")

#---------------------------------------------------------
#TURTLE Create
galaxy = turtle.Turtle()
galaxy.shape("star")
galaxy.speed(0)

#---------------------------------------------------------
#Color creator
colors = ["white", "yellow", "blue", "red", "pink"]


#---------------------------------------------------------
# My creating Custom function, tell to draw a star
def draw_star(size, color):
    galaxy.fillcolor(color)
    galaxy.begin_fill() 
    for _ in range(5):
        galaxy.forward(size)
        galaxy.right(145)  # Star angle ask mainhardt
    galaxy.end_fill()


#---------------------------------------------------------
#User question/input part
arms = int(screen.numinput("Galaxy Setting", "How many arms for the spiral", 5,2,12))
stars_for_each_per_arm = int(screen.numinput("Galaxy Settings", "How many stars for each arm?", 20, 5, 400))

#---------------------------------------------------------
#Galaxy Drawing 
for arm in range(arms):
    galaxy.penup()
    galaxy.home()
    galaxy.right((360 / arms) * arm)
    for star in range(stars_for_each_per_arm):
        galaxy.forward(10 + star * 5)
        color = random.choice(colors)
        size = random.randint(5,15)
        draw_star(size,color)

 # extra title
galaxy.penup()
galaxy.goto(-250,-250)
galaxy.color("white")
galaxy.write("Galaxy Creator", align="center", font=("Arial", 16, "bold"))

#----------------------------------------------------------
extra = screen.textinput("Extra Feature", "Would you like a planet with 67 in it? (yes/no")

if extra and extra.lower() == "yes":
#67 planet draw
    galaxy.penup()
    galaxy.goto(-150,-150)
    galaxy.pendown()
    galaxy.color("purple")
    galaxy.begin_fill()
    galaxy.circle(80)
    galaxy.end_fill()


#----------------------------------------------------------
#inside of planet finish
    galaxy.penup()
    galaxy.goto(-150, -70) #search how to move up in circle
    galaxy.color("white")
    galaxy.write("67", align="center", font=("Arial", 36, "bold"))
    galaxy.pendown()

galaxy.hideturtle()
screen.mainloop()
    
    # (-190, -95),      (-150, -70) , old coords