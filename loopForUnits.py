import json


playerOneNumberOfUnits = int(input("How many units in your team?:"))

playerOneListOfUnits = []

def playerOneCharacters (playerOneNumberOfUnits):
    count = 0
    
    while count < playerOneNumberOfUnits :
        print(count + 1)
        print ("Choose a character for your team")
        print ("""[T]roll - A strong attack but careless monster that has 50% chance of missing its target\n[K]night - A soldier with decent attack and strong defence\n[M]age - A spell caster with low attack/defence""")
        characterClassInput = str(input("Enter chosen character:"))
        characterNameInput = str(input("Enter character's name:"))
        localplayerOneListOfUnits = {"character_class":characterClassInput, "character_name":characterNameInput}
        print (localplayerOneListOfUnits)
        playerOneListOfUnits.append(localplayerOneListOfUnits)
        count = count + 1
    

playerOneCharacters (playerOneNumberOfUnits)

print (list(playerOneListOfUnits))

def printUnits(playerOneListOfUnits):
    for unit in playerOneListOfUnits:
        if (unit["character_class"]) == "T":
            trollFile = open("init/mage.json", "r")
            trollJson = trollFile.read()
            troll = json.loads(trollJson)
            troll["name"] = unit["character_name"]
            configFile = open("config.json","r")
            configJson = configFile.read()
            config = json.loads(configJson)
            config["player_one"]["team"].append(troll)
            with open('config.json','w') as outfile:
                json.dump(config, outfile)
        elif (unit["character_class"]) == "K":
            knightFile = open("init/knight.json", "r")
            knightJson = knightFile.read()
            knight = json.loads(knightJson)
            knight["name"] = unit["character_name"]
            configFile = open("config.json","r")
            configJson = configFile.read()
            config = json.loads(configJson)
            config["player_one"]["team"].append(knight)
            with open('config.json','w') as outfile:
                json.dump(config, outfile)
        elif (unit["character_class"]) == "M":
            mageFile = open("init/mage.json", "r")
            mageJson = mageFile.read()
            mage = json.loads(mageJson)
            mage["name"] = unit["character_name"]
            configFile = open("config.json","r")
            configJson = configFile.read()
            config = json.loads(configJson)
            config["player_one"]["team"].append(mage)
            with open('config.json','w') as outfile:
                json.dump(config, outfile)

            

printUnits(playerOneListOfUnits)

