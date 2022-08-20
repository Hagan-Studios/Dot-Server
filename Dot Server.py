import json

s = open("settings.json")
settings = json.load(s)
n = settings["name"]

print("Dot Server by Hagan Studios")
print("Version 1.0.0")
print("")
print("Hello "+n)
print("")
print("Welcome to Dot Server Guide")
print("Type 'm' for 'How to use guide' ,'l' for license, and 'quit' to exit")
while True:
    i=input(">>>")
    if(i=="m"):
        print("Dot Server Manual:-")
        print("")
        print("Important notes:\nThe source files are located in the 'SOURCE' directory.\nYou need to open command prompt in the 'Dot Server' directory")
        print("")
        print("Steps:\nOpen cmd in the 'Dot Server' directory.\nType 'dot'.\nThe server starts.\nOpen 192.168.0.1:[port]\nIf you want to add your HTML,JS,CSS files replace the files from the 'SOURCE' directory")
        print("")
        print("To change the PORT open the 'setting.json' file and do the required changes")
    elif(i=="l"):
        l = open("LICENSE.txt")
        li = l.read()
        print(li)
    elif(i=="quit"):
        exit()
    elif(i=="v"):
        print("Version 1.0.0")
    elif(i=="Hagan"):
        print("Who's Hagan?")
    else:
        print("Input Incorrect")
