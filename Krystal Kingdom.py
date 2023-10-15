
def introScene():
  directions = ["left","right","forward"]
  print("*You are at a crossroad in the middle of a forest, you can go by 4 paths. To the left is a mysterious figure, to the right is suspiciously empty space and in front of you is a house.*")
  userInput = ""
  while userInput not in directions:
    print("Options: forward/left/right/backward")
    userInput = input()
    if userInput == "left":
      showMysteriousFigure()
    elif userInput == "right":
      showEmptySpace()
    elif userInput == "forward":
      House1()
    elif userInput == "backward":
      print("*Some unknown force prevents you from going back.*")
    else: 
      print("Please enter a valid option.")