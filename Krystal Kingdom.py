key = False
weapen = False
crystal = False

def Throneroomfight():
    actions = ["I have destroyed it!","The crystal?"]
    global weapen
    global key
    global crystal
    print("You have a no chance to defeat me !")
    print("Unless you destroy my crystal. It powers my armor!")
    userInput = ""
    while userInput not in actions:
        print("I have destroyed it!/The crystal?")
        userInput = input()
        if userInput == "I have destroyed it!":
           print("WHAT ! WHAT HAVE YOU DONE TO MY CRYSTAL !!!")
           print("I will check that!")
           if crystal:
               print("Oh no! My armor is not shining")
               print("*You immediately regognize that you have chance to kill him so you cut him in a half.")
               print("*You have finished the game at the best ending!")
               quit()
           else:
               print("My armor is shining. YOU LIED TO ME !!!")
               print("YOU THINK THAT YOU CAN LIE TO ME !!!")
               print("*He chopped you into a small pieces*")
               print("*You have finished the game at the trecherous ending.")
               quit()
        elif userInput == "The crystal?":
            print("HA HA HA yeah, yeah that is what i am talking about. YOU HAVE A NO CHANCE !!!")
            print("*He chopped you into a small pieces*")
            print("*You have finished the game at the worst ending!")
            quit()
        else:
            print("Please enter a valid option.")

def Throneroomreturn():
    actions = ["Yes sir", "No way! The fight is inevitable"]
    global weapen
    global key
    global crystal
    userInput = ""
    while userInput not in actions:
        print("Optins: Yes sir/No way! The fight is inevitable")
        userInput = input()
        if userInput == "Yes sir":
           print("You leaved the castle.")
           print("*You have finished the game at the neutral ending.")
        elif userInput == "No way! The fight is inevitable":
            Throneroomfight()
        else:
            print("Please enter a valid option.")
            
def Throneroom1():
    actions = ["Who are you?","Stop talking and go fight with me!"]
    global weapen
    global key
    global crystal
    print("*The king and his whole kingdom were slaughtered.*")
    print("THIS KINGDOM BELONGS TO ME !!!")
    userInput = ""
    while userInput not in actions:
        print("Options: Who are you?/Stop talking and go")
        userInput = input()
        if userInput == "Who are you?":
            print("*I am the lord of all monsters from a dark.*")
            print("*NOW COME BACK FROM WHERE YOU CAME !!!*")
            Throneroomreturn()
        elif userInput == "Stop talking and go fight with me!":
            Throneroomfight()
        else:
            print("Please enter a valid option.")

def Throneroom():
    actions = ["This castle belongs my king!"]
    global weapen
    global key
    global crystal
    print("*You have entered the throne room and saw a big creature in a throne*")
    print("*The creature immediately stands up and says:*" "Who dares to enter my castle!")
    userInput = ""
    while userInput not in actions:
        print("Option: This castle belongs my king!")
        userInput = input()
        if userInput == "This castle belongs my king!":
            Throneroom1()
        else:
            print("PLease enter a valid option.")
        
def LockedDoor():
    directions = ["forward","backward","right","left"]
    global weapen
    global key
    global crystal
    print("*You have entered a room with a locked door on the left side.*")
    print("*They must guard something important.*")
    userInput = ""
    while userInput not in directions:
        print("Options: forward/backward/left/right")
        userInput = input()
        if userInput == "left":
            if key:
                print("*You locked the door and saw that the room is a forge.*")
                print("*On the anvil you found a mighty sword.*")
                print("*You have picked up that sword and leaved the room.*")
                weapen = True
                LockedDoor()
            else:
                print("*You cannot unlocked the door! Maybe find a ... key?*")
                LockedDoor()
        #elif userInput == "left":
            #if weapen and key:
                #print("*You have already found a weapen!*")
                #print("*So for what are you looking for?*")
                #LockedDoor()
            #else:
                #print("You cannot unlocked the door! Maybe find a ... key?")
                #LockedDoor()
        elif userInput == "right":
            Gate()
        elif userInput == "backward":
           Room1()
        elif userInput == "forward":
            Room3()
        else:
            print("PLease enter a valid option")
            
def Room3():
    directions = ["room with locked door","room with guards"]
    global weapen
    global key
    global crystal
    print("*In this room is nothing which can interested you.*")
    userInput = ""
    while userInput not in directions:
        print("Options: room with locked door/room with guards")
        userInput = input()
        if userInput == "room with locked door":
            LockedDoor()
        elif userInput == "room with guards":
            Guards()
        else:
            print("PLease enter a valid option.")
            
def GuardsFight():
    print("*Now you have a hard decision.*")
    actions = ["fight","backward"]
    global weapen
    global key
    global crystal
    userInput = ""
    while userInput not in actions:
       print("Options: fight/backward")
       userInput = input()
       if userInput == "fight":
            if weapen:
                print("*You have killed easily these guards.*")
                print("*After you killed the guards and opened the door, you saw, the hallway is leading to the throne room*")
                Throneroom()
            else:
                print("*Your old sword broke and the guards cut your head off.*")
                print("*You have finished the game at the bad ending.*")
                quit()
       elif userInput == "backward":
            Guards()
       else:
            print("PLease enter a valid option.")
        
def Guards():
    directions = ["left","backward"]
    global weapen
    global key
    global crystal
    print("*You have entered a room and saw a four well-armored guards.*")
    print("*They must protects something important!*")
    userInput = ""
    while userInput not in directions:
        print("Options: forward/left/backward")
        userInput = input()
        if userInput == "backward":
            SleepingMonster()
        elif userInput == "left":
            Room3()
        elif userInput == "forward":
            GuardsFight()
        else: 
            print("Please enter a valid option.")

def SleepingMonster():
    actions = ["flee forward","fight","flee backward"]
    global weapen
    global key
    global crystal
    print("*A giant monster lies in room, seeming to be asleep.*")
    userInput = ""
    while userInput not in actions:
        print("Options: flee forward/fight/flee backward")
        userInput = input()
        if userInput == "flee backward":
            print("*You flee to the previous room.*")
            Gate()
        elif userInput == "fight":
            print("*A giant monster woke up and killed you faster than you could realize it.*")
            print("*You have finished the game at the stupiest ending.*")
            quit()
        elif userInput == "flee forward":
            print("*A giant monster did not wake up and you flee forward to the next room.*")
            Guards()
        else: 
            print("Please enter a valid option.")

def Gate():
    directions = ["left","right","backward","forward"]
    global weapen
    global key
    global crystal
    print("*You have entered a room with a big gate in front of you.*")
    userInput = ""
    while userInput not in directions:
        print("Options: forward/left/right/backward")
        userInput = input()
        if userInput == "left":
            LockedDoor()
        elif userInput == "right":
            PrisonEntrance()
        elif userInput == "forward":
            SleepingMonster()
        elif userInput == "backward":
            print("*You came back to the hall.*")
            introScene()
        else: 
            print("Please enter a valid option.")

def Prison():
    directions = ["forward","backward"]
    global weapen
    global key
    global crystal
    print("*You have entered a prison and saw a skeleton and a shiny thing on the ground.*")
    userInput = ""
    while userInput not in directions:
        print("Options: forward/backward")
        userInput = input()
        if userInput == "forward":
            print("*You have pick up the mysterious key.*")
            key = True
            PrisonEntrance()
        elif userInput == "backward":
            PrisonEntrance()
            
def PrisonEntrance():
  directions = ["left","forward","backward"]
  global weapen
  global key
  global crystal
  print("*You have entered a room and saw the next room which is forward look like a prison.*")
  userInput = ""
  while userInput not in directions:
    print("Options: forward/left/backward")
    userInput = input()
    if userInput == "backward":
      Room2()
    elif userInput == "left":
        Gate()
    elif userInput == "forward":
        Prison()
    else: 
      print("Please enter a valid option.")

def Ruinedroom():
  directions = ["backward","destroy the crystal"]
  global weapen
  global key
  global crystal
  print("*You have entered a room which is ruined and you cannot go forward.*")
  print("*On the ground at the back is laying a crystal.*")
  userInput = ""
  while userInput not in directions:
    print("Options: backward/destroy the crystal")
    userInput = input()
    if userInput == "backward":
      Room2()
    elif userInput == "destroy the crystal":
        print("*After you destroyed the crystal, it stopped shining.*")
        print("*Looks like nothing else happened*")
        print("YOu have returned to a previous room.")
        crystal = True
        Room2()
    else: 
      print("Please enter a valid option.")

def Room2():
  directions = ["backward","left","forward"]
  global weapen
  global key
  global crystal
  print("*In this room is a big picture of a king.*")
  userInput = ""
  while userInput not in directions:
    print("Options: backward/left/forward")
    userInput = input()
    if userInput == "backward":
      print("*You came back to the hall.*")
      introScene()
    elif userInput == "left":
        PrisonEntrance()
    elif userInput == "forward":
      Ruinedroom()
    else: 
      print("Please enter a valid option.")

def Room1():
  directions = ["backward","forward"]
  global weapen
  global key
  global crystal
  print("*In this room is nothing which can interested you.*")
  userInput = ""
  while userInput not in directions:
    print("Options: backward/forward")
    userInput = input()
    if userInput == "backward":
      print("*You came back to the hall.*")
      introScene()
    elif userInput == "forward":
        LockedDoor()
    else: 
      print("Please enter a valid option.")

def introScene():
  directions = ["left","right","backward""forward"]
  global weapen
  global key
  global crystal
  print("*You have entered the hall and you can go to the left, right, backward or forward.*")
  userInput = ""
  while userInput not in directions:
    print("Options: forward/left/right/backward")
    userInput = input()
    if userInput == "left":
      Room1()
    elif userInput == "right":
      Room2()
    elif userInput == "forward":
      Gate()
    elif userInput == "backward":
      print("*Some unknown force prevents you from going back.*")
    else: 
      print("Please enter a valid option.")

if __name__ == "__main__":
  while True:
    print("Welcome to Krystal kingdom!")
    print("You are a knight who returns home from an expedition, because you have heard that your castle has been attacked.")
    print("You have seen a ruined village and fleeing villagers.")
    print("One villager told you, that the castle is invaded by monsters.")
    print("You are standing at the entrance to the hall and there is none who protects it.")
    print("You realize that you forgot to bought a new sword, beacause you have only a sword which is in a bad condition from an expedition.")
    print("So let's start with your name: ")
    name = input()
    print("Good luck, " +name+ ", you will need it.")
    introScene()