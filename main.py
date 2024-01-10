from aliasmodify import *
from skypefetch import *
from colorama import Fore, Style
from datetime import datetime


count = 0
logs_arr = []

input_skype_user_pass(username)
while(1):
    mod_address_arr = []
    [users, addresses] = fetch_data_chat(count)
    
    print("\nChecking data fetched from Skype: ")
    for index, message in enumerate(users):
        print(f"{Fore.YELLOW}{Style.BRIGHT}SKYPE{Style.NORMAL}{Fore.RESET}: {users[index]} : {addresses[index]}")
    
    print("\nChecking data fetched from Pfsense: ")
    for index, user in enumerate(users):
        [address_arr, descriptions_arr] = fetch_data()
        
        user_index = find_index_of_user(descriptions_arr, user)
        user_address = find_address_of_user(address_arr, user_index)
        mod_address_arr = modify_address_of_user(user_index, addresses[index])
        
        try:
            with open('whitelist_logs.txt', 'w') as log:
                if user_address != mod_address_arr[user_index]: 
                    print(f"{Fore.YELLOW}{Style.BRIGHT}PFSENSE{Style.NORMAL}{Fore.RESET}: {user} IP Address was changed from {user_address} to {mod_address_arr[user_index]}")
                    logs_arr.append(f"{datetime.now()} PFSENSE: {user} IP Address was changed from {user_address} to {mod_address_arr[user_index]}\n")
                else: 
                    print(f"{Fore.YELLOW}{Style.BRIGHT}PFSENSE{Style.NORMAL}{Fore.RESET}: No changes made for {user}")
                    logs_arr.append(f"{datetime.now()} PFSENSE: No changes made for {user}")
                
                log.writelines(logs_arr)
                log.close()
        except: continue
   
    time.sleep(5)
    count += 1