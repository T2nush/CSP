# TODO Start screen -> Open letter function (on click), send to next screen, give text input for user to insert their name then.  Nov 11
# TODO Name and age (to then get displayed at the end screen with the job profession image nov 12
# TODO Ask 10 questions, each leading up to the next, answers result in an output of a profession. Nov 12-13
# TODO Create generating code to fetch the jobs based on answers (takes 2 yeses in one category to funnel into 2 jobs, and 2 no’s in one subject to eliminate other choices). NOV 14 (consultancy protocol help)
# TODO Code to pick the job with the highest score 
# TODO Display final screen with job, name, picture of job and congratulate and then finiish the events

import turtle as turt
wn = turt.Screen()
pen = turt.Turtle()
wn.title("Dream Job Finder")
#Letter part 
turtle_letter = turt.Turtle()
normal_letter = "blueletter.gif"
wn.addshape(normal_letter)

turtle_letter = turt.Turtle()
turtle_letter.shape(normal_letter)
turtle_letter.penup()
pen = turt.Turtle()
pen.hideturtle()
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

def go_blue(x,y):
    wn.bgcolor("LightBlue")
    turtle_letter.hideturtle()
    pen.clear()

    # Text input/starting questions (name, age)
name = wn.textinput("Welcome", "Whats your name?")
wn.textinput("Hi" + name + "!", "Whats your dream JOB Anwser yes or no")
if not name: 
    name = "Friend"

# \n\n point for break for when new line displayed(write in doc)
pen.clear()
pen.penup()
pen.goto(0, 0)
message = f"Hi {name} Let's find your dream job!\n\nClick OK to start answering questions."
pen.write(message, align="center", font=("Arial", 18, "bold"))

#-------------------------------------------------------
#scoring for jobs and how they are decided
scores = {job: 0 for job in jobs}

#questions
q1 = wn.textinput("Question 1","Do you enjoy helping your community? (yes/no)")
if q1 == "yes":
    scores["Doctor"] += 2
    scores["Firefighter"] += 1
q2 = wn.textinput("Question 2","Do you enjoy drawing or making art? (yes/no)")
if q2 == "yes":
    scores["Artist"] += 2
    scores["Chef"] += 1
q3 = wn.textinput("Question 3","Do you like building or fixing things? (yes/no)")
if q3 == "yes":
    scores["Engineer"] += 2
    scores["Astronaut"] += 1
q4 = wn.textinput("Question 4","Do you like stars or spaceships? (yes/no)")
if q4 == "yes":
    scores["Astronaut"] += 2
    scores["Engineer"] += 1
q5 = wn.textinput("Question 5","Do you like teaching or even helping other peoole learn stuff you know? (yes/no)")
if q5 == "yes":
    scores["Teacher"] += 2
    scores["Doctor"] += 1
q6 = wn.textinput("Question 6","Do you like baking or cooking? (yes/no)")
if q6 == "yes":
    scores["Chef"] += 2
    scores["Artist"] += 1
q7 = wn.textinput("Question 7","Do you like sports? (yes/no)")
if q7 == "yes":
    scores["Athlete"] += 2
    scores["Firefighter"] += 1
q8 = wn.textinput("Question 8","Do you like solving hard problems or doing experiments ? (yes/no)")
if q8 == "yes": 
    scores["Engineer"] += 2
    scores["Doctor"] += 1
q9 = wn.textinput("Question 9","Do you like protecting nature or animals? (yes/no)")
if q9 == "yes":
    scores["Doctor"] += 2
    scores["Firefighter"] += 1
q10= wn.textinput("Question 10","Do you enjoy being creative and testing out new ideas? (yes/no)")
if q10 == "yes":
    scores["Artist"] += 2
    scores["Engineer"] += 1

#highest score
best_job = max(scores, key=scores.get)

#final screen
wn.clear
wn.bgcolor("lightyellow")

#name display and age 
name_writer = turt.Turtle()
name_writer.hideturtle()
name_writer.penup()
name_writer.goto(-350,250)
name_writer.write(f"Name:{name}", align="left", font=("Arial", 16, "bold"))

#-------------------------------------------------------
#job images 
pic = job_pics.get(best_job)
job_turtle = turt.Turtle()
job_turtle.penup()
job_turtle.goto(0,-50)
if pic:
    job_turtle.shape(pic)
else:
    job_turtle.hideturtle()
    job_turtle.write("(Image Missing)",
align = "center", font=("Arial",12,"normal"))
    
#job title 



                  
                                                                                                










