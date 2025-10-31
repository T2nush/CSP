# Project 1.2.5 Hangman with hidden number guessing and one superpower
# Clean version with hanger, improved layout, and interactive guessing

#TODO Start screen asking for difficulty, (Only options are hard, and extremely hard) finish by OCT 29
#TODO #Setting up word, draw short line for each letter, each line has a letter the user guessed on top of it. Lives represented with head, body, left arm, right arm, left leg, right leg, and powerups if you run out to give a free letter. Finish by oct 29 also.
#TODO Set up extra feature, each guess user has, they can guess a letter and a number, numbers are randomized within the random word which is going to be 8-13 letters long. The words will be difficult to guess and long due to a feature Im adding giving the user a extra life/cutting off one of the body parts on the hangman if they guess the letter with the correct number below it (guessing). Finish by 30 ALSO, create word stuff.
# TODO #Create Superpower (only 1 option), gives back life if you are on your last life/right leg. Finish by oct 31
# TODO If all body parts are there, show lose screen Nov 1st or 2nd
# TODO If word guessed, show win screen nov 1st-3rd

import turtle
import random

#------------------------------------------------
# Config
WORD_LIST = [
    "LIGHTHOUSE", "RESPONSIBILITY", "UNDERGROUND",
    "CONSTITUTION", "ASTRONOMICAL", "ENVIRONMENTAL", "LOLLYGAG"
]
MIN_WORD_LEN = 8

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
HANGMAN_PARTS = ["head", "body", "left_arm", "right_arm", "left_leg", "right_leg"]
MAX_WRONG = len(HANGMAN_PARTS)

#------------------------------------------------
# Turtle setup
screen = turtle.Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.title("Hangman: Letter + Number Edition")

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)

# Game state
difficulty = None
word = ""
word_letters = []
guessed = []
number_map = {}
wrong_guesses = 0
superpower_used = False
buttons = {}

#------------------------------------------------
# Utility draw functions
def draw_text(x, y, text, size=20, color="black", align="center"):
    pen.penup()
    pen.goto(x, y)
    pen.color(color)
    pen.write(text, align=align, font=("Arial", size, "bold"))

def draw_hanger():
    pen.penup()
    pen.goto(200, -200)
    pen.pendown()
    pen.pensize(5)
    pen.goto(300, -200)  # base
    pen.goto(250, -200)
    pen.goto(250, 150)
    pen.goto(200, 150)
    pen.goto(200, 100)
    pen.penup()

#------------------------------------------------
# Start screen
def draw_start_screen():
    pen.clear()
    draw_text(0, 150, "Welcome to Hangman!", 36)
    draw_text(0, 100, "Choose Your Difficulty", 22)

    hard_btn = turtle.Turtle()
    hard_btn.penup()
    hard_btn.shape("square")
    hard_btn.shapesize(2, 8)
    hard_btn.fillcolor("lightgreen")
    hard_btn.goto(-150, 0)
    hard_btn.write("HARD", align="center", font=("Arial", 16, "bold"))
    hard_btn.onclick(lambda x, y: start_game("hard"))

    extreme_btn = turtle.Turtle()
    extreme_btn.penup()
    extreme_btn.shape("square")
    extreme_btn.shapesize(2, 8)
    extreme_btn.fillcolor("orange")
    extreme_btn.goto(150, 0)
    extreme_btn.write("EXTREMELY HARD", align="center", font=("Arial", 14, "bold"))
    extreme_btn.onclick(lambda x, y: start_game("extreme"))

#------------------------------------------------
# Start game setup
def start_game(selected_difficulty):
    global difficulty, word, word_letters, guessed, number_map, wrong_guesses
    difficulty = selected_difficulty
    wrong_guesses = 0

    # Hide old turtles
    for t in screen.turtles():
        if t != pen:
            t.hideturtle()
            t.clear()

    pen.clear()
    draw_hanger()

    # Pick word
    word = random.choice([w for w in WORD_LIST if len(w) >= MIN_WORD_LEN])
    word_letters = list(word)
    guessed = ["_"] * len(word_letters)
    number_map = {i: random.randint(1, 9) for i in range(len(word_letters))}

    draw_word()
    draw_buttons()
    draw_text(0, 230, f"The word has {len(word_letters)} letters.", 18, "darkblue")
    draw_text(0, -240, "Click a letter, then enter a number (1-9) in the console.", 14, "black")

#------------------------------------------------
# Draw alphabet buttons
def draw_buttons():
    letters = [
        "A","B","C","D","E","F","G","H","I","J","K","L","M",
        "N","O","P","Q","R","S","T","U","V","W","X","Y","Z"
    ]
    start_x, start_y = -350, -160  # moved up a bit
    x, y = start_x, start_y
    for i, letter in enumerate(letters):
        btn = turtle.Turtle()
        btn.penup()
        btn.shape("square")
        btn.shapesize(1.5, 1.5)
        btn.fillcolor("lightblue")
        btn.speed(0)
        btn.goto(x, y)
        btn.write(letter, align="center", font=("Arial", 12, "bold"))
        buttons[letter] = btn

        x += 40
        if (i + 1) % 10 == 0:
            x = start_x
            y -= 45
        btn.onclick(on_click)

#------------------------------------------------
# Draw word blanks
def draw_word():
    pen.penup()
    pen.goto(-300, 100)
    spacing = 40
    for i, ch in enumerate(guessed):
        pen.goto(-300 + i * spacing, 100)
        pen.write(ch, font=("Arial", 24, "bold"))

#------------------------------------------------
# Draw hangman parts
def draw_hangman():
    pen.pensize(3)
    if wrong_guesses >= 1:  # Head
        pen.penup(); pen.goto(200, 75); pen.pendown(); pen.circle(25)
    if wrong_guesses >= 2:  # Body
        pen.penup(); pen.goto(200, 75); pen.pendown(); pen.goto(200, -25)
    if wrong_guesses >= 3:  # Left arm
        pen.penup(); pen.goto(200, 50); pen.pendown(); pen.goto(170, 20)
    if wrong_guesses >= 4:  # Right arm
        pen.penup(); pen.goto(200, 50); pen.pendown(); pen.goto(230, 20)
    if wrong_guesses >= 5:  # Left leg
        pen.penup(); pen.goto(200, -25); pen.pendown(); pen.goto(170, -70)
    if wrong_guesses >= 6:  # Right leg
        pen.penup(); pen.goto(200, -25); pen.pendown(); pen.goto(230, -70)

#------------------------------------------------
# Handle clicking letters
def on_click(x, y):
    global wrong_guesses, superpower_used
    for letter, btn in buttons.items():
        if btn.distance(x, y) < 20:
            btn.fillcolor("gray")
            btn.onclick(None)

            # Ask player for number guess
            try:
                number_guess = int(screen.textinput("Number Guess", f"Enter your number (1–9) for {letter}:"))
            except:
                draw_text(0, -280, "Invalid number!", 14, "red")
                return

            # Check if letter is in word
            if letter in word_letters:
                letter_indices = [i for i, l in enumerate(word_letters) if l == letter]
                success = False
                for i in letter_indices:
                    if number_map[i] == number_guess:
                        guessed[i] = letter
                        success = True
                if success:
                    draw_text(0, -280, "✅ Correct number + letter combo! Extra life earned!", 14, "green")
                    if wrong_guesses > 0:
                        wrong_guesses -= 1  # bonus life
                else:
                    draw_text(0, -280, "Correct letter but wrong number!", 14, "orange")
                draw_word()
            else:
                wrong_guesses += 1
                draw_hangman()

            # Superpower on last life
            if wrong_guesses == MAX_WRONG - 1 and not superpower_used:
                superpower_used = True
                wrong_guesses -= 1
                draw_text(0, -300, "Superpower Activated! You got an extra life!", 16, "green")

            # Win / Lose
            if "_" not in guessed:
                draw_text(0, -250, "🎉 YOU WIN! 🎉", 28, "blue")
                disable_buttons()
            elif wrong_guesses >= MAX_WRONG:
                draw_text(0, -250, f"💀 GAME OVER 💀 The word was {word}", 20, "red")
                disable_buttons()

def disable_buttons():
    for b in buttons.values():
        b.onclick(None)

#------------------------------------------------
# Start program
draw_start_screen()
turtle.done()
