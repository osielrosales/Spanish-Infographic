# Final Project
# CS 111, Hayes & Reckinger
# This program is intended has two main tabs, one meant to inform the user on the history of the Spanish language and another meant to provide resources on how to learn the Spanish language. The first tab contains a paragraph on the history. The second tab contains a diagnostic test that will test the user on their Spanish speaking abilities; outputting a list of resources if they are not proficient enough.

# Source for Spanish History: https://www.newsdle.com/blog/brief-history-of-spanish-language#:~:text=Spanish%20originated%20in%20the%20Iberian,spread%20around%20the%20world%20thereafter.

import turtle
import random
import time

# The following four functions are the different "tabs" contained in the program 
# This functions creates the starting screen of the program. It takes two inputs, x and y, which allows it to be called using an onclick function. This allows the user to return to the homescreen at any point they are prompted to. 
def homescreen(x, y):
    bg.clear()
    bg.bgpic("first_bg.gif")
    
    # Welcome messeges
    welcome = turtle.Turtle()
    welcome.penup()
    welcome.hideturtle()
    welcome.goto(0,200)
    welcome.write("Welcome!", False, align="center", font=("Courier", 20, "bold"))

    # Sets up the info tab turtle
    info_tab = turtle.Turtle()
    info_tab.penup()
    info_tab.goto(-200, -200) 
    info_tab.write("Click here to learn the history", False, align="center", font=("Courier", 14, "bold"))
    info_tab.goto(-210, -225)
    info_tab.shape("click_here.gif")

    # Sets up the larning tab turtle
    learn_tab = turtle.Turtle()
    learn_tab.penup()
    learn_tab.goto(200, -200)
    learn_tab.write("Click here to learn the language", False, align="center", font=("Courier", 14, "bold"))
    learn_tab.goto(210,-225)
    learn_tab.shape("click_here.gif")

    # On click events
    info_tab.onclick(infographic)
    learn_tab.onclick(starting_information)

# This function makes the infographcs tab when the user clicks the "learn the history" button.
def infographic(x, y):
    bg.clear()

    # Picture
    flags = turtle.Turtle()
    flags.penup()
    flags.hideturtle
    flags.goto(240, 0)
    flags.shape("flags.gif")

    q.goto(-170, 200)
    q.write("The History of Spanish", False, align="center", font=("Courier", 20, "bold"))

    q.goto(-170, 170)
    info = read_file("info.txt")
   
    x_val = 170
    for i in range(len(info)): # Prints each line of the list in paragraph form
        q.write(info[i], False, align="center", font=("Courier", 11))
        x_val -= 20
        q.goto(-175, x_val)

    # Creates the turtle that will return the user to the homescreen
    q.goto(-175, x_val - 25)
    q.write("Click to return to the homescreen", False, align="center", font=("Courier", 12, "bold"))
    return_t = turtle.Turtle()
    return_t.penup()
    return_t.hideturtle()
    return_t.goto(-175, x_val - 55)
    return_t.shape("click_here.gif")
    return_t.showturtle()
    return_t.onclick(homescreen)

# This function is what runs when the user clicks the "click to learn" button. It explains to the user the test they were about to take.
def starting_information(x, y):
    bg.clear()
    bg.bgpic("first_bg.gif")
    
    q.goto (0, 200)
    q.write("You are about to start a Spanish diognostic test where you will be", False, align="center", font=("Courier", 14, "bold"))
    q.goto(0, 160)
    q.write("given english words/sentances to translate to Spanish.", False, align="center", font=("Courier", 14, "bold"))
    q.goto(0,-200)
    q.write("The test will progressively get harder.", False, align="center", font=("Courier", 14, "bold"))

    timer = turtle.Turtle()
    timer.penup()
    timer.hideturtle()
    timer.goto(0,-240)
    for i in range(5, 0, -1): # Creates a 5 second timer that counts down from 5
        timer.write(str(i), False, align="center", font=("Courier", 20, "bold"))
        time.sleep(1)
        timer.clear()

    start_learning_game()

# This function is what outputs the quiz to the screen. 
def start_learning_game():
    bg.clear()
    bg.bgcolor("green")
    questions = read_file("questions.txt")
    create_bar()
    
    global bar_amt_moved 
    bar_amt_moved = 0

    global amt_right
    amt_right = 0
    
    # Loops through each question
    for i in range(0, int(len(questions)), 7):
        question = []
        question = questions[i:i+7] # Each question has this interval
        print_question(question)

        global right_answer 
        right_answer = question[-2] # Always the second to last in the list

        global diff_level
        diff_level = question[-1] # Always the last in the list

        global answered
        answered = False
        
        s = turtle.Screen()
        s.listen()
        s.onkey(chose_1, "1")
        s.onkey(chose_2, "2")
        s.onkey(chose_3, "3")
        s.onkey(chose_4, "4")

        stall = turtle.Turtle()
        stall.hideturtle()
        stall.penup()
        while answered == False: # Stalls the screen while the user answers the question
            stall.forward(5)
            stall.right(180)
            stall.forward(5)
            stall.right(180) 
    
    ending_screen()

# This functions outputs to the user the results of their diagnostics test. Depending on how the user did, they will either get links to help them with their Spanish, or a messege saying they are fluent. 
def ending_screen():
    global bar_amt_moved
    global amt_right
    bg.bgcolor("green")

    q.goto(0, 200)
    q.write("The test is finished", False, align="center", font=("Courier", 20, "bold"))
    q.goto(0,150)
    q.write("You got " + str(amt_right) + "/10 questions right", False, align="center", font=("Courier", 20, "bold")) 

    percent_fluent = (bar_amt_moved / 600) * 100 # Highest possible score is 600
    percent_fluent = "{:.2f}".format(percent_fluent)
    q.goto(0, -140) 
    q.write("You are " + percent_fluent + "% fluent", False, align="center", font=("Courier", 20, "bold"))

    time.sleep(5)
    bg.clear() # Clears for the next screen
    bg.bgcolor("green")     
    
    # The turtle that will return the user to the homescreen
    return_t = turtle.Turtle()
    return_t.penup()
    return_t.hideturtle()
    if bar_amt_moved < 450: # For users who get less than 75% fluent
        q.goto(0,200)
        q.write("Here are some links to help you learn Spanish:", False, align="center", font=("Courier", 17, "bold"))
        q.goto(0, 100)
        q.write("https://www.duolingo.com/course/es/en/Learn-Spanish", False, align="center", font=("Courier", 15, "bold"))
        q.goto(0,75)
        q.write("^ free! ^", False, align="center", font=("Courier", 15, "bold"))
        q.goto(0, 0)
        q.write("https://www.babbel.com/learn-spanish", False, align="center", font=("Courier", 15, "bold"))
        q.goto(0, -25)
        q.write("^ paid ^", False, align="center", font=("Courier", 15, "bold"))
        q.goto(0, -100)
        q.write("https://www.youtube.com/watch?v=qE-03EATjho", False, align="center", font=("Courier", 15, "bold"))
        q.goto(0, -125)
        q.write("^ Excellent video for visual learners ^", False, align="center", font=("Courier", 15, "bold"))

        q.goto(0, -200)
        q.write("Click to return to the homescreen", False, align="center", font=("Courier", 15, "bold"))

        return_t.goto(0, -230)
        return_t.showturtle()
        return_t.shape("click_here.gif")
        return_t.showturtle()
        return_t.onclick(homescreen) # Allows the user to return to the homescreen
    else: # For users higher than 75% fluent
        q.goto(0,200)
        q.write("You are already fluent in Spanish!", False, align="center", font=("Courier", 17, "bold"))
        q.goto(0,100)
        q.write("- You could still learn its history - ", False, align="center", font=("Courier", 17, "bold"))
        q.goto(0,0)
        q.write("Click to return to the homescreen", False, align="center", font=("Courier", 17, "bold"))
        
        return_t.goto(0, -50)
        return_t.showturtle()
        return_t.shape("click_here.gif")
        return_t.showturtle()
        return_t.onclick(homescreen)# Allows the user to return to the homescreen

# This function draws a simple rectangle shape with labels on either side.
def create_bar():
    # Creates rectangle
    b = turtle.Turtle()
    b.penup() 
    b.hideturtle()
    turtle.tracer(False)
    b.width(5)
    b.goto(-300, -150) 
    b.pendown()
    b.forward(600)
    b.right(90)
    b.forward(75)
    b.right(90)
    b.forward(600)
    b.right(90)
    b.forward(75)
    b.right(90)

    # Creates the labels
    b.penup()
    b.goto(-300, -145)
    b.write("Not fluent", font=("Courier", 10, "bold"))

    b.goto(250, -145)
    b.write("Fluent", font=("Courier", 10, "bold"))
    turtle.tracer(True)

# This function takes in the amount needed to move and displays an animation of the bar increasing.
def move_bar(amt_move):
    global bar_amt_moved
    bar_amt_moved += amt_move
    
    # Fills the bar red
    b_move.pencolor("red")
    b_move.fillcolor("red")
    
    # This for loop allows for the "animation" of the bar moving
    for i in range(0, amt_move):
        b_move.begin_fill()
        b_move.pendown()
        b_move.forward(5)
        b_move.right(90)
        b_move.forward(70)
        b_move.right(90)
        b_move.forward(5)
        b_move.right(90)
        b_move.forward(70)
        b_move.right(90)
        b_move.end_fill()

        b_move.forward(1)

# The following four functions are for the user's choice between asnwers. 
def chose_1(): # ANSWER 1
    global answered
    answered = True
    
    global right_answer
    global diff_level

    if "1" == right_answer:
        answer_right()
        if diff_level == "E": # Easy question
            move_bar(40)
        elif diff_level == "M": # Medium question
            move_bar(60)
        else: # Hard question
            move_bar(100)
    else:
        answer_wrong()

    q.clear()

def chose_2(): #ANSWER 2
    global answered
    answered = True
    
    global right_answer
    global diff_level

    if "2" == right_answer:
        answer_right()
        if diff_level == "E": # Easy question
            move_bar(40)
        elif diff_level == "M": # Medium question
            move_bar(60)
        else: # Hard question
            move_bar(100)
    else:
        answer_wrong()

    q.clear()

def chose_3(): # ANSWER 3
    global answered
    answered = True
    
    global right_answer
    global diff_level

    if "3" == right_answer:
        answer_right()
        if diff_level == "E": # Easy question
            move_bar(40)
        elif diff_level == "M": # Medium question
            move_bar(60)
        else: # Hard question
            move_bar(100)
    else:
        answer_wrong()

    q.clear()

def chose_4(): # ANSWER 4
    global answered
    answered = True
    
    global right_answer
    global diff_level

    if "4" == right_answer:
        answer_right()
        if diff_level == "E": # Easy question
            move_bar(40)
        elif diff_level == "M": # Medium question
            move_bar(60)
        else: # Hard question
            move_bar(100)
    else:
        answer_wrong()

    q.clear()

# This function will display a messege saying the user answered correctly. 
def answer_right():
    global amt_right
    amt_right += 1
    q.clear()
    q.penup()
    q.goto(0, 200)
    q.write("Correct!", False, align="center", font=("Courier", 20, "bold"))

# This function displays a messege saying the user answered incorrectly, alone with the correct answer.
def answer_wrong():
    global right_answer
    q.clear()
    q.penup()
    q.goto(-70, 200)
    q.write("Incorrect", font=("Courier", 20, "bold"))
    q.goto(-150, 170)
    q.write("The correct answer was " + str(right_answer), font=("Courier", 15, "bold"))
    
    time.sleep(3)

# This function will print the questions from the inputted list.
def print_question(question):
    q.goto(-350,200)
    q.write(question[0], font=("Courier", 20, "bold"))

    start_y = 125  
    for i in range(1,5): # Prints each question in a column
        q.goto(-350, start_y)
        q.write(question[i], font=("Courier", 17, "bold"))
        start_y -= 75

# This function takes in a file as an input and will turn it into a list with all the \n's removed.
def read_file(file):
    file = open(file)
    file_list = file.readlines()
    for i in range(len(file_list)):
        file_list[i] = file_list[i].strip()
    return file_list

# The bg screen turtle allows the program to change the background color and to clear everything on the screen. 
bg = turtle.getscreen()
bg.setup(width=800, height=550)
bg.addshape("click_here.gif")
bg.addshape("flags.gif")

# The q turtle is the primary text turtle used throughout this program
q = turtle.Turtle()
q.penup()
q.hideturtle()

# The b_move turtle is the turtle that allows for the animation of the bar
b_move = turtle.Turtle()
b_move.penup()
b_move.hideturtle()
b_move.speed("fastest")
b_move.goto(-300, -152) 

homescreen(0,0) # Allows the homescreen function to run when the code is executed
