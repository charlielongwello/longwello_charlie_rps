#This File was created by: Charlie Longwello

'''
Goals:
When a user click on their choice, the computer randomly chooses and displays the result 

Sources:
https://realpython.com/python-rock-paper-scissors/

'''

# import package
import turtle
from turtle import *


from random import randint
# The os module allows us to access the current directory in order to access assets
import os
print("The current working directory is (getcwd): " + os.getcwd())
print("The current working directory is (path.dirname): " + os.path.dirname(__file__))

# setup the game folders using the os module
game_folder = os.path.dirname(__file__)
images_folder = os.path.join(game_folder, 'images')

rps_choices = ["rock", "paper", "scissors"]

player = ""
CPU = ""

# setup the width and height for the window
WIDTH, HEIGHT = 1000, 400

rock_w, rock_h = 256, 280

paper_w, paper_h = 256, 204

scissors_w, scissors_h = 256, 170

# setup the Screen class using the turtle module
screen = turtle.Screen()
screen.setup(WIDTH + 4, HEIGHT + 8)  # fudge factors due to window borders & title bar
screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
screen.screensize(canvwidth=WIDTH, canvheight=HEIGHT, bg="lightblue")


# canvas object
cv = screen.getcanvas()
# hack to make window not resizable for more reliable coordinates
cv._rootwindow.resizable(False, False)


# setup the rock image using the os module as rock_image
rock_image = os.path.join(images_folder, 'rock.gif')
# instantiate (create an instance of) the Turtle class for the rock
rock_instance = turtle.Turtle()
# setup the paper image using the os module as paper_image
paper_image = os.path.join(images_folder, 'paper.gif')
# instantiate (create an instance of) the Turtle class for the paper
paper_instance = turtle.Turtle()
# setup the scissors image using the os module as scissors_image
scissors_image = os.path.join(images_folder, 'scissors.gif')
# instantiate (create an instance of) the Turtle class for the scissors
scissors_instance = turtle.Turtle()


def show_rock(x,y):
    # add the rock image as a shape
    screen.addshape(rock_image)
    # attach the rock_image to the rock_instance
    rock_instance.shape(rock_image)
    # remove the pen option from the rock_instance so it doesn't draw lines when moved
    rock_instance.penup()
    # set the position of the rock_instance
    rock_instance.setpos(x,y)

def show_paper(x,y):
    # add the paper image as a shape
    screen.addshape(paper_image)
    # attach the paper_image to the paper_instance
    paper_instance.shape(paper_image)
    # remove the pen option from the paper_instance so it doesn't draw lines when moved
    paper_instance.penup()
    # set the position of the paper_instance
    paper_instance.setpos(x,y)

def show_scissors(x,y):
    # add the scissors image as a shape
    screen.addshape(scissors_image)
    # attach the scissors_image to the scissors_instance
    scissors_instance.shape(scissors_image)
    # remove the pen option from the scissors_instance so it doesn't draw lines when moved
    scissors_instance.penup()
    # set the position of the scissors_instance
    scissors_instance.setpos(x,y)

# instantiate a turtle for writing text
text = turtle.Turtle()
text.color('deep pink')
text.hideturtle()
text.penup() 

show_rock(-300, 0)
show_paper(0, 0)
show_scissors(300, 0)

# this function uses and x y value, an obj, and width and height 
def collide(x,y,obj,w,h):
    if x < obj.pos()[0] + w/2 and x > obj.pos()[0] - w/2 and y < obj.pos()[1] + h/2 and y > obj.pos()[1] - h/2:
        return True
    else:
        return False

# function that passes through wn onlick



def mouse_pos(x, y):
    if collide(x,y,rock_instance, rock_w, rock_h):
        # This block of code determines what will happen when you chose rock
        print("rock")
        text.clear()
        # It wil type you chose rock if player chooses rock
        text.write("you chose rock!", False, "left", ("Arial", 24, "normal"))
        # this is the coordinates of what the opponent chooses
        text.goto(0,-150)
        # this determines what the CPU will chose and how it will type out
        text.write("Opponent picks " + str(rps_choices[randint(0, len(rps_choices)-1)]), False, "left", ("Arial", 24, "normal"))
        
    elif collide(x,y,paper_instance, paper_w, paper_h):
        print("paper")
        # this is the block of code that decifers what will happen if you chose rock
        text.clear()
        text.write("you chose paper!", False, "left", ("Arial", 24, "normal"))
        # the coordinates of where the text will be, same as rock       
        text.goto(0,-150)
        # this is the same as before, just the repeated steps
        text.write("Opponent picks " + str(rps_choices[randint(0, len(rps_choices)-1)]), False, "left", ("Arial", 24, "normal"))
    elif collide(x,y,scissors_instance, scissors_w, scissors_h):
        print("scissors")
        # moving on, all the same blocks of code just repeated for each choice
        text.clear()
        text.write("you chose scissors!", False, "left", ("Arial", 24, "normal"))
        text.goto(0,-150)
        # all of the wording is in the same place for each option
        text.write("Opponent picks " + str(rps_choices[randint(0, len(rps_choices)-1)]), False, "left", ("Arial", 24, "normal"))
    else:
        text.clear()
        # this is what happens if you dont click on anything
        text.write("you chose nothing bozo!!", False, "left", ("Arial", 24, "normal"))

text.setpos(0,130)
text.write("Do you chose Rock, Paper, or Scissors?", False, "left", ("Arial", 19, "normal"))
# had to use 19 size font so it can all fit on the screen



# user this to get mouse position
screen.onclick(mouse_pos)
# runs mainloop for Turtle - required to be last
screen.mainloop()

