# TODO Start screen -> Open letter function (on click), send to next screen, give text input for user to insert their name then.  Nov 11
# TODO Name and age (to then get displayed at the end screen with the job profession image nov 12
# TODO Ask 10 questions, each leading up to the next, answers result in an output of a profession. Nov 12-13
# TODO Create generating code to fetch the jobs based on answers (takes 2 yeses in one category to funnel into 2 jobs, and 2 no’s in one subject to eliminate other choices). NOV 14 (consultancy protocol help)
# TODO Code to pick the job with the highest score 
# TODO Display final screen with job, name, picture of job and congratulate and then finiish the events

import turtle as turt
wn = turt.Screen()
pen = turt.Turtle()
#Letter part 
def start_screen():
    pen.penup()
    pen.goto(0,120)
    pen.pendown()
    pen.write("Hangman Game", align="center", font=("Arial", 25, "bold"))
    pen.penup()

def go_blue(x,y):
    wn.bgcolor("LightBlue")
    turtle_letter.hideturtle()
    # Text input/starting questions (name, age)
    name = wn.textinput("Welcome, Whats your name?")
    wn.textinput("Hi" + name + "!", "Lets play: What's your dream JOB! Anwser either yes or no")


turtle_letter = turt.Turtle()
turtle_letter.onclick(go_blue)
wn.setup(width=600, height=600)
normal_letter = "blueletter.gif"
wn.addshape(normal_letter)
turtle_letter = turt.Turtle()
turtle_letter.shape(normal_letter)
#-------------------------------------------------------
#set up scores/job images and jobs (use gif convert at end(on doc))
jobs = ["Doctor","Artist","Engineer","Astronaut", "Teacher","Athlete","Firefighter","Chef"]

job_pics = {
    "Doctor":"doctor.gif",
    "Artist":"artist.gif",
    "Engineer":"engineer.gif",
    "Astronaut":"astronaut.gif",
    "Teacher":"teacher.gif",
    "Athlete":"athlete.gif",
    "Firefighter":"firefighter.gif",
    "Chef":"chef.gif"
}
# Make the pics 
for pic in job_pics.values():
    try: 
        wn.addshape(pic)
    except:
        pass 
#-------------------------------------------------------
#scoring for jobs and how they are decided
scores = {job: 0 for job in jobs}
#questions
q1 = wn.textinput("Question 1","Do you enjoy helping your community? (yes/no)")
if q1 = "yes":
                                                                                                










