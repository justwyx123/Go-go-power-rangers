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
        localplayerOneListOfUnits = {"character_class":[characterClassInput], "character_name":[characterNameInput]}
        playerOneListOfUnits.append(localplayerOneListOfUnits)
        count = count + 1
    

playerOneCharacters (playerOneNumberOfUnits)

print (list(playerOneListOfUnits))