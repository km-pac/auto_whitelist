import getpass, os, re
import time as t
from colorama import Fore, Style
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

os.system('cls')

url = "https://web.skype.com/"
username = "lkejna1022@gmail.com"
# password = getpass.getpass()
password = "Gu1n3ver3"

chat_name = "GRP DEV - NA"


# Initialize Selenium
options = Options()

options.add_experimental_option("detach", True)
options.add_argument("--window-position=-10000,0")
options.add_argument("--start-maximized")

driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), 
                          options = options)
driver.get(url)


def input_skype_user_pass(username):
    delay = 2000
    user_bar_xpath = '//*[@id="i0116"]'
    pass_bar_xpath = '/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div[2]/div/div[3]/div/div[2]/div/div[3]/div/div[2]/input'
    no_button_xpath = "//input[contains(@class, 'win-button') and contains(@class, 'button-secondary') and contains(@class, 'button') and contains(@class, 'ext-button') and contains(@class, 'secondary') and contains(@class, 'ext-secondary')]"
    
    # Input username
    WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, user_bar_xpath)))  
    enter_user = ActionChains(driver).send_keys(username, Keys.ENTER).perform()
    print(f"{Fore.GREEN}{Style.BRIGHT}STATUS{Style.NORMAL}{Fore.RESET}: Username was SUCCESSFULY passed in")
    
    # Input password
    WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, pass_bar_xpath)))
    enter_pass = ActionChains(driver).send_keys(password, Keys.ENTER).perform()
    print(f"{Fore.GREEN}{Style.BRIGHT}STATUS{Style.NORMAL}{Fore.RESET}: Password was SUCCESSFULY passed in")
    
    print(f"{Fore.YELLOW}{Style.BRIGHT}PROMPT{Style.NORMAL}{Fore.RESET}: Please AUTHENTICATE using the Microsoft Authenticator")
    
    # Ensure that user does not stays signed in
    no_button = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, no_button_xpath)))
    print(f"{Fore.GREEN}{Style.BRIGHT}STATUS{Fore.RESET}: SUCCESSFULY logged in")
    t.sleep(1.5)
    print(f"{Fore.GREEN}{Style.BRIGHT}STATUS{Style.NORMAL}{Fore.RESET}: Waiting for {url} to load")
    signed_act = ActionChains(driver).click(no_button).perform()
    
    
def fetch_data_chat(count):
    delay = 5000  
    users = []
    addresses = []
    verf_user = []
    verf_whitelisted_address = []
    clean_verf_user = []
    clean_verf_whitelisted_address = []
    loading_sprite = ["•   ", "••  ", "••• ", "••••", "•   ", "••  ", "••• ", "••••", "•   ", "••  ", "••• ", "••••", "•   ", "••  ", "••• ", "••••", "•   ", "••  ", "••• ", "••••"]
 
    valid_ip_regex = r"(\b25[0-5]|\b2[0-4][0-9]|\b[01]?[0-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}"
    users_regex = ".*,\s(\d{2}|\d{1}):(\d{2}|\d{1})\s(PM|AM)"
    network_user_regex = "(\d{2}|\d{1}:\d{2}|\d{1})\s(PM|AM)"
    
    os.system('cls')

    chat_xpath = '/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[1]/div/div[1]/div[2]/div[2]/div/div[2]/div/div/div[1]/div/div/div[1]/div[3]/div/div'
    
    messages_container_xpath = '/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div[2]/div/div/div/div/div/div[1]/div/div[1]/div/div/div/div[1]/div/div[2]'
    
    
    got_it_xpath = '/html/body/div[1]/div/div/div[1]/div/div[2]/div/div[2]/div/div[1]/div/div/div/div/div/div[3]/button'
    search_xpath = '/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[1]/div/div[1]/div[2]/div/div[1]/div[2]'
    search_textfield_xpath = '/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[1]/div/div[1]/div[2]/div[2]/div/div[1]/div[1]/div[2]/div[1]/div/div/div/input'
    close_search_xpath = '/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[1]/div/div[1]/div[2]/div[2]/div/div[1]/div[1]/div[2]/div[2]/button'
    
    loop_count = 0
    while loop_count != 2:
        
        # Loading time. Gives time to fully load the chat list
        for i in range(0, 8, 1):
            print(f'\r{Fore.GREEN}{Style.BRIGHT}STATUS{Style.NORMAL}{Fore.RESET}: Loading the Chat list. This might take a while {Fore.GREEN}{Style.BRIGHT}{loading_sprite[i]}{Style.NORMAL}{Fore.RESET}', flush=True, end=" ")
            t.sleep(0.7)

        loop_count += 1
        if loop_count < 2 and count < 3: driver.refresh()
    
     
    print(f"\n{Fore.GREEN}{Style.BRIGHT}STATUS{Style.NORMAL}{Fore.RESET}: Found chat group {chat_name}")
    
    if count < 1:
        got_it_button = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, got_it_xpath)))
        t.sleep(1)
        click_got = ActionChains(driver).click(got_it_button).perform()
     
   
    search = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, search_xpath)))
    click_search = ActionChains(driver).click(search).perform()
    
    search_textfield = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, search_textfield_xpath)))
    search_group = ActionChains(driver).click(search_textfield).send_keys(chat_name, Keys.ENTER).click(search_textfield).perform()
    
    t.sleep(2)
    
    # Waits for the chat to appear before performing the action
    chat = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, chat_xpath)))
    click_chat = ActionChains(driver).click(chat).perform()  
    
    t.sleep(2)
    
    # Waits for the messages to appear before performing the action
    WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, messages_container_xpath)))
    messages = driver.find_elements(By.XPATH, messages_container_xpath)
    
    print(f"{Fore.GREEN}{Style.BRIGHT}STATUS{Style.NORMAL}{Fore.RESET}: Reading messages in {chat_name}")
    
    close = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, close_search_xpath)))
    close_textfield = ActionChains(driver).click(close).perform()
    
    # Split the single line of string and stores it in array
    for message in messages:
        text_messages = message.text.splitlines()
    
    # print(text_messages)

    # Categorizes the users and addresses
    for index, text in enumerate(text_messages):
        # Append USER if user is mising
        if bool(re.search(users_regex, text)): users.append(text)
        elif bool(re.search(network_user_regex, text)): users.append("NETWORK") 
        else: users.append("USER")
        # Append ADDRESS if address is missing
        if bool(re.search(valid_ip_regex, text)): addresses.append(text)
        else: addresses.append("ADDRESS")
           
    # ENSURES that len for each arrays are equal, ensures that the index won't be out of range
    # print("\n\nARRAY COUNT: USERS addresses")
    # print(len(users), len(addresses))

    # UNCOMMENT FOR DEBUGGING
    # print("\nParitally Parsed Data:")
    # for index, address in enumerate(addresses):
        # print(f"{users[index]} : {address}")

    # Further parses the arrays, if it contains USER, or ADDRESS it appends the entry before it
    for index, address in enumerate(addresses):
        if users[index] == "USER": users[index] = users[index-1]
        elif users[index] == "USER" and users[index+1] == "NETWORK" : users[index].append("NETWORK")
        else: users[index] = users[index].split(", ")[0]

        if addresses[index] == "ADDRESS": addresses[index] = ""
        # Loop through address and check if it contains a digit or a "."
        else: addresses[index] = "".join(x for x in address if x.isdigit() or x == ".")

    # UNCOMMENT FOR DEBUGGING
    # print("\n\nParitally Parsed Data:")
    # for index, address in enumerate(addresses):
        # print(f"{users[index]} : {address}")
   
    # Filters only the necessary data. Drops extra information in chats
    for index, address in enumerate(addresses):
        if users[index].upper() != "NETWORK" and addresses[index] != "":
            verf_user.append(users[index])
            verf_whitelisted_address.append(addresses[index])
    
    
    # Removes the duplicates and assign the latest ip to be whitelisted
    verf_user_ips = {}
    for user, ip in zip(verf_user, verf_whitelisted_address):
        verf_user_ips[user] = ip

    clean_verf_user = list(verf_user_ips.keys())
    clean_verf_whitelisted_address = [verf_user_ips[user] for user in clean_verf_user]

    return clean_verf_user, clean_verf_whitelisted_address