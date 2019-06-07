from sys import exit
from textwrap import dedent
from os import system, name

# define clear function
def screen_clear():
   if name == 'nt':
      _ = system('cls')
   # for mac and linux(here, os.name is 'posix')
   else:
      _ = system('clear')


class Scene(object):

    def next(self):
        pass

class Engine(object):

    def __init__(self, battle, phase):
        self.battle = battle
        self.phase = phase

    def play(self):
        current_scene = self.battle.opening_scene()
        last_scene = self.battle.play_scene('finished')

        while current_scene != last_scene:
            # self.battle.play_scene('look')
            next_scene_name = current_scene.start()
            current_scene = self.battle.play_scene(next_scene_name)

        current_scene.start()

class Tools(object):
    avaiable = ['Rock', 'Pitchfork', 'Bomb', 'Double Ax', 'Sunglasses']
    inventory = []
    
class Phase(object):

    def __init__(self, phase, battle):
        self.phase = phase
        self.battle = battle

    def get_phase(self):
        return self.phase

    def next_phase(self):
        self.phase += 1

        if(self.phase == 1):
            self.battle.play_scene('phase1')
        elif(self.phase == 2):
            self.battle.play_scene('phase2')
        elif(self.phase == 3):
            self.battle.play_scene('phase3')

class Opening(Scene):

    def start(self):
        print(dedent(""" 
        You are in a beautiful garden, with vine covered cobblestone walls, a small waterfall trickling down a rock face,
        and right in front of you, an empty plot of tilled land.
        That is, empty except for a single red flower, in the very center of the plot of land.
        You see a watering can to your right, under a large fern. Will you be kind and water the flower?"""))
        what = input("> ")
        if what.lower() == 'yes':
            return 'phase1' 

class Phase1(Scene):

    def start(self):
        screen_clear()
        print(dedent("""
        Out of the watering can emerges clear, pure water, sparkling in the midday sun. It runs down the flower's leaves and covers it's crimson petals.
        
        ...Then the flower starts to shake.
        It vibrates mysteriously, becoming faster and faster untill...
        The ground around you explodes with a collosal force, sending you backwards several feet, landing on your rump.
        In front of you emerges the giant face of a dragon, with a viny, leaf-covered neck that emerges from the ground like a worm."""))
        return 'look'

class Look(Scene):

    def start(self):
        print(dedent(""" You look around... you see: """))
        for i in a_tools.avaiable:
            print(dedent('* ' + i))
        print("What do you do?")
        take = input("> ")
        
        words = take.split()
        print(words[0])
        
        if words[0].lower() == "use":
            if words[1].lower() == "rock" and "Rock" in a_tools.inventory:
                return 'useRock'
            if words[1].lower() == "pitchfork" and "Pitchfork" in a_tools.inventory:
                return 'usePitch'
            if words[1].lower() == "bomb" and "Bomb" in a_tools.inventory:
                return 'useBomb'
            if words[1].lower() == "ax" and "Double Ax" in a_tools.inventory:
                return 'useAx'
            if words[1].lower() == "sunglasses" and "Sunglasses" in a_tools.inventory:
                return 'useSun'

        
        if words[0].lower() == "take":
            
            for x in a_tools.avaiable:
                if x in take:
                    a_tools.inventory.append(x)
                    a_tools.avaiable.remove(x)
                    print(a_tools.inventory)
                    print(a_tools.avaiable)
                    
            return 'look'
        

class Phase2(Scene):

    def start(self):
        pass

class Phase3(Scene):

    def start(self):
        pass

class Death(Scene):

    def start(self):
        print(dedent(""" Sorry, guy. You're are pretty bad if you knows what im sayingg """))
        exit(1)

class UseRock(Scene):

    def start(self):
        print(dedent(""" You threw the rock. That didn't do much. """))
        return 'look'

class UsePitch(Scene):

    def start(self):
        print(dedent(""" 
        You threw the pitchfork like a javelin, but the dragon fires a great ball of fire, melting the fork and
        killing you. """))
        return 'death'

class UseBomb(Scene):

    def start(self):
        if a_battle.phase_num == 1:
            print(dedent(""" Your bad. """))
            return 'look'
        elif a_battle.phase_num == 2:
            print(dedent(""" Your good! """))
            return 'finished'

class UseAx(Scene):

    def start(self):
        print(dedent(""" You swung the axe with all your might at the base of the dragon's viny neck. It sticks there as the dragon lifts up his head in a mighty roar. """))
        a_battle.next_phase()
        print(dedent(""" It's hurt! what will you do to finish it off? """))
        return 'look'

class UseSunglasses(Scene):

    def start(self):
        print(dedent(""" You look cool. So cool, your DEFENSE increased! """))
        return 'look'

class Finished(Scene):

    def start(self):
        print(dedent("""
        You threw the bomb into the dragon's gaping maw. A couple seconds later, a muffled BOOM eminates from the dragon's jaw, along with a great
        amount of black smoke...
        When the smoke clears, the garden is covered in flowers."""))

class Battle(object):
    phase_num = 1

    scenes = {
        'look' : Look(),
        'opening' : Opening(),
        'phase1' : Phase1(),
        'phase2' : Phase2(),
        'phase3' : Phase3(),
        'useRock' : UseRock(),
        'usePitch': UsePitch(),
        'useBomb' : UseBomb(),
        'useAx': UseAx(),
        'useSun' : UseSunglasses(),
        'death' : Death(),
        'finished' : Finished()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def play_scene(self, scene_name):
        val = Battle.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.play_scene(self.start_scene)
        
    def next_phase(self):
        self.phase_num += 1


a_tools = Tools()
a_battle = Battle("opening")
a_phase = Phase(0, a_battle)
a_game = Engine(a_battle, a_phase)
a_game.play()