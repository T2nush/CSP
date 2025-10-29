#Start screen asking for difficulty, (Only options are hard, and extremely hard) finish by OCT 29
# TODO #Setting up word, draw short line for each letter, each line has a letter the user guessed on top of it. Lives represented with head, body, left arm, right arm, left leg, right leg, and powerups if you run out to give a free letter. Finish by oct 29 also.
Set up extra feature, each guess user has, they can guess a letter and a number, numbers are randomized within the random word which is going to be 8-13 letters long. The words will be difficult to guess and long due to a feature Im adding giving the user a extra life/cutting off one of the body parts on the hangman if they guess the letter with the correct number below it (guessing). Finish by 30 ALSO, create word stuff.
# TODO #Create Superpower (only 1 option), gives back life if you are on your last life/right leg. Finish by oct 31
# TODO If all body parts are there, show lose screen Nov 1st or 2nd
# TODO If word guessed, show win screen nov 1st-3rd

# hangman_superpower.py
# Project 1.2.5 Hangman with number guess mechanic and one superpower

import turtle   
import random 

#---------------------------------------------
#Configuration part

Word_list = [ "LIGHTHOUSE", "RESPONSIBILITY", "UNDERGROUND", "CONSTITUTION", "ASTRONOMICAL", "ENVIRONMENTAL", "LOLLYGAG"]
MIN_WORD_LEN = 8

#screen set
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

#---------------------------------------------
#setting up the order to draw the body parts 
HANGMAN_PARTS = ["head", "body", "left_arm", "right_arm", "left_leg", "right_leg"] 
MAX_WRONG = len(HANGMAN_PARTS)

#---------------------------------------------
# Turtle setup area
screen = turtle.screen()
screen = 