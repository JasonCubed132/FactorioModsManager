#Import modules.
import os
import json

#Get appdata directory for the user who is running it.
path = os.getenv("APPDATA")
path = path + "\Factorio\mods\mod-list.json"

#Open file
modList = open(path,"r")

#Parse to single line (this may not be neccessary)
lines = modList.readlines()
line = ""
for data in lines:
    line = line + data
line = line.strip("\n")

#Parse line to file.
parsed_json = json.loads(line)

#Load modpack file
modPackFile = open(input("Please enter the name of the modpack file: "),"r")
#modPackData = modPackFile.readlines()
modPackDataDump = ""
for line in modPackFile:
    modPackDataDump = modPackDataDump + line
#Go through mods and enable/disable them.
for mod in range(len(parsed_json["mods"])):
    print(parsed_json["mods"][mod])
    print(parsed_json["mods"][mod]["name"])
    print(parsed_json["mods"][mod]["enabled"])
    if parsed_json["mods"][mod]["name"] in modPackDataDump:
        parsed_json["mods"][mod]["enabled"] = "true"
    else:
        parsed_json["mods"][mod]["enabled"] = "false"
modList.close()
#Re-convert parsed_json for outputting to file.
print(parsed_json)
unparsed_json = json.dumps(parsed_json,ensure_ascii=False)
print(unparsed_json)

#Write to mod file.
file = path
modFile = open(file,"w")
modFile.write(unparsed_json)
modFile.close()

