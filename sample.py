import json

file = open("files/knight.json", "r")
knightJson = file.read().replace('\n','')

knight = json.loads(knightJson)

# print(knight["attributes"]["attack"])
# print(knight["attributes"]["experience"])
# print(knight["attributes"]["health"])
# print(knight["attributes"]["defence"])

knight["rank"] = 3
print (knight["rank"])

with open('files/knight.json','w') as outfile:
    json.dump(knight, outfile)
# f = open("files/file.json", "w")
# f.write("You have changed the content!")
# f.close()