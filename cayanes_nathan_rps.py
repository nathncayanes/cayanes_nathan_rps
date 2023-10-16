# This file was created by Nathan Cayanes on 9/19/23

'''
Goals - create images for paper and scissors
Write program so that user selects rock or paper or scissors when cliking on image...
'''

# import package
import turtle
from turtle import *
# The os module allows us to access the current directory in order to access assets
import os
import winsound
print("The current working directory is (getcwd): " + os.getcwd())
print("The current working directory is (path.dirname): " + os.path.dirname(__file__))

from random import randint

# setup the game folders using the os module
game_folder = os.path.dirname(__file__)
images_folder = os.path.join(game_folder, 'images')
sounds_folder = os.path.join(game_folder, 'sounds')

# Used this resource to include sound
# https://www.youtube.com/watch?v=w6g8PO-Pqp4
def play_rock():
    winsound.PlaySound(os.path.join(sounds_folder, 'rock.wav'), winsound.SND_ASYNC)
def play_paper():
    winsound.PlaySound(os.path.join(sounds_folder, 'paper.wav'), winsound.SND_ASYNC)
def play_scissors():
    winsound.PlaySound(os.path.join(sounds_folder, 'scissors.wav'), winsound.SND_ASYNC)

# setup the width and height for the window
WIDTH, HEIGHT = 1000, 400

rock_w, rock_h = 256, 280

paper_w, paper_h = 256, 204

scissors_w, scissors_h = 256, 170

player_choice = ""

cpu_choice = ""

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
rock_instance = turtle.Turtle()
cpu_rock_image = os.path.join(images_folder, 'cpu_rock.gif')
cpu_rock_instance = turtle.Turtle()

paper_image = os.path.join(images_folder, 'paper.gif')
paper_instance = turtle.Turtle()
cpu_paper_image = os.path.join(images_folder, 'cpu_paper.gif')
cpu_paper_instance = turtle.Turtle()

scissors_image = os.path.join(images_folder, 'scissors.gif')
scissors_instance = turtle.Turtle()
cpu_scissors_image = os.path.join(images_folder, 'cpu_scissors.gif')
cpu_scissors_instance = turtle.Turtle()

def show_rock(x,y):
    # add the rock image as a shape
    screen.addshape(rock_image)
    # attach the rock_image to the rock_instance
    rock_instance.shape(rock_image)
    # remove the pen option from the rock_instance so it doesn't draw lines when moved
    rock_instance.penup()
    # set the position of the rock_instance
    rock_instance.setpos(x,y)

def cpu_show_rock(x,y):
    screen.addshape(cpu_rock_image)
    cpu_rock_instance.shape(cpu_rock_image)
    cpu_rock_instance.penup()
    cpu_rock_instance.setpos(x,y)

def show_paper(x,y):
    screen.addshape(paper_image)
    paper_instance.shape(paper_image)
    paper_instance.penup()
    paper_instance.setpos(x,y)

def cpu_show_paper(x,y):
    screen.addshape(cpu_paper_image)
    cpu_paper_instance.shape(cpu_paper_image)
    cpu_paper_instance.penup()
    cpu_paper_instance.setpos(x,y)

def show_scissors(x,y):
    screen.addshape(scissors_image)
    scissors_instance.shape(scissors_image)
    scissors_instance.penup()
    scissors_instance.setpos(x,y)

def cpu_show_scissors(x,y):
    screen.addshape(cpu_scissors_image)
    cpu_scissors_instance.shape(cpu_scissors_image)
    cpu_scissors_instance.penup()
    cpu_scissors_instance.setpos(x,y)

text = turtle.Turtle()
text.color('navy blue')
text.hideturtle()

# this function uses the same random choice as we used with the original program without turtle but instead
# returns a choice that can be seen in turtle
def cpu_select():
    choices = ["rock", "paper", "scissors"]
    return choices[randint(0,2)]

# this function uses and x y value, an obj
def collide(x,y,obj,w,h):
    if x < obj.pos()[0] + w/2 and x > obj.pos()[0] -  w/2 and y < obj.pos()[1] + h/2 and y > obj.pos()[1] - h/2:
        return True
    else:
        return False

show_rock(-300,0)
show_paper(0,0)
show_scissors(300,0)

# function that passes through wn onlick
def mouse_pos(x, y):
    # print("it is " + str(collide(x,y,rock_instance,rock_w,rock_h)) +  " that I collided with rock")
    # print("it is " + str(collide(x,y,paper_instance,paper_w,paper_h)) +  " that I collided with paper")
    # print("it is " + str(collide(x,y,scissors_instance,scissors_w,scissors_h)) +  " that I collided with scissors")
    print(cpu_select())
    cpu_picked = cpu_select()
    if collide(x,y,rock_instance,rock_w,rock_h):
        print("I collided with rock...")
        text.setpos(-400,150)
        # this sets the coordinates for where the text should go
        text.write("you choose rock!", False, "left", ("Arial", 24, "normal"))
        # this creates a text box that appears in turtle displaying the choice, font, and font size
        play_rock()
        if cpu_picked == "rock":
            show_rock(-300,0)
            # set show_rock to where the original should go or in this case stay
            show_paper(0,-1000)
            # set show_paper to where you want paper to go
            show_scissors(1000,0)
            # set show_paper to where you want scissors to go
            cpu_show_rock(300,0)
            # you set cpu_show_rock to where you want the second image to appear
            text.clear()
            # hides the "you choose rock!" and "Choose rock or paper or scissors" text
            text.penup()
            text.setpos(0,150)
            text.write("its a tie, we go again", False, "left", ("Arial", 24, "normal"))
            # same as the one above
        elif cpu_picked == "paper":
        # follows the same pattern as the one above
            show_paper(0,-1000)
            show_scissors(1000,0)
            show_rock(-300,0)
            cpu_show_paper(300,0)
            text.clear()
            text.penup()
            text.setpos(0,150)
            text.write("no way you lost to a computer", False, "left", ("Arial", 24, "normal"))
        elif cpu_picked == "scissors":
        # follows the same pattern as the one above
            show_scissors(1000,0)
            show_paper(0,-1000)
            show_rock(-300,0)
            cpu_show_scissors(300,0)
            text.clear()
            text.penup()
            text.setpos(0,150)
            text.write("YOU WIN", False, "left", ("Arial", 24, "normal"))
    if collide(x,y,paper_instance,paper_w,paper_h):
    # does basically the same as the if statements above but sets the logic and "rules of the game"
    # for paper instead of rock
        print("I collided with paper")
        text.setpos(-400,150)
        text.write("you choose paper!", False, "left", ("Arial", 24, "normal"))
        play_paper()
        if cpu_picked == "rock":
            show_paper(0,-1000)
            show_rock(300,0)
            show_scissors(1000,0)
            cpu_show_paper(-300,0)
            text.clear()
            text.penup()
            text.setpos(0,150)
            text.write("YOU WIN", False, "left", ("Arial", 24, "normal"))
        elif cpu_picked == "paper":
            show_paper(-300,0)
            show_rock(-1000,0)
            show_scissors(1000,0)
            cpu_show_paper(300,0)
            text.clear()
            text.penup()
            text.setpos(0,150)
            text.write("its a tie, we go again", False, "left", ("Arial", 24, "normal"))
        elif cpu_picked == "scissors":
            show_scissors(300,0)
            show_rock(-1000,0)
            show_paper(-300,0)
            cpu_show_scissors(300,0)
            text.clear()
            text.penup()
            text.setpos(0,150)
            text.write("no way you lost to a computer", False, "left", ("Arial", 24, "normal"))
    if collide(x,y,scissors_instance,scissors_w,scissors_h):
    # does basically the same as the if statements above but sets the logic and "rules of the game"
    # for scissors instead of paper or scissors
        print("I collided with scissors")
        text.setpos(-400,150)
        text.write("you choose scissors!", False, "left", ("Arial", 24, "normal"))
        play_scissors()
        if cpu_picked == "rock":
            show_rock(-1000,0)
            show_paper(0,-1000)
            show_scissors(-300,0)
            cpu_show_rock(300,0)
            text.clear()
            text.penup()
            text.setpos(0,150)
            text.write("no way you lost to a computer", False, "left", ("Arial", 24, "normal"))
        elif cpu_picked == "paper":
            show_paper(-1000,0)
            show_rock(-1000,0)
            show_scissors(-300,0)
            cpu_show_paper(300,0)
            text.clear()
            text.penup()
            text.setpos(0,150)
            text.write("YOU WIN", False, "left", ("Arial", 24, "normal"))
        elif cpu_picked == "scissors":
            show_rock(-1000,0)
            show_paper(0,-1000)
            show_scissors(-300,0)
            cpu_show_scissors(300,0)
            text.clear()
            text.penup()
            text.setpos(0,150)
            text.write("its a tie, we go again", False, "left", ("Arial", 24, "normal"))
    else:
        print("bro missed")

screen.onclick(mouse_pos)
# runs mainloop for Turtle - required to be last  

text.penup()
text.setpos(0,150)
text.write("Choose rock or paper or scissors", False, "left", ("Arial", 24, "normal"))
text.setpos(72,320)
screen.mainloop()