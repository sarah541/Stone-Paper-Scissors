#Stone-Paper-Scissors

# The key idea of this program is to equate the strings
# "stone", "paper", "scissors" to numbers
# as follows:
#
# 0 - stone
# 1 - paper
# 2 - scissors
import sys
import random
count = 0
s = 0
p = 0
q = 0
player_choice = ""
comp_choice = ""
import simplegui
def new_game():
    global count
    global s
    global p
    global q
    s = 0
    p = 0
    q = 0
    count = 0
    print "new game starts"
def name_to_number(name):
    
    if name == "stone":
        return 0
    elif name == "paper":
        return 1
    elif name == "scissors":
        return 2
    else:
        return  "Not a valid name, Try again"


def number_to_name(number):
  
    if number == 0:
        return "stone"
    elif number == 1:
        return "paper"
    elif number == 2:
        return "scissors"
    else:
        return "Not a valid number, Try again"
def stone():
    global player_choice
    player_choice = "stone"
    rpsls()
def paper():
    global player_choice
    player_choice = "paper"
    rpsls()
def scissors():
    global player_choice
    player_choice = "scissors"
    rpsls()

def draw(c):
    global count
    global s
    global p
    c.draw_line((150, 0), (150, 400), 5, 'Blue')
    c.draw_line((390, 0), (390, 400), 5, 'Blue')
    c.draw_text("You", [50,100], 48, "Blue")
    c.draw_text("Computer", [180,100], 48, "Blue")
    c.draw_text("Ties", [430,100], 48, "Blue")
    c.draw_text(str(s), (250, 200), 36, "White")
    c.draw_text(str(p), (80, 200), 36, "White")
    c.draw_text(str(q), (450, 200), 36, "White")
    c.draw_text(comp_choice, [190,150], 48, "Lime")

    if count == 5:
        if s > p:
            c.draw_text("GAME OVER",(160,300), 36, "Red")
            c.draw_text("Computer Wins!",(150,350), 36, "Red")
        elif p > s:
            c.draw_text("GAME OVER",(40,300), 36, "Red")
            c.draw_text("  You    Win!",(40,350), 36, "Red")
        elif s == p:
            c.draw_text("GAME OVER",(390,300), 36, "Red")
            c.draw_text("It's a tie!",(420,350), 36, "Red")

    

def rpsls():
    global count
    global s
    global p
    global q
    
    if(count <= 4):
        global player_choice
        global comp_choice
        print ""
        print  ("Player's choice is:" + player_choice)
        player_number = name_to_number(player_choice)
        comp_number = random.randrange(0,3)
        comp_choice  = number_to_name(comp_number)
        print ("computer's choice is:" + comp_choice)
        x = (comp_number - player_number)
    
        if (player_choice == "stone"):
            if (comp_choice  == "paper"):
                print "Computer is the winner"
                s = s + 1
            elif (comp_choice  == "scissors"):
                print "You are the winner"
                p = p + 1
            elif (comp_choice  == "stone"):
                print "It's a tie"
                q = q + 1
        elif (player_choice == "paper"):
            if (comp_choice  == "scissors"):
                print "Computer is the winner"
                s = s + 1
            elif (comp_choice  == "stone"):
                print "You are the winner"
                p = p + 1
            elif (comp_choice  == "paper"):
                print "It's a tie"
                q = q + 1
        if (player_choice == "scissors"):
            if (comp_choice  == "stone"):
                print "Computer is the winner"
                s = s + 1
            elif (comp_choice  == "paper"):
                print "You are the winner"
                p = p + 1
            elif (comp_choice  == "scissors"):
                print "It's a tie"
                q = q + 1
    if (count == 5):
        if (s>p):
            print ("GAME OVER \n COMPUTER WINS")
        elif (p > s):
            print ("GAME OVER \n YOU WIN")
        elif (s == p):
            print ("GAME OVER \n IT'S A TIE")
    count = count + 1            
        

frame = simplegui.create_frame("Guess The Number",600,400)
frame.add_button("NEW GAME",new_game,150)
frame.add_button("Stone",stone,100)
frame.add_button("Paper",paper,100)
frame.add_button("Scissors",scissors,100)
frame.set_draw_handler(draw)
frame.start()
