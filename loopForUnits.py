# playerOneNumberOfUnits = int(input("How many units in your team?:"))

# playerOneListOfUnits = {"character_class":[], "character_name":[]}

# count = 0

# def playerOneCharacters (playerOneNumberOfUnits):
#     while count == 0:
#         print ("Choose a character for your team")
#         print ("""[T]roll - A strong attack but careless monster that has 50% chance of missing its target\n[K]night - A soldier with decent attack and strong defence\n[M]age - A spell caster with low attack/defence""")
#         characterClassInput = str(input("Enter chosen character:"))
#         playerOneListOfUnits["character_class"].append(characterClassInput)
#         characterNameInput = str(input("Enter character's name:"))
#         playerOneListOfUnits["character_name"].append(characterNameInput)
#         count + 1
#     if count <= playerOneNumberOfUnits:
#             print ("Choose a character for your team")
#             print ("""[T]roll - A strong attack but careless monster that has 50% chance of missing its target\n[K]night - A soldier with decent attack and strong defence\n[M]age - A spell caster with low attack/defence""")
#             playerOneExtendedCharacters = {"character_class":[], "character_name":[]}
#             characterClassInput = str(input("Enter chosen character:"))
#             playerOneExtendedCharacters["character_class"].append(characterClassInput)
#             characterNameInput = str(input("Enter character's name:"))            
#             playerOneExtendedCharacters["character_name"].append(characterNameInput)
#             finalListOFPlayerOneUnits = {**playerOneListOfUnits,**playerOneExtendedCharacters}
#             playerOneListOfUnits.update(finalListOFPlayerOneUnits)
#             count + 1

# playerOneCharacters (playerOneNumberOfUnits)

# print (playerOneListOfUnits)

playerOneNumberOfUnits = int(input("How many units in your team?:"))

playerOneListOfUnits = {"character_class":[], "character_name":[]}



def playerOneCharacters (playerOneNumberOfUnits):
    count = 0
    
    while count == 0:
        print (1)
        print ("Choose a character for your team")
        print ("""[T]roll - A strong attack but careless monster that has 50% chance of missing its target\n[K]night - A soldier with decent attack and strong defence\n[M]age - A spell caster with low attack/defence""")
        characterClassInput = str(input("Enter chosen character:"))
        playerOneListOfUnits["character_class"].append(characterClassInput)
        characterNameInput = str(input("Enter character's name:"))
        playerOneListOfUnits["character_name"].append(characterNameInput)
        count = count + 1
        print(count + 1)
        if count < playerOneNumberOfUnits:
            print ("Choose a character for your team")
            print ("""[T]roll - A strong attack but careless monster that has 50% chance of missing its target\n[K]night - A soldier with decent attack and strong defence\n[M]age - A spell caster with low attack/defence""")
            playerOneExtendedCharacters = {"character_class":[], "character_name":[]}
            characterClassInput = str(input("Enter chosen character:"))
            playerOneExtendedCharacters["character_class"].append(characterClassInput)
            characterNameInput = str(input("Enter character's name:"))            
            playerOneExtendedCharacters["character_name"].append(characterNameInput)
            finalListOFPlayerOneUnits = {**playerOneListOfUnits,**playerOneExtendedCharacters}
            count = count + 1
            print(count)
            print (finalListOFPlayerOneUnits)

playerOneCharacters (playerOneNumberOfUnits)

print (playerOneListOfUnits)