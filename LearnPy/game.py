from sys import exit
import random
from textwrap import dedent




class Scene(object):
    def enter(self):
        print("This scene is not configured yet.")
        print("Subclass it and implement enter()")
        exit(1)

class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')
        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

# be sure to print the last scene
        current_scene.enter()


class Death(Scene):
    quips = [
        "You died. You kinda suck at this.",
        "Your mum would be proud... if she were smarter.",
        "Such a luser.",
        "I have a small puppy that's better at this.",
        "You're worse than your Dad's jokes."
    ]

    def enter(self):
        print(Death.quips[random.randint(0,len(self.quips)-1)])
    #    exit(1)
        print("Do you want to play agian?")
        R = input("YES or NO\n>")
        if R == 'YES':
            self.a_map = Map('Central_Corridor')
            self.a_game = Engine(a_map)
            self.a_game.play()
        else:
            exit(1)


class CentralCorridor(Scene):

    def enter(self):
        print(dedent("""
        The Gothons of Planet Percal #25 have invaded your ship and 6 destroyed your entire crew.You are the last surviving 7 member and your last mission is to get the neutron destruct 8 bomb from the Weapons Armory, put it in the bridge, and blow the ship up after getting into an escape pod.

        You're running down the central corridor to the Weapons Armory when a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume flowing around his hate filled body.He's blocking the door to the Armory and  about to pull a weapon to blast you.
        """))

        action = input('>A. shoot B. dodge C. tell a joke\n')

        if action == 'A':
            print(dedent("""
            Quick on the draw you yank out your blaster and fire it at the Gothon. His clown costume is flowing and moving around his body, which throws off your aim. Your laser hits his costume but misses him entirely. This completely ruins his brand new costume his mother bought him, which makes him fly into an insane rage and blast you repeatedly in the face until you are dead. Then he eats you.
            """))
            return 'death'

        elif action == 'B':
            print(dedent("""
            Like a world class boxer you dodge, weave, slip and slide right as the Gothon's blaster cranks a laser past your head. In the middle of your artful dodge your foot slips and you bang your head on the metal wall and pass out. You wake up shortly after only to die as the Gothon stomps on your head and eats you.
            """))
            return 'death'

        elif action == 'C':
            print(dedent("""
            Lucky for you they made you learn Gothon insults in the academy. You tell the one Gothon joke you know: Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, fur fvgf nebhaq gur ubhfr. The Gothon stops, tries not to laugh, then busts out laughing and can't move. While he's laughing you run up and shoot him square in the head putting him down, then jump through the Weapon Armory door.
            """))
            return 'lasar_weapon_armory'

        else:
            print("DOES NOT COMPUTE")
            return 'Central_Corridor'

class  LaserWeaponArmory(Scene):
    def enter(self):
        print(dedent("""
        You do a dive roll into the Weapon Armory, crouch and scan  the room for more Gothons that might be hiding. It's dead quiet, too quiet. You stand up and run to the far side of the room and find the neutron bomb in its container. There's a keypad lock on the box and you need the code to get the bomb out. If you get the code wrong 10 times then the lock closes forever and you can't get the bomb."""))

        code = "9.1*10^(-11)"
        # seceret operation
        #print(code)
        guess = input("[keypad]> ")
        guesses = 0

        while guess != code and guess != "hint" and guesses < 10:
            print('BZZZZZEDDD\n If you want some hints enter hint, but you have only one chance.')
            guesses += 1
            guess = input("[keypad]> ")
            if guess == "hint":
                print("What's the probability to find aliens in our galaxy(less than 1)? Maybe you need to know something about Drake Equation.")
                guess = input()
                break


        if guess == code:
            print(dedent("""
            The container clicks open and the seal breaks, letting gas out. You grab the neutron bomb and run as fast as you can to the bridge where you must place it in the right spot.
            """))
            return 'The_Bridge'
        else:
            print(dedent("""
            The lock buzzes one last time and then you hear a sickening melting sound as the mechanism is fused together. You decide to sit there, and finally the Gothons blow up the ship from their ship and you die.
            """))
            return 'death'


class TheBridge(Scene):
    def enter(self):
        print(dedent("""
        You burst onto the Bridge with the neutron destruct bomb under your arm and surprise 5 Gothons who are trying to take control of the ship. Each of them has an even uglier clown costume than the last. They haven't pulled their wapons out yet, as they see the active bomb under your arm and don't want set it off.
        """))
        action = input('> A. throw the bomb B. slowly place the bomb\n')

        if action == 'A':
            print(dedent("""
            In a panic you throw the bomb at the group of Gothons and make a leap for the door. Right as you drop it a Gothon shoots you right in the back killing you. As you die you see another Gothon frantically try to disarm the bomb. You die knowing they will probably blow up when it goes off.
            """))
            return 'death'
        elif action == 'B':
            print(dedent("""
            You point your blaster at the bomb under your arm and the Gothons put their hands up and start to sweat. You inch backward to the door, open it, and then carefully place the bomb on the floor, pointing your blaster at it. You then jump back through the door, punch the close button and blast the lock so the Gothons can't get out. Now that the bomb is placed you run to the escape pod to get off this tin can.
            """))
            return 'EscapePod'
        else:
            print("DOES NOT COMPUTE")
            return 'The_Bridge'

class EscapePod(Scene):
    def enter(self):
        print(dedent("""
        You rush through the ship desperately trying to make it to the escape pod before the whole ship explodes. It seems like hardly any Gothons are on the ship, so your run is clear of interference. You get to the chamber with the escape pods, and now need to pick one to take. There are two pods entangle with each other, they maybe both damaged or one of them damaged or both are in good state, but you don't know, unless you try one. which one do you take?
        """))

        p = random.random()
        p1 = round(p,2)
        p = 1 - p1
        p2 = round(p,2)
        print(f"Do you like the alien problem? I think you like it, so let's do more physics. The 2 pods stand for 2 quantum status and they entangle each other in a specific way, i.e like electron spin. Now I can tell you the eigenvalue of the 1st one is 1/2  and the probability to detect it is {p1}, the 2nd pod's eigenvalue is -1/2 and its probability is {p2}. So what's the expectation of the whole quantum system? You can enter the equation directly. ")
        good_pod = p1 * 1 / 2 + p2 * (- 1 / 2)
        # seceret operation
        #print(good_pod)
        guess = eval(input('[pod #]> '))
        pod = round(guess,2)

        if guess != good_pod:
            print(dedent(f"""
            You jump into pod {pod} and hit the eject button. The pod escapes out into the void of space, then implodes as the hull ruptures, crushing your body into jam jelly.
            """))
            return 'death'
        else:
            print(dedent(f"""
            You jump into pod {pod} and hit the eject button. The pod easily slides out into space heading to the planet below. As it flies to the planet, you look back and see your ship implode then explode like a bright star, taking out the Gothon ship at the same time. You won!
            """))
            return 'finished'

class Finished(Scene):

    def enter(self):
        print("You won! Good job.")
        return 'finished'

class Map(object):

    scenes = {
        'Central_Corridor': CentralCorridor(),
        'lasar_weapon_armory': LaserWeaponArmory(),
        'The_Bridge': TheBridge(),
        'EscapePod': EscapePod(),
        'death': Death(),
        'finished': Finished(),
    }

    def __init__(self,start_scene):

        self.start_scene = start_scene

    def next_scene(self,scene_name):

        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('Central_Corridor')
a_game = Engine(a_map)
a_game.play()
