#UI/UX

#INTRODUCE PSB BATTLE GAME TO USER
print ("WELCOME TO PSB BATTLE GAME")
str(input("Press enter to proceed"))

print ("Menu")
print ("""[N]ew Game
[R]esume Game
[H]ow to Play
[E]xit Game""")

chosenMenu = str(input("Choose menu option: "))
userTeam = []
if chosenMenu=="N":
    print ("Choose your game mode:")
    print ("[1] Player vs AI")
    print ("[2] Player vs Player")
    answer = int(input("Game mode chosen:"))
    if answer==1:
        print ("Build your team!")
        print ("1 unit\n2 units\n3 units\n4 units\n5 units")
        numberOfUnits = int(input("How many units in your team?:"))
        if numberOfUnits==1:
                print ("Choose a character for your team")
                print ("""[T]roll - A strong attack but careless monster that has 50% chance of missing its target\n[K]night - A soldier with decent attack and strong defence\n[M]age - A spell caster with low attack/defence""")
                characterOne = str(input("Enter chosen character:"))
                def playerOne(characterOne):
                    if characterOne=="T":
                        player1unit1 = "Troll"
                    elif characterOne=="K":
                        player1unit1 = "Knight"
                    else:
                        player1unit1 = "Mage"
                player1unit1 = str(input("Name your character:"))
                finalPlayers = player1unit1
                userTeam.append (finalPlayers)

        elif numberOfUnits==2:
                print ("Choose units for your team")
                print ("""[T]roll - A strong attack but careless monster that has 50% chance of missing its target\n[K]night - A soldier with decent attack and strong defence\n[M]age - A spell caster with low attack/defence""")
                characterOne = str(input("Enter 1st character:"))
                def playerOne(characterOne):
                    if characterOne=="T":
                        player1unit1 = "Troll"
                    elif characterOne=="K":
                        player1unit1 = "Knight"
                    else:
                        player1unit1 = "Mage"
                player1unit1 = str(input("Name your 1st character:"))
                print ("Choose units for your team")
                print ("""[T]roll - A strong attack but careless monster that has 50% chance of missing its target\n[K]night - A soldier with decent attack and strong defence\n[M]age - A spell caster with low attack/defence""")
                characterTwo = str(input("Enter 2nd character:"))
                def playerOne(characterTwo):
                    if characterTwo=="T":
                        player1unit2 = "Troll"
                    elif characterTwo=="K":
                        player1unit2 = "Knight"
                    else:
                        player1unit2 = "Mage"
                player1unit2 = str(input("Name your 2nd character:"))
                finalPlayers = player1unit1,player1unit2
                userTeam.append (finalPlayers)
                
        elif numberOfUnits==3:
                print ("Choose units for your team")
                print ("""[T]roll - A strong attack but careless monster that has 50% chance of missing its target\n[K]night - A soldier with decent attack and strong defence\n[M]age - A spell caster with low attack/defence""")
                characterOne = str(input("Enter 1st character:"))
                def playerOne(characterOne):
                    if characterOne=="T":
                        player1unit1 = "Troll"
                    elif characterOne=="K":
                        player1unit1 = "Knight"
                    else:
                        player1unit1 = "Mage"
                player1unit1 = str(input("Name your 1st character:"))
                print ("Choose units for your team")
                print ("""[T]roll - A strong attack but careless monster that has 50% chance of missing its target\n[K]night - A soldier with decent attack and strong defence\n[M]age - A spell caster with low attack/defence""")
                characterTwo = str(input("Enter 2nd character:"))
                def playerOne(characterTwo):
                    if characterTwo=="T":
                        player1unit2 = "Troll"
                    elif characterTwo=="K":
                        player1unit2 = "Knight"
                    else:
                        player1unit2 = "Mage"
                player1unit2 = str(input("Name your 2nd character:"))
                print ("Choose units for your team")
                print ("""[T]roll - A strong attack but careless monster that has 50% chance of missing its target\n[K]night - A soldier with decent attack and strong defence\n[M]age - A spell caster with low attack/defence""")
                characterThree = str(input("Enter 3rd character:"))
                def playerOne(characterThree):
                    if characterThree=="T":
                        player1unit3 = "Troll"
                    elif characterThree=="K":
                        player1unit3 = "Knight"
                    else:
                        player1unit3 = "Mage"
                player1unit3 = str(input("Name your 3rd character:"))
                finalPlayers = player1unit1,player1unit2,player1unit3
                userTeam.append (finalPlayers)

        elif numberOfUnits==4:
                print ("Choose units for your team")
                print ("""[T]roll - A strong attack but careless monster that has 50% chance of missing its target\n[K]night - A soldier with decent attack and strong defence\n[M]age - A spell caster with low attack/defence""")
                characterOne = str(input("Enter 1st character:"))
                def playerOne(characterOne):
                    if characterOne=="T":
                        player1unit1 = "Troll"
                    elif characterOne=="K":
                        player1unit1 = "Knight"
                    else:
                        player1unit1 = "Mage"
                player1unit1 = str(input("Name your 1st character:"))
                print ("Choose units for your team")
                print ("""[T]roll - A strong attack but careless monster that has 50% chance of missing its target\n[K]night - A soldier with decent attack and strong defence\n[M]age - A spell caster with low attack/defence""")
                characterTwo = str(input("Enter 2nd character:"))
                def playerOne(characterTwo):
                    if characterTwo=="T":
                        player1unit2 = "Troll"
                    elif characterTwo=="K":
                        player1unit2 = "Knight"
                    else:
                        player1unit2 = "Mage"
                player1unit2 = str(input("Name your 2nd character:"))
                print ("Choose units for your team")
                print ("""[T]roll - A strong attack but careless monster that has 50% chance of missing its target\n[K]night - A soldier with decent attack and strong defence\n[M]age - A spell caster with low attack/defence""")
                characterThree = str(input("Enter 3rd character:"))
                def playerOne(characterThree):
                    if characterThree=="T":
                        player1unit3 = "Troll"
                    elif characterThree=="K":
                        player1unit3 = "Knight"
                    else:
                        player1unit3 = "Mage"
                player1unit3 = str(input("Name your 3rd character:"))
                print ("Choose units for your team")
                print ("""[T]roll - A strong attack but careless monster that has 50% chance of missing its target\n[K]night - A soldier with decent attack and strong defence\n[M]age - A spell caster with low attack/defence""")
                characterFour = str(input("Enter 4th character:"))
                def playerOne(characterFour):
                    if characterFour=="T":
                        player1unit4 = "Troll"
                    elif characterFour=="K":
                        player1unit4 = "Knight"
                    else:
                        player1unit4 = "Mage"
                player1unit4 = str(input("Name your 4th character:"))
                finalPlayers = player1unit1,player1unit2,player1unit3,player1unit4
                userTeam.append (finalPlayers)
                
        elif numberOfUnits==5:
                print ("Choose units for your team")
                print ("""[T]roll - A strong attack but careless monster that has 50% chance of missing its target\n[K]night - A soldier with decent attack and strong defence\n[M]age - A spell caster with low attack/defence""")
                characterOne = str(input("Enter 1st character:"))
                def playerOne(characterOne):
                    if characterOne=="T":
                        player1unit1 = "Troll"
                    elif characterOne=="K":
                        player1unit1 = "Knight"
                    else:
                        player1unit1 = "Mage"
                player1unit1 = str(input("Name your 1st character:"))
                print ("Choose units for your team")
                print ("""[T]roll - A strong attack but careless monster that has 50% chance of missing its target\n[K]night - A soldier with decent attack and strong defence\n[M]age - A spell caster with low attack/defence""")
                characterTwo = str(input("Enter 2nd character:"))
                def playerOne(characterTwo):
                    if characterTwo=="T":
                        player1unit2 = "Troll"
                    elif characterTwo=="K":
                        player1unit2 = "Knight"
                    else:
                        player1unit2 = "Mage"
                player1unit2 = str(input("Name your 2nd character:"))
                print ("Choose units for your team")
                print ("""[T]roll - A strong attack but careless monster that has 50% chance of missing its target\n[K]night - A soldier with decent attack and strong defence\n[M]age - A spell caster with low attack/defence""")
                characterThree = str(input("Enter 3rd character:"))
                def playerOne(characterThree):
                    if characterThree=="T":
                        player1unit3 = "Troll"
                    elif characterThree=="K":
                        player1unit3 = "Knight"
                    else:
                        player1unit3 = "Mage"
                player1unit3 = str(input("Name your 3rd character:"))
                print ("Choose units for your team")
                print ("""[T]roll - A strong attack but careless monster that has 50% chance of missing its target\n[K]night - A soldier with decent attack and strong defence\n[M]age - A spell caster with low attack/defence""")
                characterFour = str(input("Enter 4th character:"))
                def playerOne(characterFour):
                    if characterFour=="T":
                        player1unit4 = "Troll"
                    elif characterFour=="K":
                        player1unit4 = "Knight"
                    else:
                        player1unit4 = "Mage"
                player1unit4 = str(input("Name your 4th character:"))
                print ("Choose units for your team")
                print ("""[T]roll - A strong attack but careless monster that has 50% chance of missing its target\n[K]night - A soldier with decent attack and strong defence\n[M]age - A spell caster with low attack/defence""")
                characterFive = str(input("Enter 5th character:"))
                def playerOne(characterFive):
                    if characterFive=="T":
                        player1unit5 = "Troll"
                    elif characterFive=="K":
                        player1unit5 = "Knight"
                    else:
                        player1unit5 = "Mage"
                player1unit5 = str(input("Name your 5th character:"))
                finalPlayers = player1unit1,player1unit2,player1unit3,player1unit4, player1unit5
                userTeam.append (finalPlayers)

#elif chosenMenu=="R":
elif chosenMenu=="H":
        f = open("how_to_play.txt", "r")
        print(f.read())
        f.close()
else:
    print ("Exit game")

userName = str(input("What is your team's name?:"))
print (userName,"Team VS AI Team")
print (userName,"Team Players:")
print (userTeam)
print ("VS\nAI Team Players:")
# print (aiTeam)
print ("A187 (Troll), A316 (Knight), A214(Mage)")  
print ("Begin battle!")

#Battle Proper
