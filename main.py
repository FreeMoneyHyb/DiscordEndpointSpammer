import json
import requests
import time
import random
 


print('''FreeMoneyHub Discord Bypass Spammer

1 = Single Token Spam 
2 = Double Token Spam
3 = File Read Spam 
4 = Random Adress Spam
5 = Random Link Spam 

p2 = Next Page
Page 1/2 

''')

channelId = ""

token1 = ""
token2 = "-"
mytoken = "PUT TOKEN HERE"

main = input("[?] Enter An Option : ")
if main == "1":
  message = input("[?] Enter A Message : ")
  poopsex = int("9999999999")
  for i in range(poopsex):      
    url = 'https://discord.com/api/v9/channels/{}/messages'.format(channelId)
    header = {"authorization": mytoken}
    data = {"content": message}
    mkq = requests.post(url, headers=header, data=data)


    if mkq.status_code==200:            
      print(f"✅ [1] Message Sent - {message}")
      time.sleep(.0001)
    elif mkq.status_code==400:
      print(f"❌ Token Has Been Termed")
      time.sleep(.01)
    elif mkq.status_code==401:
      print(f"❌ Token Has Changed")
      time.sleep(.0001) 
    elif mkq.status_code==429:
      mkp = mkq.json()['retry_after'] 
      print(f"❌ Token Is Rate Limited {mkp}")            
      time.sleep(mkp)
    else:
      print(f"❓ An Unknown Error Has Occured {mkq.text}")
      time.sleep(15)
elif main == "2":    
  message = input("[?] Enter A Message : ")
  poopsex2 = int("9999999999")
  for i in range(poopsex2):  
    tokenz = random.choice([token1, token2])
    

    url2 = 'https://discord.com/api/v9/channels/{}/messages'.format(channelId)
    header = {"authorization": tokenz}
    data = {"content": message}
    mkq2 = requests.post(url2, headers=header, data=data)


    if mkq2.status_code==200:            
      print(f"✅ [2] Message Sent - {message}")
      time.sleep(.0001)
    elif mkq2.status_code==400:
      print(f"❌ Token Has Been Termed")
      time.sleep(.01)
    elif mkq2.status_code==401:
      print(f"❌ Token Has Changed")
      time.sleep(.0001) 
    elif mkq2.status_code==429:
      mkp2 = mkq2.json()['retry_after'] 
      print(f"❌ Token Is Rate Limited {mkp2}")            
      time.sleep(mkp2)
    else:
      print(f"❓ An Unknown Error Has Occured {mkq2.text}")
      time.sleep(15)
elif main == "3":
  poopsex3 = int("9999999999")
  for i in range(poopsex3):  
    with open("sentances.txt") as file:
        for line in file:
          message3 = line.rstrip()    

          url = 'https://discord.com/api/v9/channels/{}/messages'.format(channelId)
          header = {"authorization": mytoken}
          data = {"content": message3}
          mkq = requests.post(url, headers=header, data=data)


          if mkq.status_code==200:            
            print(f"✅ [3] Message Sent - {message3}")
            time.sleep(.0001)
          elif mkq.status_code==400:
            print(f"❌ Token Has Been Termed {mkq.text}")
            time.sleep(.01)
          elif mkq.status_code==401:
            print(f"❌ Token Has Changed")
            time.sleep(.0001) 
          elif mkq.status_code==429:
             mkp = mkq.json()['retry_after'] 
             print(f"❌ Token Is Rate Limited {mkp}")            
             time.sleep(mkp)
             requests.post(url, headers=header, data=data)          
             print(f"✅ [3] Message Sent - {message3}")
          else:
             print(f"❓ An Unknown Error Has Occured {mkq.text}")
             time.sleep(15)         
elif main == "4":
  poopsex = int("9999999999")
  for i in range(poopsex):  

    
    
    poop = requests.get("https://random-data-api.com/api/v2/addresses")
    bigp1 = poop.json()['street_address'] 
    bigp2 = poop.json()['city']
    bigp3 = poop.json()['state']
    bigp4 = poop.json()['zip_code']
    message = (f" {bigp1}, {bigp2}, {bigp3}, {bigp4}")   
    url = 'https://discord.com/api/v9/channels/{}/messages'.format(channelId)
    header = {"authorization": mytoken}
    data = {"content": message}
    mkq = requests.post(url, headers=header, data=data)


    if mkq.status_code==200:            
      print(f"✅ [4] Message Sent - {message}")
      time.sleep(.0001)
    elif mkq.status_code==400:
      print(f"❌ Token Has Been Termed")
      time.sleep(.01)
    elif mkq.status_code==401:
      print(f"❌ Token Has Changed")
      time.sleep(.0001) 
    elif mkq.status_code==429:
      mkp = mkq.json()['retry_after'] 
      print(f"❌ Token Is Rate Limited {mkp}")            
      time.sleep(mkp)
    else:
      print(f"❓ An Unknown Error Has Occured {mkq.text}")
      time.sleep(15)
elif main == "5":
  poopsex = int("9999999999")
  for i in range(poopsex):  
    
    sex = requests.get("https://api.api-ninjas.com/v1/randomword")
    ani = sex.json()["word"] 
    domains = random.choice(["com","net"])
    message = (f"https://{ani}.{domains}")
    url = 'https://discord.com/api/v9/channels/{}/messages'.format(channelId)
    header = {"authorization": mytoken}
    data = {"content": message}
    mkq = requests.post(url, headers=header, data=data)
    if mkq.status_code==200:            
      print(f"✅ [5] Message Sent - {message}")
      time.sleep(.0001)
    elif mkq.status_code==400:
      print(f"❌ Token Has Been Termed")
      time.sleep(.01)
    elif mkq.status_code==401:
      print(f"❌ Token Has Changed")
      time.sleep(.0001) 
    elif mkq.status_code==429:
      mkp = mkq.json()['retry_after'] 
      print(f"❌ Token Is Rate Limited {mkp}")            
      time.sleep(mkp)
    else:
      print(f"❓ An Unknown Error Has Occured {mkq.text}")
      time.sleep(15)
      
      
      
      
#page2
if main == "p2":
  print('''FreeMoneyHub Discord Bypasser

1 = Mass React
2 = Hentai Flooder
3 = N/A
4 = N/A
5 = N/A

Page 2/2 

''')
  p2 = input("[?] Enter An Option : ")
  if p2 =="1":
    channelid = input("[?] Enter The Channel ID : ")
    emoji = input("[?] Enter The Emoji : ")
    
    header = {"authorization": mytoken}
    poop = requests.get(f"https://discord.com/api/v9/channels/{channelid}/messages?limit=50", headers=header)
    jsonloadz = poop.json()
    for popbob2 in jsonloadz:
      notgayz = popbob2['id']
      egg = requests.put(f"https://discord.com/api/v9/channels/{channelid}/messages/{notgayz}/reactions/{emoji}/%40me?location=Message&burst=false", headers=header)
      if egg.status_code==204:            
        print(f"✅ [1] Reaction Added - {notgayz}")
        time.sleep(.0001)
      elif egg.status_code==429:
        mkp = egg.json()['retry_after'] 
        print(f"❌ Token Is Rate Limited {mkp}")            
        time.sleep(mkp)        
        requests.put(f"https://discord.com/api/v9/channels/{channelid}/messages/{notgayz}/reactions/{emoji}/%40me?location=Message&burst=false", headers=header)
        print(f"✅ [1] Reaction Added - {notgayz}")        
  elif p2 =="2":
    links = (["https://purrbot.site/api/img/nsfw/fuck/gif", "https://purrbot.site/api/img/nsfw/solo/gif"])
    job = input("[?] Enter A Message To Go Along With The Hentai : ")
    poopsex = int("9999999999")
    for i in range(poopsex): 
      eggz = random.choice(links)
      linky = requests.get(eggz)
      jo = linky.json()['link']
      message = (f"{job} {jo}")
      url = 'https://discord.com/api/v9/channels/{}/messages'.format(channelId)
      header = {"authorization": mytoken}
      data = {"content": message}
      mkq = requests.post(url, headers=header, data=data)
      if mkq.status_code==200:            
        print(f"✅ [2] Message Sent - {message}")
        time.sleep(.0001)
      elif mkq.status_code==400:
        print(f"❌ Token Has Been Termed")
        time.sleep(.01)
      elif mkq.status_code==401:
        print(f"❌ Token Has Changed")
        time.sleep(.0001) 
      elif mkq.status_code==429:
        mkp = mkq.json()['retry_after'] 
        print(f"❌ Token Is Rate Limited {mkp}")            
        time.sleep(mkp)
      else:
        print(f"❓ An Unknown Error Has Occured {mkq.text}")
        time.sleep(15)
  
    
     
    
