# TODO Start screen -> Open letter function (on click), send to next screen, give text input for user to insert their name then.  Nov 11
# TODO 
# TODO 
# TODO
# TODO
# TODO

import turtle as turt
wn = turt.Screen()

#Letter part 
wn.screen.textinput("Click the Envelope!")
wn.setup(width=600, height=600)
normal_letter = "blueletter.gif"
wn.addshape(normal_letter)
turtle_letter = turt.Turtle()
turtle_letter.shape(normal_letter)
def go_blue(x,y):
    wn.bgcolor("LightBlue")
    turtle_letter.hideturtle()
turtle_letter.onclick(go_blue)
#-------------------------------------------------------
# Text input/starting questions (name, age




wn.mainloop()









