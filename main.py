from aliasmodify import *
from skypefetch import *
from colorama import Fore, Style

count = 0
input_skype_user_pass(username)
while(1):
    user_list = []
    [users, addresses] = fetch_data_chat()
    
    print("\nChecking data fetched from Skype: ")
    for index, message in enumerate(users):
        print(f"{Fore.YELLOW}{Style.BRIGHT}SKYPE{Style.NORMAL}{Fore.RESET} {users[index]} : {addresses[index]}")
    
    print("\nChecking data fetched from Pfsense: ")
    for index, user in enumerate(users):
        [address_arr, descriptions_arr] = fetch_data()
        user_index = find_index_of_user(descriptions_arr, user)
        user_address = find_address_of_user(address_arr, user_index)
        
        user_list.append(user)
        if user_address != addresses[index] and user not in user_list: print(f"{Fore.YELLOW}{Style.BRIGHT}PFSENSE{Style.NORMAL}{Fore.RESET} {user}: Index {user_index}: {user_address}")
        else: print(f"{Fore.YELLOW}{Style.BRIGHT}PFSENSE{Style.NORMAL}{Fore.RESET}: No changes made for user {user}")
        
        modify_address_of_user(user_index, addresses[index])

    time.sleep(5)