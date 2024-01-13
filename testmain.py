from aliasmodify import *
from skypefetch import *
from colorama import Fore, Style

count = 0
input_skype_user_pass(username)
while(1):
    user_list = []
    [users, addresses] = fetch_data_chat(count)
    
    print("\nChecking data fetched from Skype: ")
    for index, message in enumerate(users):
        print(f"{Fore.YELLOW}{Style.BRIGHT}SKYPE{Style.NORMAL}{Fore.RESET} {users[index]} : {addresses[index]}")
    
    print("\nChecking data fetched from Pfsense: ")
    for index, user in enumerate(users):
        [address_arr, descriptions_arr] = fetch_data()
        print(address_arr, descriptions_arr)
    time.sleep(5)
    count += 1