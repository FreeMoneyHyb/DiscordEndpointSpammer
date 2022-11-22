import random
import sys
import time
import requests
#colerama eventually

# Channel To Do Stuff
channelId = "YOUR CHANNEL ID TO SPAM"

# Main Token
mytoken = "YOUR DISCORD TOKEN"

# ignore this part----------------
print("Loading Up All Data, Ints Strings Ect")
header = {"authorization": mytoken}
emojilist = (
['😳', '😀', '😅', '😊', '🤣', '🤓', '😕', '🫠', '🥱', '🤨', '🥺', '😱', '😝', '😐', '🤫', '😯', '😍', '🥰', '🤬', '🥳', '😢', '😭', '😉', '😎',
 '🤯', '😇', '🤮', '😵‍💫', '😬', '🥴', '👎', '👍', '👊', '✊'])
url = f'https://discord.com/api/v9/channels/{channelId}/messages'
url2 = f'https://discord.com/api/v9/channels/{channelId}/messages?limit=50'
channelreq = requests.get(f'https://discord.com/api/v9/channels/{channelId}', headers=header)
channelname = channelreq.json()['name']
userq = requests.get("https://discord.com/api/v9/users/@me", headers=header)
username = userq.json()['username']
discrim = userq.json()['discriminator']
poopsex = int("9999999999")
stupidi = int("4000")
stupidi2 = int("2000")

animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

for i in range(len(animation)):
    time.sleep(0.2)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()

print("\n")
print(f'''
\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
FreeMoneyHubs Discord Endpoint Beamer V2.0.0 
-------------------------------
1 = Normal Spam           8 = Ghost Spam
2 = Hentai Spam           9 = Mass React
3 = File Read Line Spam   10 = Thread Spammer
4 = Random Adress Spam    11 = Pin Spammer (50 Msg)
5 = Random Link Spam 
6 = Reply Spam (50 Msg)
7 = 2000/4000 Spam
-------------------------------

Channel : {channelname}
Account : {username}#{discrim}

''')
main = input("[?] Enter An Option : ")
# --------------------


# 1

if main == "1":
    message = input("[?] Enter A Message : ")
    for i in range(poopsex):
        data = {"content": message}
        mkq = requests.post(url, headers=header, data=data)
        if mkq.status_code == 200:
            print(f"✅ Message Sent - {message}")
            time.sleep(.0001)
        elif mkq.status_code == 400:
            print(f"❌ Token Has Been Termed")
            time.sleep(.01)
        elif mkq.status_code == 401:
            print(f"❌ Token Has Changed")
            time.sleep(.0001)
        elif mkq.status_code == 429:
            mkp = mkq.json()['retry_after']
            print(f"❌ Token Is Rate Limited {mkp}")
            time.sleep(mkp)
        else:
            print(f"❓ An Unknown Error Has Occured {mkq.text}")
            time.sleep(1)

# 2

elif main == "2":
    links = (["https://purrbot.site/api/img/nsfw/fuck/gif", "https://purrbot.site/api/img/nsfw/solo/gif",
              "https://purrbot.site/api/img/nsfw/anal/gif"])
    job = input("[?] Enter A Message To Go Along With The Hentai : ")
    for i in range(poopsex):
        eggz = random.choice(links)
        linky = requests.get(eggz)
        jo = linky.json()['link']
        message = (f"{job} {jo}")
        data = {"content": message}
        mkq = requests.post(url, headers=header, data=data)
        if mkq.status_code == 200:
            print(f"✅ Message Sent - {message}")
            time.sleep(.0001)
        elif mkq.status_code == 400:
            print(f"❌ Token Has Been Termed")
            time.sleep(.01)
        elif mkq.status_code == 401:
            print(f"❌ Token Has Changed")
            time.sleep(.0001)
        elif mkq.status_code == 429:
            mkp = mkq.json()['retry_after']
            print(f"❌ Token Is Rate Limited {mkp}")
            time.sleep(mkp)
        else:
            print(f"❓ An Unknown Error Has Occured {mkq.text}")
            time.sleep(15)

# 3

elif main == "3":
    for i in range(poopsex):
        with open("sentances.txt") as file:
            for line in file:
                message3 = line.rstrip()
                data = {"content": message3}
                mkq = requests.post(url, headers=header, data=data)
                if mkq.status_code == 200:
                    print(f"✅ Message Sent - {message3}")
                    time.sleep(.0001)
                elif mkq.status_code == 400:
                    print(f"❌ Token Has Been Termed {mkq.text}")
                    time.sleep(.01)
                elif mkq.status_code == 401:
                    print(f"❌ Token Has Changed")
                    time.sleep(.0001)
                elif mkq.status_code == 429:
                    mkp = mkq.json()['retry_after']
                    print(f"❌ Token Is Rate Limited {mkp}")
                    time.sleep(mkp)
                    requests.post(url, headers=header, data=data)
                    print(f"✅ Message Sent - {message3}")
                else:
                    print(f"❓ An Unknown Error Has Occured {mkq.text}")
                    time.sleep(1)

                # 4

elif main == "4":
    for i in range(poopsex):
        poop = requests.get("https://random-data-api.com/api/v2/addresses")
        bigp1 = poop.json()['street_address']
        bigp2 = poop.json()['city']
        bigp3 = poop.json()['state']
        bigp4 = poop.json()['zip_code']
        message = (f"{bigp1}, {bigp2}, {bigp3}, {bigp4}")
        data = {"content": message}
        mkq = requests.post(url, headers=header, data=data)
        if mkq.status_code == 200:
            print(f"✅ Message Sent - {message}")
            time.sleep(.0001)
        elif mkq.status_code == 400:
            print(f"❌ Token Has Been Termed")
            time.sleep(.01)
        elif mkq.status_code == 401:
            print(f"❌ Token Has Changed")
            time.sleep(.0001)
        elif mkq.status_code == 429:
            mkp = mkq.json()['retry_after']
            print(f"❌ Token Is Rate Limited {mkp}")
            time.sleep(mkp)
        else:
            print(f"❓ An Unknown Error Has Occured {mkq.text}")
            time.sleep(1)

# 5

elif main == "5":
    for i in range(poopsex):
        sex = requests.get("https://api.api-ninjas.com/v1/randomword")
        ani = sex.json()["word"]
        domains = random.choice(["com", "net"])
        message = (f"https://{ani}.{domains}")
        data = {"content": message}
        mkq = requests.post(url, headers=header, data=data)
        if mkq.status_code == 200:
            print(f"✅ Message Sent - {message}")
            time.sleep(.0001)
        elif mkq.status_code == 400:
            print(f"❌ Token Has Been Termed")
            time.sleep(.01)
        elif mkq.status_code == 401:
            print(f"❌ Token Has Changed")
            time.sleep(.0001)
        elif mkq.status_code == 429:
            mkp = mkq.json()['retry_after']
            print(f"❌ Token Is Rate Limited {mkp}")
            time.sleep(mkp)
        else:
            print(f"❓ An Unknown Error Has Occured {mkq.text}")
            time.sleep(1)

# 6

elif main == "6":
    message = input("[?] Enter A Message : ")
    poop = requests.get(url2, headers=header)
    jsonloadz = poop.json()
    for popbob2 in jsonloadz:
        notgayz = popbob2['id']
        notgayz2 = popbob2['content']
        datapriv = {"content": message, "message_reference": {"channel_id": channelId, "message_id": notgayz}}
        mkq = requests.post(url, headers=header, json=datapriv)
        if mkq.status_code == 200:
            print(f"✅ Replyed To ({notgayz2}) With - ({message})")
            time.sleep(.0001)
        elif mkq.status_code == 401:
            print(f"❌ Token Has Changed")
            time.sleep(.0001)
        elif mkq.status_code == 429:
            mkp = mkq.json()['retry_after']
            print(f"❌ Token Is Rate Limited {mkp}")
            time.sleep(mkp)
            requests.post(url, headers=header, json=data)
            print(f"✅ Replyed To ({notgayz2}) With - ({message})")
        else:
            print(f"❓ An Unknown Error Has Occured {mkq.text}")
            time.sleep(1)

        # 7

elif main == "7":
    nitro = input("[?] Does This Token Have Premium Nitro y/n : ")
    if nitro == "y":
        for i in range(poopsex):
            char4k = "".join(
                random.choice("abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSUVWXYZ") for _ in range(stupidi))
            data = {"content": char4k}
            mkq = requests.post(url, headers=header, data=data)
            if mkq.status_code == 200:
                print(f"✅ Message Sent - {mkq}")
                time.sleep(.0001)
            elif mkq.status_code == 400:
                print(f"❌ Token Has Been Termed")
                time.sleep(.01)
            elif mkq.status_code == 401:
                print(f"❌ Token Has Changed")
                time.sleep(.0001)
            elif mkq.status_code == 429:
                mkp = mkq.json()['retry_after']
                print(f"❌ Token Is Rate Limited {mkp}")
                time.sleep(mkp)
            else:
                print(f"❓ An Unknown Error Has Occured {mkq.text}")
                time.sleep(1)
    elif nitro == "n":
        for i in range(poopsex):
            char2k = "".join(
                random.choice("abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSUVWXYZ") for _ in range(stupidi2))
            data = {"content": char2k}
            mkq = requests.post(url, headers=header, data=data)
            if mkq.status_code == 200:
                print(f"✅ Message Sent - {mkq}")
                time.sleep(.0001)
            elif mkq.status_code == 400:
                print(f"❌ Token Has Been Termed")
                time.sleep(.01)
            elif mkq.status_code == 401:
                print(f"❌ Token Has Changed")
                time.sleep(.0001)
            elif mkq.status_code == 429:
                mkp = mkq.json()['retry_after']
                print(f"❌ Token Is Rate Limited {mkp}")
                time.sleep(mkp)
            else:
                print(f"❓ An Unknown Error Has Occured {mkq.text}")
                time.sleep(1)
    else:
        print("❌ Not A Valid Option Did You Use Uppercase Letters?")

# 8

elif main == "8":
    message = input("[?] Enter A Message : ")
    delt = int(input("[?] Enter A Delete Time : "))
    for i in range(poopsex):
        data = {"content": message}
        mkq = requests.post(url, headers=header, data=data)
        if mkq.status_code == 200:
            print(f"✅ Message Sent - {message}")
            time.sleep(.0001)
            fart = mkq.json()['id']
            bigfart = requests.delete(f"https://discord.com/api/v9/channels/{channelId}/messages/{fart}",
                                      headers=header)
            time.sleep(delt)
            if bigfart.status_code == 204:
                print(f"✅ {fart} Has Been Deleted")
            elif bigfart.status_code == 429:
                jj = bigfart.json()['retry_after']
                time.sleep(jj)
                requests.delete(f"https://discord.com/api/v9/channels/{channelId}/messages/{fart}", headers=header)
                print(f"✅ {fart} Has Been Deleted")
        elif mkq.status_code == 400:
            print(f"❌ Token Has Been Termed")
            time.sleep(.01)
        elif mkq.status_code == 401:
            print(f"❌ Token Has Changed")
            time.sleep(.0001)
        elif mkq.status_code == 429:
            mkp = mkq.json()['retry_after']
            time.sleep(mkp)
            requests.post(url, headers=header, data=data)
        else:
            print(f"❓ An Unknown Error Has Occured {mkq.text}")
            time.sleep(1)

# 9

elif main == "9":
    question1 = input("[?] Use Random Emojis y/n : ")
    if question1 == "y":
        for i in range(poopsex):
            print(f"🤖 Listening In On ({channelname})")
            poop = requests.get(f"https://discord.com/api/v9/channels/{channelId}/messages?limit=50", headers=header)
            jsonloadz = poop.json()
            for popbob2 in jsonloadz:
                notgayz = popbob2['id']
                notgayz2 = popbob2['content']
                emojirandom = random.choice(emojilist)
                egg = requests.put(
                    f"https://discord.com/api/v9/channels/{channelId}/messages/{notgayz}/reactions/{emojirandom}/%40me?location=Message&burst=false",
                    headers=header)
                if egg.status_code == 403:
                    print(f"❌ {emojirandom} Has Already Been Used In ({notgayz})")
                elif egg.status_code == 204:
                    print(f"✅ Reaction {emojirandom} Added To - ({notgayz2})")
                    time.sleep(.0001)
                elif egg.status_code == 429:
                    mkp = egg.json()['retry_after']
                    time.sleep(mkp)
                    requests.put(
                        f"https://discord.com/api/v9/channels/{channelId}/messages/{notgayz}/reactions/{emojirandom}/%40me?location=Message&burst=false",
                        headers=header)
                    print(f"✅ Reaction {emojirandom} Added To - ({notgayz2})")
                else:
                    print(f"❓ An Unknown Error Has Occured {egg} {egg.text}")

    if question1 == "n":
        emoji = input("[?] Enter An Emoji")
        for i in range(poopsex):
            print(f"🤖 Listening In On ({channelname})")
            poop = requests.get(f"https://discord.com/api/v9/channels/{channelId}/messages?limit=50", headers=header)
            jsonloadz = poop.json()
            for popbob2 in jsonloadz:
                notgayz = popbob2['id']
                notgayz2 = popbob2['content']
                egg = requests.put(
                    f"https://discord.com/api/v9/channels/{channelId}/messages/{notgayz}/reactions/{emoji}/%40me?location=Message&burst=false",
                    headers=header)
                if egg.status_code == 403:
                    print(f"❌ {emoji} Has Already Been Used In ({notgayz})")
                elif egg.status_code == 204:
                    print(f"✅ Reaction {emoji} Added To - ({notgayz2})")
                    time.sleep(.0001)
                elif egg.status_code == 429:
                    mkp = egg.json()['retry_after']
                    time.sleep(mkp)
                    requests.put(
                        f"https://discord.com/api/v9/channels/{channelId}/messages/{notgayz}/reactions/{emoji}/%40me?location=Message&burst=false",
                        headers=header)
                    print(f"✅ Reaction {emoji} Added To - ({notgayz2})")
                else:
                    print(f"❓ An Unknown Error Has Occured {egg} {egg.text}")
    else:
        print("❌ Not A Valid Option Did You Use Uppercase Letters?")

# 10

elif main == "10":
    tname = input("[?] Enter A Thread Name : ")
    poop = requests.get(f"https://discord.com/api/v9/channels/{channelId}/messages?limit=50", headers=header)
    jsonloadz = poop.json()
    for popbob2 in jsonloadz:
        notgayz = popbob2['id']
        data = {"name": tname, "location": "Message"}
        mkq = requests.post(f"https://discord.com/api/v9/channels/{channelId}/messages/{notgayz}/threads",
                            headers=header, json=data)
        if mkq.status_code == 201:
            print(f"✅ Thread Created - {tname}")
            time.sleep(.0001)
        elif mkq.status_code == 429:
            mkp = mkq.json()['retry_after']
            print(f"❌ Token Is Rate Limited {mkp}")
            time.sleep(mkp)
            jackjumper = requests.post(f"https://discord.com/api/v9/channels/{channelId}/messages/{notgayz}/threads",
                                       headers=header, json=data)
            print(f"✅ Thread Created - {tname}")
        else:
            print(f"❓ An Unknown Error Has Occured {mkq.text}")
            time.sleep(15)

# 11

elif main == "11":
    poop = requests.get(f"https://discord.com/api/v9/channels/{channelId}/messages?limit=50", headers=header)
    jsonloadz = poop.json()
    for popbob2 in jsonloadz:
        notgayz = popbob2['id']
        notgayz2 = popbob2['content']
        egg = requests.put(f"https://discord.com/api/v9/channels/{channelId}/pins/{notgayz}", headers=header)
        if egg.status_code == 204:
            print(f"✅ Pinned Message - {notgayz2}")
            time.sleep(.0001)
        elif egg.status_code == 429:
            mkp = egg.json()['retry_after']
            print(f"❌ Token Is Rate Limited {mkp}")
            time.sleep(mkp)
            requests.put(f"https://discord.com/api/v9/channels/{channelId}/pins/{notgayz}", headers=header)
            print(f"✅ Pinned Message - {notgayz2}")
        else:
            print(f"❓ An Unknown Error Has Occured {egg.text}")
            time.sleep(15)

        #Dev Only (Unless you for some reason need this lmafo)

elif main =="dev":
    message = "!help"
    # channels
    channel1 = "redacted"
    channel2 = "redacted"
    channel3 = "redacted"
    channel4 = "redacted"
    channel5 = "redacted"
    channel6 = "redacted"

    token1 = "redacted"
    token2 = "redacted"
    token3 = "redacted"
    token4 = "redacted"
    token5 = "redacted"
    token6 = "redacted"

    for i in range(poopsex):
        channelz = random.choice([channel1, channel2, channel3, channel4, channel5, channel6])
        takens = random.choice([token1, token2, mytoken, token3, token4, token5, token6])
        url = 'https://discord.com/api/v9/channels/{}/messages'.format(channelz)
        data = {"content": message}
        mkq = requests.post(url, headers=header, data=data)

        if mkq.status_code == 200:
            print(f"✅ Message Sent - {message} - Channel {channelz}")
            time.sleep(.0001)
        elif mkq.status_code == 401:
            print(f"❌ Token Has Changed {takens}")
            time.sleep(.0001)
        elif mkq.status_code == 429:
            mkp = mkq.json()['retry_after']
            print(f"❌ Token Is Rate Limited {mkp}")
        else:
            print(f"❓ An Unknown Error Has Occured {mkq.text}")
            time.sleep(15)


