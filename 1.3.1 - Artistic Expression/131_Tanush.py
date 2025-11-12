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

def open_letter(x,y):
    wn.bgcolor("lightblue")
    turtle_letter.hideturtle()
''''
def go_blue(x,y):
    wn.bgcolor("LightBlue")
    turtle_letter.hideturtle()
turtle_letter.onclick(go_blue)
'''
#-------------------------------------------------------
# Text input/starting questions (name, age)
name = wn.textinput("Welcome", "Whats your name?")
wn.textinput("Hi" + name + "!", "Lets play: What's your dream JOB! Anwser either yes or no")

#set up scores/job images and jobs (use gif convert at end(on doc))
jobs = [Doctor,]
wn.mainloop()









