from sys import exit
from random import randint

def death():
    quips = ["You died, You Kinda suck at this.", "Nice job, you died ...jackass.", "Such a loser", "I have a small puppy that's better at this than you"]
    
    print(quips[randint(0, len(quips)-1)])
    exit(1)
    
def central_corridor():
    print("The Gothons of Planet Percal #25 have invaded your ship and destroyed ")
    print("your entire crew. You are the last surviving member and your last ")
    print("mission is to get the neutron bomb from the Weapons Armoury, ")
    print("put it in the bridge, and blow the ship up after getting into an ")
    print("escape pod.")
    print("\n")
    print("You're running down the central corridor to the Weapons Armoury when ")
    print("a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume")
    print("flowing around his hate-filled body. He's blocking he door to the ")
    print("Armmoury and about to pull a weapon to blast you.")
    
    action = input("What are you going to do?")
    
    if action == "shoot":
        print("Quick on the draw you yank out your blaster and fire it at the Gothon.")
        print("His clown costume is flowing and moving around his body, which throws")
        print("off your aim. Your laser hits his costume but misses him entirely. The")
        print("completely ruins his brand new costume his mother bought him which")
        print("makes him fly inton an insane rage and blast you repeatedly in the face until")
        print("you are dead. Then he eats you.")
        return 'death'
    
    elif action =="dodge":
        print("Like a world class boxer you dodge, weave, slip and slide right")
        print("as the Gothon's blaster cranks a laser past your head.")
        print("In the middle of your artful dodge your foot slips and you")
        print("bang your head on the metal wall and pass out.")
        print("You wake up shortly after only to die as the Gothon stomps on")
        print("your head and eats you")
        return 'death'
        
    elif action == "tell a joke":
        print("Lucky for you they made you learn Gothon insults in the academy.")
        print("You tell the one Gothon joke you know:")
        print("Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, fur fvgf nebhaq gur ubhfr.")
        print("The Gothon stops, tries not to laugh, then bursts out laughing")
        print("While he's laughing you run up and shoot him square in the head")
        print("putting him down, then jump through the Weapoin Armoury door.")
        return 'laser_weapon_armoury'
    
    else:
        print("DOES NOT COMPUTE!")
        return 'central_corridor'
  
def laser_weapon_armoury():
    print("You do a dive roll into the Weapon Armoury, crouch and scan the room")
    print("for more Gothons that might be hiding. It's dead quiet, too quiet.")
    print("You stand up and run to the far side of a room and find the ")
    print("neutron bomb in its container. There's a keypad lock on the box")
    print("and you need te code to get the bomb out. If you get the code")
    print("wrong 10 times then the lock closes forever and you can't")
    print("get the bomb. The code is 3 digits.")
    code = "%d%d%d" (randint(1,9), randint(1,9), randint(1,9))
    guess = input("[keypad]> ")
    guesses = 0
    
    
    
 
    