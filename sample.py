import json
# Create a team
# integrate team to json

# knightFile = open("files/knight.json", "r")
# knightJson = knightFile.read()
# knight = json.loads(knightJson)
# print (knight)
# knight["name"] = str(input("Name your character:"))
# print (knight)
# configFile = open("config.json","r")
# configJson = configFile.read()
# config = json.loads(configJson)
# with open('config.json','w') as outfile:
#     json.dump(config, outfile)

knightFile = open("init/knight.json", "r")
knightJson = knightFile.read()
knight = json.loads(knightJson)
knight["name"] = str(input("Name your character:"))
configFile = open("config.json","r")
configJson = configFile.read()
config = json.loads(configJson)
config["player_one"]["team"].append(knight)
with open('config.json','w') as outfile:
    json.dump(config, outfile)



# print (config["player_one"]["team"][0]["name"])
# 

# print(knight["attributes"]["attack"])
# print(knight["attributes"]["experience"])
# print(knight["attributes"]["health"])
# print(knight["attributes"]["defence"])

#knight["rank"] = 3
#print (knight["rank"])

# with open('files/knight.json','w') as outfile:
#     json.dump(knight, outfile)
# f = open("files/file.json", "w")
# f.write("You have changed the content!")
# f.close()