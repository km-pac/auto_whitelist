import os, time, sys, re
from skpy import Skype
from skpy import SkypeAuthException
from datetime import datetime, timedelta


token_loc = "token"
sk = Skype()
sk.conn.setTokenFile(token_loc)
sk.conn.setUserPwd("lkejna1022@gmail.com","skktawtuhjudkfkf")

if os.path.exists(token_loc) == False:
	sk.conn.getSkypeToken()
	sk.conn.readToken()
	sk.conn.writeToken()
else:
    sk.conn.readToken()

# print(sk.user)        
# print(sk.chats)        
# for chat in sk.chats:
    # if chat.topic == "GRP DEV - NA - SA": print(chat.id)

# 19:I25ld3RvbjI4MDUvJGFuZ2VsbWVsb2R5MTI7MjhjZDUzNjRiNjc2MGQ5@p2p.thread.skype

while(1):
    while sk.chats.recent():
        pass
    try:
        dev_chat = sk.chats["19:I25ld3RvbjI4MDUvJGFuZ2VsbWVsb2R5MTI7MjhjZDUzNjRiNjc2MGQ5@p2p.thread.skype"]
        messages = dev_chat.getMsgs()

        valid_ip_regex = r"(\b25[0-5]|\b2[0-4][0-9]|\b[01]?[0-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}"
       
        
        for message in messages:
            eng_time = datetime.strptime(str(message.time), '%Y-%m-%d %H:%M:%S.%f') + timedelta(hours=8)
            now = datetime.now()
      
            
            eng_timestamp = (eng_time.year, eng_time.month, eng_time.day)
            now_timestamp = (now.year, now.month, now.day)
            
            if bool(re.search(valid_ip_regex, message.content)) and "legacyquote" not in message.content and eng_timestamp == now_timestamp:
                
                print(f"TIME: {eng_time}")
                print(f"ID: {message.id}")
                print(f"USER ID: {message.userId}")
                print(f"MESSAGE: {message.content}")
                print("\n\n")
    except: continue
    time.sleep(5)
    print("Refresh")
   
 
    

    
    
     