import requests
from requests_html import HTMLSession
import time
import json
s = HTMLSession()




f = open("fnamelist.txt", "r") # this textfile "fnamelist.txt" is where you should put a list of possible usernames to check
#put 1 username per line
Noobs = f.read().split()

acc = 0
#print(Noobs[acc])






while acc < 12775:
    url = "https://api.mojang.com/users/profiles/minecraft/"
    url = url + Noobs[acc]
    r = s.get(url)
    print(Noobs[acc], r.status_code)
    if r.status_code == 204:
        print("FOUND POGGERS", Noobs[acc], acc, url)

        nrl = "https://namemc.com/search?q="
        nrl = nrl + Noobs[acc]
        test = HTMLSession().get(nrl).html.find('.container .mb-3', first=True).text.split()
        if test[2] == "Available":
            ava = "Available later"
        elif test[2] == "Available*":
            ava = "Available now"
        else:
            ava = 'error'
        print('The username ', Noobs[acc], ' is ', ava)
        #Here is the discord webhook url, its been split in to two to make it easier.
        vrl1 = 'https://discordapp.com/api/webhooks/NUMBERSHERE/'
        vrl2 = 'REMAINING PART OF THE WEBHOOK'
        vrl = vrl1 + vrl2

        data = {}
        data["content"] = 'The username ' + Noobs[acc] + ' is ' + ava
        data["username"] = "MC Account Checker"

        result = requests.post(vrl, data=json.dumps(data), headers={"Content-Type": "application/json"})

        try:
            result.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print(err)
        else:
            print("Payload delivered successfully, code {}.".format(result.status_code))

        dank = open("AvailableACC.txt", "a")
        dank.write(Noobs[acc] + "\r")
        dank.close()

        dank = open("Status.txt", "a")
        dank.write(Noobs[acc] + " is " + ava + "\r")
        dank.close()
    acc = acc + 1
    time.sleep(1.5)
# <Response [204]> means the account is  available
# <Response [200]> means the account is NOT available
