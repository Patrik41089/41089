key = False
weapen = False
crystal = False

def Throneroom():
    

def LockedDoor():
    directions = ["forward","backward","right","left"]
    global weapen
    global key
    global crystal
    print("*You have entered a room with locked doors on the left side.*")
    print("*They must guard something important.*")
    userInput = ""
    while userInput not in directions:
        print("Options: forward/backward/left/right")
        userInput = input()
        if userInput == "left":
            if key:
                print("*You locked the door and saw that the room is a forge*")
                print("*On the anvil you found a mighty sword*")
                print("*You have picked up that sword and leaved the room*")
                weapen = True
                LockedDoor()
            elif weapen:
                print("*You have already found a weapen!*")
                print("*So for what are you looking for?*")
            else:
                print("You cannot unlocked the door! Maybe find a ... key?")
                LockedDoor()
        elif userInput == "right":
            Gate()
        elif userInput == "backward":
           Room1()
        elif userInput == "forward":
            Room3()
            
def Room3():
    directions = ["forward","backward"]
    global weapen
    global key
    global crystal
    print("*In this room is nothing which can interested you.*")
    userInput = ""
    while userInput not in directions:
        print("Options: forward/backward")
        userInput = input()
        if userInput == "forward":
            LockedDoor()
        elif userInput == "backward":
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
            print("*You pick up the mysterious key.*")
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