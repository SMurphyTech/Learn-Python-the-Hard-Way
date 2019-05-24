
class Scene(object):
    
    def enter(self):
        pass
    
class Engine(object):
    
    def __init__(self, scene_map):
        self.scene_map = scene_map
    
    def play(self):
        self.scene_map.opening_scene()
    
class Death(Scene):
    
    def enter(self):
        print("Game Over")
    
class CentralCorridor(Scene):
    
    def enter(self):
        print("You enter the central corridor. Everything is exploding.")
        print("It appears that the ship is under attack.")
        print("Standing at the end of the corridor is one of the attackers, armed with a big hammer.")
        joke = input("The only weapon you have is your amazing sense of humor. Tell a joke? (Y/N)")
        if(joke == 'Y' or joke == 'y'):
            print("You ask, what do you call a guy that hangs around musicians?")
            print("A drummer!")
            print("The alian looks at you strangley. Then, he falls to his kness and begins to weep. You walk past him.")
            input("press enter to continue. > ")
            lwa = LaserWeaponArmory()
            lwa.enter()
        elif(joke == 'N' or joke == 'n'):
            print("The ailieanan is mad because he doesn't get a funnee joke. He smushes you with his hammer.")
            die = Death()
            die.enter()
        else:
            print("you die because you CAN'T READ!")
            die = Death()
            die.enter()
    
class LaserWeaponArmory(Scene):
    
    def enter(self):
        print("You enter the room and immediatly trip on something heavy and metal on the ground.")
        print("You look back and see that it is a nuetron bomb.")
        print("Who left that on the floor?")
        print("It was probably Dave. No, it was definitely Dave.")
        print("You don't like Dave. I don't like Dave.")
        print("Everybody hates Dave.")
        print("But anyway, you pick up the bomb and move on to the next room.")
        input("press enter to continue. > ")
        brig = TheBridge()
        brig.enter()
    
class TheBridge(Scene):
    
    def enter(self):
        print("You enter the brige. It is a beautiful day out. The asteroids are floating by, the space winds are whistling....")
        print("there's another big stupod alienn at the end of the bridge. he has his back turned to you.")
        attack = input(""" do you: 
        1. Karate Kick
        2. Body Slam 
        3. Tickle his neck
        """)
        if(attack == '1'):
            print("You perform a flying karate kick, but you don't know karate. the alilen grabs your head and spins you so fast you float up like a helicopter into the void.")
            die = Death()
            die.enter()
        elif(attack == '2'):
            print("You throw all of your body weight onto the alinine. The alieen is vaporised, leavin only dust.")
            print("You see the proper position where you could use the nuetron bomb to blow up the ship, but a swarm of amiens are surround it.")
            print("you throw the bomb like a frisbee, and miss by 10 feet. But it's okay because the aleienss start playing frisbee with it.")
            print("You run the other direction toward the escape pods.")
            input("press enter to continue. > ")
            escape = EscapePod()
            escape.enter()
        elif(attack == '3'):
            print("You tickle his neck. He does that neck twist thing, then he turns around. you both look at eachother for like 5 seconds, then he shoots you and you die.")
            die = Death()
            die.enter()
        else:
            print("you die because you CAN'T READ!")
            die = Death()
            die.enter()
    
class EscapePod(Scene):
    
    def enter(self):
        print("You enter the escape pod, and see a big ol' glass of OJ waiting for you on the escape pod table")
        print("Tou sip it as you push the button to shoot away from your ship, and watch all of the alienimsnesannelines explode along with the ship. You were a good boy today.")
    
class Map(object):
    
    def __init__(self, start_scene):
        self.start_scene = start_scene
    
    def next_scene(self, scene_name):
        pass
    
    def opening_scene(self):
        print(self.start_scene)
        c_corridor = CentralCorridor()
        c_corridor.enter()
        
    
a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
