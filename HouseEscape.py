# I have imported textwrap, dedent, random and randint to have complex feature in this code
from sys import exit
from random import randint
from textwrap import dedent

# Writing serveral classes is required for the game being built, in this case, "Scene", is a class that tranisions from scene to scene if each conditions are true.
class Scene(object):

    #this "def" would be able to transition with the main Scene class
    def enter(self):
        pass

# Another class is created called "StartDoor" which is the entrance of the game which would also be a method that would call the first room, its texts and the selection inputs
class StartDoor(object):

    #The def and __init__'s would let the user to the next room if the input from the user would be true
    def __init__(self, scene_map):
        pass

    def play(self):
        pass

# Another class is created called "Death" which causes the method to call if the user inputs a choice that is wrong
class Death(Scene):

    def enter(self):
        pass

# Another class is created called "FirstFloor" which transfers the user to the first main floor which would be the beginning of the game
class FirstFloor(Scene):

    def enter(self):
        pass

# Another class is created called "SecondFloor" which transfers the player to the second floor if they choose the answer correctly
class SecondFloor(Scene):

    def enter(self):
        pass

# Another class is created called "AtticRoom" which transfers the player to the attic if they chose the answer correctly
class AtticRoom(Scene):

    def enter(self):
        pass

# Another class is created called "RoofTop" which transfers the player to the final area of the game if they answered correctly
class RoofTop(Scene):

    def enter(self):
        pass

# Another class is created called "Map" which would hold an object that contains all the other locations of the game
class Map(object):

    def __init__(self, start_scene):
        pass

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass
# This method will get accesses to the other classes to get a view of the full map and will know to activate the game
a_map = Map('first_floor')
a_game = StartDoor(a_map)
a_game.play()

# This class will hold an object that will be activated if one of the classes is not completed
class Scene(object):

    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)

# This class will hold an object that would activate the beginning of the game with the first location which is "StartDoor" to "FirstFloor"
class StartDoor(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # This needs to print out the last scene
        current_scene.enter()

# This class will activate the method of death quotes if the player chooses the wrong option and will play one of these quotes are random
class Death(Scene):

    quips = [
        "Well this sucks!",
        "Not so easy is it?",
        "Your ideas only sounds good on paper.",
        "You have regretted all life's choices.",
        "School is better punishment than this.",
        "What were you thinking?",
        "There were no wrong choices and yet you came up with one."

        ]
    # this def ensures the Death method gets called and the player goes back one scene and starts from there
    def enter(self):
            print(Death.quips[randint(0, len(self.quips)- 1)])
            exit(1)

# This class is the first room the player enters after the first scene
class FirstFloor(Scene):

    # This def ensures that it prints out the first challenge and gives the player a chance to guess an output to determine whether or not the player goes to the next scene or start over.
    def enter(self):
        print(dedent("""
             You are trying to get to the second room of your aunt's house.
             You are trying to escape because you are bored out of your life
             and want to leave. However Mom doesn't want you to leave and Dad
             is stubborn but couldn't care less.

             This is the house layout:
             """))
        print("""
                      / \\
                     /   \\  
                    /     \\(RoofTop)
                   /       \\--------
                  / (Attic) \\
                 /-----------\\
                 |           |
                 | (Second)  |
                 |-----------|
                 |           |
             ----------------------
             |                    |
             |                    |
             |                    |
             |                    |
             |    (FirstFloor)    |
             |--------------------|  (StartDoor)
             |                    |----------------
             """)
        print(dedent("""
             You are going upstairs but Mom stops you. "Where are you going young man?"
             You have 3 things to say to convince her. Be careful, just because a simple choice
             is obvious, doesn't mean it would always work. Would your choice be to run, use the
             bathroom, or see your cousins. You can only say one word or number throughout the game.
             """))

        # This action calles in an input for the players to choose, in this case either run, bathroom or cousins
        action = input("> ")

        # Each of these actions are the input answers the player gets to decide, only one of these are the right answer while the others are the wrong and will push you back to the very beginning
        if action == "run":
            print(dedent("""
                 You've decided to make a run for it, but Mom goes after you and catches you.
                 You now have to stay downstairs with their dog who keeps guard and will bark if
                 you try to move.

                 After 12 hours has passed and you've been grounded, taking your stuff away and
                 replacing them with books with security cameras placed everywhere in your room.
                 """))
            return 'death'

        elif action == "bathroom":
            print(dedent("""
                 "I'm going to the bathroom", you said to your mom, "I don't think so,
                 There is no bathroom upstairs", said Mom. What kind of house doesn't
                 have an upstairs bathroom?

                 You go back downstairs and you are forced to sit down and let Mom
                 tell your embarrising stories when you where a baby with pictures.

                 Now you are traumitized with humiliation and you ended up in a coma
                 for the rest of your life. That's how you are easily humiliated.
                 """))
            return 'death'

        elif action == "cousins":
            print(dedent("""
                 Lucky for you, your two cousins are upstairs. The older one doesn't care that
                 you are here, and the younger young would be suprised if you are here.  "I'm
                 gonna go play with my cousins upstairs", you said. They fell for it.  "Ok, it's
                 better for them to play more with their family", said your aunt.

                 You go upstairs and successfully entered the second floor.
                 """))
            return 'second_floor'

        # This else statement will print out a message if the player types in something other than the three answers
        else:
            print("Are you speaking a foreign language or something? Because it doesn't make sense.")
            return 'first_floor'

# This class will transition to the second room only when the player gets the answer right in the previous scene
class SecondFloor(Scene):

    def enter(self):
        print(dedent("""
             You successfully go upstairs and you knock on your cousins' door because their room
             is the only one that leads to the attic. The younger one opens the door slightly.
             "What's the password" he says, because he likes to start off with games whenever you come.

             You only have one guess before he starts screaming if you guess it wrong.  Becareful, he
             knows the password by heart despite him being four years old.
             """))

        # This is where the randint comes in and has number suggesstions from an order of numbers up until a certain point
        code = f"{randint(1, 1)}{randint(1, 1)}{randint(1, 1)}"
        guess = input("[Password: (Hint: It's a basic 3 digit number)]> ")
        # The player gets one chance
        guesses = 0

        # This while statement will output the conditions if the player guesses incorrectly and otherwise
        while guess != code and guesses < 0:
            print("AN INTRUDER IS HERE, HE IS GOING TO HIT ME!!!!!!!")
            guesses += 0
            guess = input("[Password: (Hint: It's a basic 3 digit number)]> ")

        if guess == code:
            print(dedent("""
                 The young one opens the door and lets you in.
                 You explain to him that you want to go into the
                 attic for a secret mission.  The young one was so excited
                 and promises to keep his mouth shut about the "mission"
                 """))
            return 'attic_room'
        else:
            print(dedent("""
                 The young one screams at the top of his lungs and the family
                 downstairs hears it and goes upstairs.  By the time they came
                 upstairs, the young one says "He tried to hit me", and you tried
                 to explain that you weren't trying to hurt him, but they believe
                 the young one instead.  Now everyone is mad at you and kicks you
                 out of the house and never wants to see you again.  You now currently
                 live in a cardboard box and no one wants to help you.
                 """))
            return 'death'

# This class allows the player to access the next room if the player guesses the right answer in the previous room
class AtticRoom(Scene):

    def enter(self):
        print(dedent("""
             You walk into the attic with only one door away from freedom.
             The problem is that there are two doors to rush out of here
             One door will lead to outside, and the other leads to a room full
             of insulation.  Here's the catch, both doors look like they have
             insulation. But you only have one chance because their are rats
             in the attic and will poison you.
             """))

        action = input("> ")

        if action == "left":
            print(dedent("""
                 In a panic you open and run through the left door.
                 It's dark, and full of insulation, you instanly go into
                 an septic-shock and can't breath.  You don't know where's
                 the door because you eyes are infected with fiber glass and
                 infected your bloodstream, preventing you from breathing and 
                 you die.
                 """))
            return 'death'

        elif action == "right":
            print(dedent("""
                 In a panic you open and run through the right door.
                 It's bright and carefully step onto the rooftop. You
                 made it.
                 """))

            return 'roof_top'
        else:
            print("Are you speaking a foreign language or something? Because it doesn't make sense.")

            return "attic_room"

# This class will include the final location of the game
class RoofTop(Scene):

    def enter(self):
        print(dedent("""
             You rush through outside and cars are travelling fast.  there is a slight
             chance you will land on a car when you jump taking you to your street.
             Or there's a chance where you don't land on a car, but instead landed
             on the road and a vehicle runs over you.  From 1 to 5 seconds, when do
             you decide to jump?
             """))

        # Another example of using randint is the timing segment where the player chooses how many seconds they want to take before taking the leap of faith
        # However, the player only gets one chance and it doesn't matter what number you pick, you'll either win or loose, it all comes down to luck
        good_timing = randint(1, 5)
        guess = input("[Time decision from 1, 2, 3, 4, or 5 seconds]> ")


        if int(guess) != good_timing:
            print(dedent("""
                 You jump off the roof, and you land on the road face first
                 and a random car runs over you and die.
                 """))
            return 'death'
        else:
            print(dedent("""
                 You jump off the roof and landed face first on the car but you still survived.
                 The car drives to your street and went home like nothing ever happened. The rest
                 of the story is up to your imagination of what happens next.  You win!!!
                 """))

            return 'finished'

# This class is the ending scene that will happen if the player survives the final challenge
class Finished(Scene):

    def enter(self):
        print("Hope the family doesn't find out!")
        return 'finished'

# This class contains an object that contains the main locations and scenes of the game
class Map(object):

    scenes = {
        'first_floor': FirstFloor(),
        'second_floor': SecondFloor(),
        'attic_room': AtticRoom(),
        'roof_top': RoofTop(),
        'death': Death(),
        'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('first_floor')
a_game = StartDoor(a_map)
a_game.play()
