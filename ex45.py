from sys import exit
from textwrap import dedent


flashlight = False

first_start = True

first_gate = True

first_house_area = True
first_house = True
first_house_window = True
first_east_room = True
first_west_room = True
key = True
reveal_rooms = False

first_woods = True
first_open_field = True
notice_gun = False
gun = False

first_shack_area = True
first_shack = True
carpet = True
hatch = True
first_basement = True
first_card_room = True
keycard = False

def start_room():
    global first_start
    global flashlight
    good = True
    
    if first_start:
        print("What will you do?")
        first_start = False
    elif first_start == False:
        print("Starting room")
    
    
    while good: 
        ## whenever take bullets and press enter it does the function but 
        ## when you type something after it wont register. So have to type again
        ## Its the same with the flashlight.
            
        choice = input("> ")
            
        if (choice == "pick up flashlight" or choice == "take flashlight") and flashlight == False:
            flashlight = True
            
            print("taken")
            
        
        elif (choice == "pick up flashlight" or choice == "take flashlight") and flashlight == True:
            print("You already have the flashlight.")
            
            
        elif choice == "go north" or choice == "walk north":
            gate()
        
        elif choice == "go south" or choice == "walk south":
            house_area()
            
        elif choice == "go east" or choice == "walk east":
            shack_area()
            
        elif choice == "go west" or choice == "walk west":
            woods()
        
        elif choice == "look around":
            print(dedent("""
            Trees around you have slashes on them and it gives you 
            an eerie feeling. You look around and there are 
            paths north, south, east and west.
            """))
        else:
            print("I dont know what that means")
        
        
            
            

def gate():
    global first_gate
    global keycard
    good = True
    if first_gate:
        print(dedent("""
        You walk north and there is a wall about 15ft 
        made out of concrete. There is a door but it 
        is locked. It seems that you need to swipe a
        keycard do unlock the door. Where the keycard
        is you have no idea. You can't go north, east,
        west. The only way you could go is back south.
        """))
        
        first_gate = False
    else:
        print("Gate")
    while good:
        choice = input("> ")
        if choice == "go south" or choice == "walk south":
            start_room()
        elif choice == "look around":
            print(dedent("""
            The big wall is still there and you need
            the keycard to get through the door. 
            Good luck with that. The only way you 
            could go is south.
            """))
            
        elif ((choice == "use keycard") or (choice == "swipe keycard")) and keycard == False:
            print("What keycard. Go find it.")
            
        elif ((choice == "use keycard") or (choice == "swipe keycard")) and keycard:
            ending()
            
        elif (choice == "go north") or (choice == "go west") or (choice == "go east"):
            print("Can't go that way dummy.")
            
        else:
            print("I dont know what that means.")
            
        
    

def house_area():
    global first_house_window
    global first_house_area
    good = True
    if first_house_area:
        print(dedent("""
        You walk south and see what seems to be an
        abandoned house. You go up to the front door
        and it's locked. There's a cracked window
        that leads to inside the house. There is 
        a forest all around you except from the 
        way you came, north.
        """))
        first_house_area = False
    else:
        print("House")
    
    while good:
        choice = input("> ")
        
        if choice == "go north" or choice == "walk north":
            start_room()
            
        elif (choice == "look around") and first_house_window:
            print(dedent("""
            The house has a cracked window which seems 
            like you could break. *COUGH* *COUGH*
            The only path is to the north.
            """))
        
        elif (choice == "look around") and first_house_window == False:
            print(dedent("""
            The house has the broken window for you to
            enter in. The only path is to the north.
            """))
        
        elif (choice == "go south") or (choice == "go east") or (choice == "go west"):
            print("You can't go that way dum dum.")
            
        elif ((choice == "break window") or (choice == "smash window")) and first_house_window:
            print(dedent("""
            You elbow the window the way Tyrese Gibson did in
            2 Fast 2 Furious. There is enough space for you
            to enter the house.
            """))
            first_house_window = False
        
        elif ((choice == "break window") or (choice == "smash window")) and first_house_window == False:
            print("You alread broke the window dummy.")
            
        elif (choice == "enter house") or (choice == "climb in"):
            house()
        
        
        else:
            print("I don't know what that means")
    
def house():
    global first_house
    global flashlight
    global reveal_rooms
    good = True
    if first_house:    
        print(dedent("""
        You enter the house and it's so dark that you 
        cant see anything. It would be impossible to
        traverse the house without a flashlight.
        """))
        first_house = False
    else:
        print("Inside of the house")
        
    while good:
        choice = input("> ")
        if ((choice == "use flashlight") or (choice == "turn on flashlight")) and flashlight:
            print(dedent("""
            You look around and see a huge mess everywhere.
            Everything is broken but there seems that there
            might be something useful in this house. There
            are rooms to the east and west.
            """)) 
            reveal_rooms = True
        elif ((choice == "use flashlight") or (choice == "turn on flashlight")) and flashlight == False:
            print("What flashlight do you have dummy.")
        
        elif (choice == "leave house") or (choice == "exit house"):
            house_area()
        
        elif ((choice == "go north") or (choice == "go south") or (choice == "go east") or (choice == "go west")) and flashlight == False:
            print("You cant see where you're going dummy.")
            print("You need a flashlight.")
        
        elif (choice == "go east") and flashlight and reveal_rooms:
            east_room()
        
        elif (choice == "go west") and flashlight and reveal_rooms:
            west_room()
        
        elif (choice == "go east") and flashlight and reveal_rooms == False:
            print("Turn on or use your flashlight")
        
        elif (choice == "go west") and flashlight and reveal_rooms == False:
            print("Turn on or use your flashlight")
            
        elif (choice == "look around") and flashlight:
            print(dedent("""
            You look around and see a hugh mess everywhere.
            Everything is broken but there seems that there
            might be something useful in this house. There
            are rooms to the east and west.
            """))
        
        elif (choice == "look around") and flashlight == False:
            print("Its to dark to see. You can leave when you want.")
            
        else:
            print("I dont know what that means.")

def east_room():
    global first_east_room
    global key
    good = True
    
    if first_east_room:
        print(dedent("""
        You enter the room and it seems like a little
        girl used to live here. The walls are pink 
        and the bed has a dirty Frozen blanket on it. 
        As you wave your flashlight around you notice 
        a shiny object and you get closer to it and 
        figure out it's a key. The only way to go is
        west.
        """))
    else:
        print("Little Girls Room")
        
    while good:
        choice = input("> ")
        if ((choice == "take key") or (choice == "pick up key")) and key:
            print("Taken")
            key = False
        elif ((choice == "take key") or (choice == "pick up key")) and key == False:
            print("You already have the key dumbo.")
        
        elif (choice == "go west") or (choice == "walk west"):
            house()
        
        elif choice == "look around" and key:
            print(dedent("""
            Your in a little girls room that has a 
            key in it WHICH YOU SHOULD PROBABLY
            TAKE! There is a door west of you.
            """))
        
        elif choice == "look around" and key == False:
            print("Just a girls room with a door west of you")
        
        else:
            print("I dont know what that means.")

def west_room():
    global first_west_room
    good = True
    
    if first_west_room:
        print(dedent("""
        You enter the room and it seems like a little
        boys room. The walls are a blue color and 
        there's a Avengers blanket on the bed. You 
        wave your flashlight around and notice 
        nothing special about this room. The only
        way to go is east.
        """))
    else:
        print("Little boys room")

    while good:
        choice = input("> ")
        if (choice == "go east") or (choice == "walk east"):
            house()
        elif choice == "look around":
            print(dedent("""
            It's just a boys room. There's nothing 
            special about this room. So go east to 
            leave.
            """))
        
        elif choice == "go south" or choice == "go north" or choice == "go west":
            print("You cant go that way.")
            
        else: 
            print("I dont know what that means.")

def woods():
    global first_woods
    good = True
    if first_woods:
        print(dedent("""
        You walk west and find yourself deep in the forest.
        You hear noises and feel some dark presence in the
        forest. You start to think that you are being 
        watch. There is a path south of where you are and
        the path you just came from, east.
        """))
        first_woods = False
        
    else:
        print("Woods")
    
    while good:
        choice = input("> ")
        
        if choice == "go east" or choice == "walk east":
            start_room()
            
        elif choice == "go south" or choice == "walk south":
            open_field()
            
        elif choice == "look around":
            print(dedent("""
            You're currently deep in the woods and you
            have a feeling you're being watched. The
            only paths are south and east to where
            you came.
            """))
            
        elif (choice == "go north") or (choice == "go west"):
            print("Wrong way dum dum")
            
        else:
            print("I dont know what that means.")
            
    

def open_field():
    global first_open_field
    global gun
    global notice_gun
    good = True
    
    if first_open_field:
        print(dedent("""
        You walk south of the woods and arrive at an open
        field of grass. A few miles away is the wall 
        surrounding the entire area you're in. There 
        seems to be nothing around but grass around you.
        The only path is back north.
        """))
        
        first_open_field = False
    else:
        print("Open Field")
    
    
    
    while good:
        choice = input("> ")
        if choice == "go north" or choice == "walk north":
            woods()
            
        elif choice == "look around":
            print(dedent("""
            You look around and notice what seems to
            be a gun on the floor. It also
            has a bullet in it. Theres only a 
            path to the north.
            """))
            notice_gun = True
            
        elif (choice == "take gun" or choice == "pick up gun") and notice_gun:
            gun = True
            print("taken")
        
        elif (choice == "take gun" or choice == "pick up gun") and notice_gun == False:
            print("What gun?")
        
        else:
            print("I dont know what that means.")
            
        
    
    

def shack_area():
    global first_shack_area
    good = True
    if first_shack_area:
        print(dedent("""
        As you walk east you see a small litle shack in the 
        distance. When you get to the shack you see that 
        there is no door to the shack. There seens to be 
        nothing wrong with the shack. The only path
        around you is the path you took to get to the 
        shack, west.
        """))
        first_shack_area = False
    else:
        print("Shack Area")
    
    while good:
        choice = input("> ")
        
        if choice == "go west" or choice == "walk west":
            start_room()
            
        elif choice == "look around":
            print(dedent("""
            The shack has no door. Maybe you should
            go in. Dumb dumb. The only path is to 
            the west.
            """))
            
        elif (choice == "go north") or (choice == "go east") or (choice == "go south"):
            print("No not that way silly.")
         
        elif (choice == "go in shack") or (choice == "enter shack"):
            shack()
        
        else:
            print("I dont know what that means.")
            
    
def shack():
    global first_shack
    global carpet
    global hatch
    global flashlight
    good = True
    if first_shack:
        print(dedent("""
        You enter the shack and see nothing out
        of the ordinary. There's hangers on the
        left wall that was probably used to hold
        up tools. There's a carpet on the floor 
        and carpets on the right wall. You can
        leave the shack whenever you want.
        """))
        first_shack = False
    else:
        print("Shack")
        
    while good:
        choice = input("> ")
        if (choice == "roll carpet") and carpet:
            print(dedent("""
            You roll the carpet which didn't
            take much force to do and notice
            theres a locked hatch that seems
            to lead down somewhere.
            """))
            carpet = False
        
        elif (choice == "roll carpet") and carpet == False:
            print("You already rolled the carpet.")
            
        elif ((choice == "use key") or (choice == "unlock hatch") ) and carpet == False and hatch and key == False:
            print(dedent("""
            You unlocked the hatch and stare
            down into the very dark basement
            of the shack. You would need a 
            flashlight to enter the basement. 
            """))
            hatch = False
        
        elif (choice == "use key") and hatch == False:
            print("Already unlocked the hatch dum dum.")
            
        elif (choice == "use key") and key:
            print("You dont have the key dummy.")
            
        elif ((choice == "go down") or (choice == "enter basement")) and hatch == False:
            basement()
        
         
        elif (choice == "leave shack") or (choice == "exit shack"):
            shack_area()
        
        elif choice == "look around" and carpet:
            print(dedent("""
            There's hangers on the
            left wall that was probably used to hold
            up tools. There's a carpet on the floor 
            and carpets on the right wall. You can
            leave the shack whenever you want.
            """))
            
        elif choice == "look around" and carpet == False:
            print(dedent("""
            Theres the hatch where you can enter
            the basement of the shack. You can 
            leave the shack whenever you want.
            """))
            
        else:
            print("I dont know what that means.")

def basement():
    global first_basement
    good = True
    
    if first_basement:
        print(dedent("""
        You walk down the dark stairs with 
        your flashlight as the only source 
        of light. It's an old basement with
        cobwebs everywhere. There is a room 
        east of you that is unlocked.
        """))
        first_basement = False
    else:
        print("Basement")
    
    while good:
        choice = input("> ")
        if (choice == "go east") or (choice == "walk east"):
            card_room()
        
        elif choice == "look around":
            print("just enter the room east of you.")
            
        elif (choice == "go up") or (choice == "exit basement"):
            shack()
            
        else:
            print("I dont know what that means.")
            
def card_room():
    global first_card_room
    global keycard
    good = True
    
    if first_card_room:
        print(dedent("""
        Basement Room
        
        You enter the dark room and with
        your flashlight look around the 
        room. This room only has a desk 
        in it. Weird. After looking 
        further on the desk you notice
        a... KEYCARD. The way to get out
        of the room is go west.
        """))
        first_card_room = False
    else:
        print("Basement Room")
        
    while good:
        choice = input("> ")
        if ((choice == "take keycard") or (choice == "pick up keycard")) and keycard == False:
            keycard = True
            print("taken")
            
        elif ((choice == "take keycard") or (choice == "pick up keycard")) and keycard:
            print("You already have the keycard dummy. SO LEAVE")
        
        elif (choice == "go west") or (choice == "walk west"):
            basement()
        
        elif (choice == "look around") and keycard == False:
            print(dedent("""
            Just take the keycard and get out
            of here already.
            """))
        
        elif (choice == "look around") and keycard:
            print("Nothing special about the room so LEAVE")
            
        else:
            print("I dont know what that means.")

def ending():
    good = True
    print(dedent("""
    You hear a beep and and the door is 
    unlocked. You Open the door and 
    there is a mysterious man with a bat just
    waiting a couple of feet from the 
    exit. You're not sure what you should
    do. Either run or attack then man. OR,
    something else.
    """))
    
    while good:
        choice = input("> ")
        if choice == "run":
            print(dedent("""
            You try to run but the man was expecting that
            so he caught you with a lasso. He approaches 
            you and ties your hand and feet. Then you get
            drugged and pass out. When you wake up you're
            in a room filled with camera's. This man has 
            been watching you. He saw you in the house 
            and the shack and the other places you've 
            been. This man has been messing with you. 
            Now you have to spend the rest of your days 
            stuck in this room, watching every decision
            you've made. 
            """))
            print("Thanks for playing!")
            exit(0)
        
        elif (choice == "attack the man") or (choice == "attack"):
            print(dedent("""
            You attack the man and knock him to the floor. 
            But he quickly gets up and fights back. He 
            lands a punch on you and now you're on the 
            floor. He detains you and duck tapes your
            hands and feet. Then you getdrugged and pass
            out. When you wake up you're in a room filled
            with camera's. This man has been watching you.
            He saw you in the house and the shack and the
            other places you've been. This man has been
            messing with you. Now you have to spend the
            rest of your days stuck in this room,
            watching every decision you've made. 
            """))
            print("Thanks for playing")
            exit(0)
        
        elif choice == "shoot the man" or choice == "use gun":
            print(dedent("""
            You shoot the man and the man seemed
            surprised that you had a gun. The man 
            falls to the floor and you make a run
            for it after. You escape the horrible 
            place and find someone with a phone
            to call for help. You get rescued and
            return to living a normal life.
            """))
            print("Thanks for playing")
            exit(0)
        
        elif choice == "throw flashlight":
            print(dedent("""
            You throw your flashlight at the man
            and he just stares at you. He looks 
            disappointed. He says \"Why do I even
            bother\" and lets you go. You escape 
            the horrible place and find someone
            with a phone to call for help. You
            get rescued and return to living a
            normal life.
            """))
            exit()
        
        else:
            print("Just type attack or run. JEEZ")

print("""
You're driving on the highway and realize that for
some reason the route you usually take is different. 
Out of nowhere the car you're in gets hit by some
invisible force and get into a serious accident which
leaves you unconscious. When you regain consciousness
you seem to be in the middle of the woods. Trees 
around you have slashes on them and it gives you 
an eerie feeling. You look around and there are 
paths north, south, east and west. There's a 
flashlight below you that you might want to pick up.
""")



start_room()
    
    


