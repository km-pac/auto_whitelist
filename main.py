from aliasmodify import *
from skypefetch import *
from colorama import Fore, Style
from datetime import datetime, time
import time as t


count = 0
logs_arr = []
female_devs = ["mj", "precious", "susana"]
now_time = datetime.now().time()


input_skype_user_pass(username)
while(1):
    
    mod_address_arr = []
    [users, addresses] = fetch_data_chat(count)
    
    if (len(users) or len(addresses)) != 0:
        print("\nChecking data fetched from Skype: ")
        for index, message in enumerate(users):
            print(f"{Fore.YELLOW}{Style.BRIGHT}SKYPE{Style.NORMAL}{Fore.RESET}: {users[index]} : {addresses[index]}")
        
        print("\nChecking data fetched from Pfsense: ")
        for index, user in enumerate(users):
            input_bar_xpath = '/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div[1]'
            
            [address_arr, descriptions_arr] = fetch_data()
            
            user_index = find_index_of_user(descriptions_arr, user)
            user_address = find_address_of_user(address_arr, user_index)
            mod_address_arr = modify_address_of_user(user_index, addresses[index])
          
            try:
                with open('whitelist_logs.txt', 'w') as log:
                    if user_address != mod_address_arr[user_index]: 
                        print(f"{Fore.YELLOW}{Style.BRIGHT}PFSENSE{Style.NORMAL}{Fore.RESET}: {user} IP Address was changed from {user_address} to {mod_address_arr[user_index]}")
                        logs_arr.append(f"{datetime.now()} PFSENSE: {user} IP Address was changed from {user_address} to {mod_address_arr[user_index]}\n")
                        
                        # Setup the message that will be sent
                        greeting = "morning" if now_time <= time(12, 0) else "afternoon"
                        gender = "Sir" if user.lower() not in female_devs else "Ma'am"            
                        message = f"Good {greeting} {user}, kindly try {gender}"
                        
                        # Sends the message per user
                        text_input = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, input_bar_xpath)))
                        send_message = ActionChains(driver).click(text_input).send_keys(message, Keys.ENTER).perform()
                        
                    else: 
                        print(f"{Fore.YELLOW}{Style.BRIGHT}PFSENSE{Style.NORMAL}{Fore.RESET}: No changes made for {user}")
                    
                    log.writelines(logs_arr)
                    log.close()
            except: continue
    else: print(f"{Fore.RED}{Style.BRIGHT}ERROR{Style.NORMAL}{Fore.RESET}: NO DATA FETCHED. RETRYING")  
    count += 1