#UI/UX
import json


#Lists used in the game
playerOneListOfUnits = []
playerTwoListOfUnits = []
playerOne = []
playerTwo = []
#######END OF LIST#######


#Functions used in the game

#For List of Units of playerOne
def playerOneCharacters (playerOneNumberOfUnits):
    count = 0
    while count < playerOneNumberOfUnits :
        print(count + 1)
        print ("Choose a character for your team")
        print ("""[T]roll - A strong attack but careless monster that has 50% chance of missing its target\n[K]night - A soldier with decent attack and strong defence\n[M]age - A spell caster with low attack/defence""")
        characterClassInput = str(input("Enter chosen character:"))
        characterNameInput = str(input("Enter character's name:"))
        localplayerOneListOfUnits = {"character_class":[characterClassInput], "character_name":[characterNameInput]}
        playerOneListOfUnits.append(localplayerOneListOfUnits)
        count = count + 1

def playerTwoCharacters (playerTwoNumberOfUnits):
    count = 0
    while count < playerTwoNumberOfUnits :
        print(count + 1)
        print ("Choose a character for your team")
        print ("""[T]roll - A strong attack but careless monster that has 50% chance of missing its target\n[K]night - A soldier with decent attack and strong defence\n[M]age - A spell caster with low attack/defence""")
        characterClassInput = str(input("Enter chosen character:"))
        characterNameInput = str(input("Enter character's name:"))
        localplayerTwoListOfUnits = {"character_class":[characterClassInput], "character_name":[characterNameInput]}
        playerTwoListOfUnits.append(localplayerTwoListOfUnits)
        count = count + 1

#AI Team
# def generateRandomPlayers(playerOneNumberOfUnits):

#######END OF FUNCTIONS#######



#INTRODUCE PSB BATTLE GAME TO USER

print ("WELCOME TO PSB BATTLE GAME")
str(input("Press enter to proceed"))

#MENU OPTIONS
Menu=("Menu \n[N]ew Game \n[R]esume Game \n[H]ow to Play \n[E]xit Game")
print (Menu)

#USER TO KEY IN CHOSEN MENU
while True:
    chosenMenu = str(input("Choose menu option: "))
    if chosenMenu.lower() == 'n': #New Game
        print ("Choose your game mode:")
        print ("[1] Player vs AI")
        print ("[2] Player vs Player")

        gameMode = int(input("Game mode chosen:"))
        if gameMode==1: #Player VS AI
            #PLAYER 1
            playerOneName = str(input("Player 1's name:"))
            playerOne.append(playerOneName)
            print (playerOneName, "build your team!")
            print ("1 unit\n2 units\n3 units\n4 units\n5 units")
            playerOneNumberOfUnits = int(input("How many units in your team?:"))
            playerOneCharacters (playerOneNumberOfUnits)
            print (playerOneName,"battle unit:")
            print (list(playerOneListOfUnits))
            #AI
            print ("VS")
            # def generateRandomPlayers(playerOneNumberOfUnits):
            # print (AI TEAM)

        elif gameMode == 2: #Player1 vs Player2
            #PLAYER 1
            playerOneName = str(input("Player 1's name:"))
            playerOne.append(playerOneName)
            print (playerOneName, "build your team!")
            print ("1 unit\n2 units\n3 units\n4 units\n5 units")
            playerOneNumberOfUnits = int(input("How many units in your team?:"))
            playerOneCharacters (playerOneNumberOfUnits)
            print (playerOneName,"battle unit:")
            print (list(playerOneListOfUnits))

            #PLAYER 2
            playerTwoName = str(input("Player 2's name:"))
            playerTwo.append(playerTwoName)
            print (playerTwoName, "build your team!")
            print ("1 unit\n2 units\n3 units\n4 units\n5 units")
            playerTwoNumberOfUnits = int(input("How many units in your team?:"))
            playerTwoCharacters (playerTwoNumberOfUnits)
            print (playerTwoName,"battle unit:")
            print (list(playerTwoListOfUnits))
        


# input = [{"character_class":"troll", "character_name":"Karen"}, ]

# def createCharacter (characterList):
#     for x in len(characterList):
#         if character class is troll 
#         pull troll.json
#         trollFile = open("init/troll.json", "r")
#         trollJson = trollFile.read()
#         troll = json.loads(trollJson)
#         troll["name"] = str(input("Name your character:"))
#         configFile = open("config.json","r")
#         configJson = configFile.read()
#         config = json.loads(configJson)
#         config["player_one"]["team"].append(troll)
#         with open('config.json','w') as outfile:
#             json.dump(config, outfile)
#         elif 

# answer = createCharacter(player1)


# trollFile = open("init/troll.json", "r")
# trollJson = trollFile.read()
# troll = json.loads(trollJson)
# troll["name"] = str(input("Name your character:"))
# configFile = open("config.json","r")
# configJson = configFile.read()
# config = json.loads(configJson)
# config["player_one"]["team"].append(troll)
# with open('config.json','w') as outfile:
#     json.dump(config, outfile)

# # userName = str(input("What is your team's name?:"))
# # print (userName,"Team VS AI Team")
# # print (userName,"Team Players:")
# # print (userTeam)
# # print ("VS\nAI Team Players:")
# # # print (aiTeam)
# # print ("A187 (Troll), A316 (Knight), A214(Mage)")  
# # print ("Begin battle!")

# # #Battle Proper
#     elif chosenMenu.lower() == 'h':
#             f = open("how_to_play.txt", "r")
#             print(f.read())
#             f.close()
#             print (Menu)
            
#     elif chosenMenu.lower() == 'e':
#         confirmation=input("Are your sure?(Y/N):")
#         if confirmation.lower() == 'y':
#             print ("Exit Game")
#             exit()
#         else:
#             print (Menu)
#             continue
#   else:
#         print ("Invalid Input. Please try again")
#         print (Menu)

# userName = str(input("What is your team's name?:"))
# print (userName,"Team VS AI Team")
# print (userName,"Team Players:")
# print ("VS\nAI Team Players:")
# # print (aiTeam)
# print ("A187 (Troll), A316 (Knight), A214(Mage)")  
# print ("Begin battle!")

# # #Battle Proper
