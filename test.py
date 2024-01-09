import re, os, time
from colorama import Fore, Style

text = "\nWednesday December 03 2023\nMJ, 7:00 AM\nPa allow ng IP ko 192.168.10.20\nthenks\nthenks\nThursday December 03 2023\nMJ, 7:10 AM\nPa-allow\n10.124.12.10\nThursday December 04 2023\nMJ, 7:10 AM\ndfsdfdsfsdf\nBob, 8:60 AM\nGood Morning\nKindly allow this IP 192.168.10.12\nThenks\nCarmello, 3:20 PM\npallow IP 192.23.211.2\nYesterday\nGunda, 5:39 AM\nPre\nPre\nPre\nPa-allow\nIP address 192.11.111.23\n, 6:20 PM\n192.168.11.2\nMark, 1:20 AM\nKindly allow IP address 10.10.22.1\nToday\nCyd, 2:20 AM\nPa-allow IP ko 1.1.22.34\nO, 5:10 PM\n IP 30.201.110.3\nNA_LEEKIE, 2:20 AM\nPa-allow IP ko 1.1.22.3"
seg_text = text.splitlines()


print(f"\nNot Parsed: \n{seg_text}\n")




timestamp = []
users = []
addresses = []
verf_timestamp = []
verf_user = []
verf_whitelisted_address = []


valid_ip_regex = r"(\b25[0-5]|\b2[0-4][0-9]|\b[01]?[0-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}"
timestamp_regex = "(Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday|Today|Yesterday).*"
users_regex = ".*,\s(\d{2}|\d{1}:\d{2}|\d{1})\s(PM|AM)"
network_user_resgex = "(\d{2}|\d{1}:\d{2}|\d{1})\s(PM|AM)"

def data_fetch(text):
    print("Raw Data:")
    for index, text in enumerate(seg_text):
        print(text)


    # Categorizes the timestamps users and addresses
    for index, text in enumerate(seg_text):
        # Append TIMESTAMP if timestamp is missing
        if bool(re.search(timestamp_regex, text)): timestamp.append(text)
        else: timestamp.append("TIMESTAMP")
        # Append USER if user is mising
        if bool(re.search(users_regex, text)): users.append(text)
        else: users.append("USER")
        # Append ADDRESS if address is missing
        if bool(re.search(valid_ip_regex, text)): addresses.append(text)
        else: addresses.append("ADDRESS")
           
    # ENSURES that len for each arrays are equal, ensures that the index won't be out of range
    print("\n\nARRAY COUNT: TIMESTAME USERS addresses")
    print(len(timestamp), len(users), len(addresses))


    print("\nParitally Parsed Data:")
    for index, address in enumerate(addresses):
        print(f"{timestamp[index]} : {users[index]} : {address}")


    # Further parses the arrays, if it contains TIMESTAMP, USER, or ADDRESS it appends the entry before it
    for index, address in enumerate(addresses):
        if timestamp[index] == "TIMESTAMP": timestamp[index] = timestamp[index-1]
        else: timestamp[index] = timestamp[index]
       
        if users[index] == "USER": users[index] = users[index-1]
        else: users[index] = users[index].split(", ")[0]


        if addresses[index] == "ADDRESS": addresses[index] = ""
        # Loop through address and check if it contains a digit or a "."
        else: addresses[index] = "".join(x for x in address if x.isdigit() or x == ".")


    print("\n\nParitally Parsed Data:")
    for index, address in enumerate(addresses):
        print(f"{timestamp[index]} : {users[index]} : {address}")
   
    # Filters only the necessary data. Drops extra information in chats
    for index, address in enumerate(addresses):
        if timestamp[index] != "" and users[index] != "" and users[index] != "NA_LEEKIE" and users[index] != "Network" and addresses[index] != "":
            verf_timestamp.append(timestamp[index])
            verf_user.append(users[index])
            verf_whitelisted_address.append(addresses[index])


    print("\n\nFinal Output:")
    return verf_timestamp, verf_user, verf_whitelisted_address




[timestamp, users, address] = data_fetch(text)
for index, x in enumerate(users):
    print(f"{timestamp[index]}  : {users[index]} : {address[index]}")
print("\n\n")

loading_sprite = ["·", "•", "••", "•••", "••••", "•••", "••", "•"]

x = 0
while x != 20:
    y = 0
    print(x)
    print(f'\r{Fore.GREEN}{Style.BRIGHT}STATUS{Style.NORMAL}{Fore.RESET}: Loading the Chat list. This might take a while {Fore.GREEN}{Style.BRIGHT}{loading_sprite[y]}{Style.NORMAL}{Fore.RESET}', flush=True, end="")
    time.sleep(1)
    if x == len(loading_sprite)-1: y = 0
    else: 
        x += 1
        y += 1
       
