import re

text = "\nsdfsdffdsf\nTuesday, December 16, 2023\nNetwork\nmessage\n, 3:28 AM\n192.11.111.23\nNA_LEEKIE, 3:28 AM\n192.11.111.23\nCarlo, 8:60 AM\nGood Morning\nKindly allow this IP 192.168.10.12\nThenks\nYesterday\nCarmello, 3:20 PM\npallow IP 192.23.211.2\nGunda, 5:39 AM\nPre\nPre\nPre\nPa-allow\nIP address 192.11.111.23\nToday\nCarlo, 8:60 AM\nPssst oks na address?"
seg_text = text.splitlines()
print(f"\nNot Parsed: \n{seg_text}\n")

dict = {}
users = []
messages = []
verf_user = []
whitelisted_address = []

valid_ip_regex = r"^(25[0-5]|2[0-4]\d|[01]?\d\d?)\.(25[0-5]|2[0-4]\d|[01]?\d\d?)\.(25[0-5]|2[0-4]\d|[01]?\d\d?)\.(25[0-5]|2[0-4]\d|[01]?\d\d?)$"
time_regex = "*\b(?:1[0-2]|0?[1-9]):[0-5][0-9] [APMapm]{2}\b"

date_regex = r'\b(Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday|Today|Yesterday)\b'
date = []

def data_fetch(text):
    print("ORIG DATA")
    for index, text in enumerate(seg_text):          
        print(text)
    print("\n\n\nNOT PARSED")
    
    for index, text in enumerate(seg_text):
        if index == 0 and ":" not in text: text = ":"
        
        if ":" in text: 
            if bool(re.compile(r'(na_leekie|network)', re.IGNORECASE).search(text)): users.append("")
            else: users.append(text.split(",")[0])
            messages.append("USER")
     
        if ":" not in text:
            
            users.append(users[index-1])
            messages.append("".join(x for x in text if x.isdigit() or x == "."))
            
        if bool(re.compile(date_regex, re.IGNORECASE).search(text)):
            date.append(text)
        bool(re.compile(date_regex, re.IGNORECASE).search(text[index+1])):
            date[index+1].appned(text)
            
    
    for index, message in enumerate(messages):          
        print(f"{date[index]} : {users[index]} : {message}")
    print("\n\n\nPARSED")
    
    for index, message in enumerate(messages):
        if re.search(valid_ip_regex, messages[index]) and not (":" in users[index] or users[index] == ""):
            verf_user.append(users[index])
            whitelisted_address.append(message)
                


    return verf_user, whitelisted_address, date

[users, address, date] = data_fetch(seg_text)
for index, x in enumerate(users):
    print(f"{date[index]} : {users[index]}: {address[index]}")
