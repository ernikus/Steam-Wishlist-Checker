import re
import json
import requests
import ast

#date and time commands
import datetime

#using webbrowser commands
import webbrowser

#Sleep command
import time



#######################################################################################################

"""
### Alternative Start


print("Please input your steam id: ")
SteamID = input()


url = 'https://store.steampowered.com/wishlist/'


if(SteamID.isdigit()):
    url += "profiles/" + SteamID
else:
    url += "id/" + SteamID

"""


exists = ""

try:
    f = open("JSON.txt")
    print("< File accessible! >")
    # Do something with the file
    exists = True
    f.close()
except IOError:
    print("< File not accessible! >")
    exists = False
    



relJSON = ""



if(exists != False):
    print("Do you wish to reload JSON?[y/n]")
    relJSON = input()




if(exists == False or relJSON == 'y'):
    # url = 'https://store.steampowered.com/wishlist/id/.../'
    url = input("Paste here link to your Wishlist: ")
    wishlist_url =  json.loads( re.findall(r'g_strWishlistBaseURL = (".*?");', requests.get(url).text)[0] )


    f = open("JSON.txt", "w")
    

    for i in range(0, 10, 1):


        #data = requests.get(wishlist_url + 'wishlistdata/?p=0').json()


        data = requests.get(wishlist_url + 'wishlistdata/?p=' + str(i)).json()

        info = json.dumps(data, indent=4)


        if (info!="[]"):

            if(i==0):
                info = info[:-2]
            else:
                info = "," + info[1:-2]
            
            print(info)
            f.write(info)
        else:

            f.write("\n}")
            break

    f.close()


file = open("JSON.txt", "r", encoding="utf-8")
data = json.load(file)

keylist = data.keys()

gameID = []

for i in keylist:
    gameID.append(i)


title = []
position = []
date = []

d = open("data.txt", "w", encoding="utf-8")


for i in range(len(gameID)):
    
    title.append(str(data[gameID[i]]["name"]))
    print(title[-1])

    position.append(str(data[gameID[i]]["priority"]))
    print(position[-1])

    date.append(str(data[gameID[i]]["added"]))
    print(date[-1]) 



for i in range(len(gameID)-1):
    for j in range(len(gameID)-1):
        if(int(position[j])>int(position[j+1])):
            position[j], position[j+1] = position[j+1], position[j]
            title[j], title[j+1] = title[j+1], title[j]
            date[j], date[j+1] = date[j+1], date[j]
            gameID[j], gameID[j+1] = gameID[j+1], gameID[j]

New_gameID = []
New_title = []
New_position = []
New_date = []            


todayDate = time.time()

print(todayDate)


for i in range(len(gameID)):

    if(data[gameID[i]]["review_score"]==0):
        continue

    #datka = int(data[gameID[i]]["release_date"])

    #if(datka>todayDate):
    #    continue

    #try:

    #    if(data[gameID[i]]["prerelease"]):
    #        continue

    #except:

    #    if(data[gameID[i]]["type"]!="Game" and data[gameID[i]]["type"]!="DLC"):
    #        continue

    if(data[gameID[i]]["type"]!="Game" and data[gameID[i]]["type"]!="DLC"):
        continue
    
    d.write(gameID[i])
    d.write("\n")
    New_gameID.append(gameID[i])

    
    d.write(title[i])
    d.write("\n")
    New_title.append(title[i])

    
    d.write(position[i])
    d.write("\n")
    New_position.append(position[i])

    
    d.write(date[i])
    New_date.append(date[i])
    d.write("\n")
    d.write("\n")
    

d.close()

print("We filtered: ", len(New_gameID))
print("out of ", len(gameID), "GAMES!")


#######################################################################################################


print("How many tabs should I open?[Depends on RAM e.g.: 10(*2) = 20 tabs] ")
tab_num = input()

#add text at the end
URL1 = "https://gg.deals/game/"

#add steamID at the end
URL2 = "https://steamdb.info/app/"

def TextPrep(text):
    
    newText = ""

    for i in text:

        #usun spacje
        if(i.isspace() or i=="\'"):
            newText += '-'

        elif(i=="-"):
            newText += i

        #usun znaki sepcjalne
        elif(i.isalnum() == False):
            continue

        else:
            newText += i

    newText = newText.lower()

    print(newText)

    return newText


for i in range(len(New_gameID)):

    if(i!=0 and i%int(tab_num)==0):
        print("You wish to continue[y/n]: ")
        answer = input()

        if(answer == "n"):
            exit(1)


    print(i+1, '/', len(New_gameID))


    temp1 = URL1 + TextPrep(New_title[i])

    temp2 = URL2 + New_gameID[i]



    #URL 1 - GG DEALS
    webbrowser.open(temp1)

    time.sleep(0.2)

    #URL 2 - SteamDB
    webbrowser.open(temp2)

    time.sleep(0.2)
