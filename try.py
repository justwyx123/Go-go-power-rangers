# # # import json

# # # trollFile = open("init/troll.json", "r")
# # # trollJson = trollFile.read()
# # # troll = json.loads(trollJson)
# # # troll["name"] = str(input("Name your character:"))
# # # configFile = open("config.json","r")
# # # configJson = configFile.read()
# # # config = json.loads(configJson)
# # # config["player_one"]["team"].append(troll)
# # # with open('config.json','w') as outfile:
# # #     json.dump(config, outfile)


playerOneNumberOfUnits = int(input("How many units in your team?:"))

playerOneListOfUnits = {"character_class":[], "character_name":[]}
count = 0

def playerOneCharacters (playerOneNumberOfUnits):
    while count <= playerOneNumberOfUnits:
        print ("Choose a character for your team")
        print ("""[T]roll - A strong attack but careless monster that has 50% chance of missing its target\n[K]night - A soldier with decent attack and strong defence\n[M]age - A spell caster with low attack/defence""")
        characterClassInput = str(input("Enter chosen character:"))
        playerOneListOfUnits["character_class"].append(characterClassInput)
        characterNameInput = str(input("Enter character's name:"))
        playerOneListOfUnits["character_name"].append(characterNameInput)
        count + 1
        break

playerOneCharacters (playerOneNumberOfUnits)

print (playerOneListOfUnits)

