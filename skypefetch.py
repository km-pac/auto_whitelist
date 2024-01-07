import getpass, time, os, re
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

chat_name = "GRP DEV"


# Initialize Selenium
options = Options()
options.add_experimental_option("detach", True)
# options.add_argument('headless')
driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), 
                          options = options)
driver.get(url)


def input_user_pass(username):
    delay = 2000
    user_bar_xpath = '//*[@id="i0116"]'
    pass_bar_xpath = '/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div[2]/div/div[3]/div/div[2]/div/div[3]/div/div[2]/input'
    no_button_xpath = "//input[contains(@class, 'win-button') and contains(@class, 'button-secondary') and contains(@class, 'button') and contains(@class, 'ext-button') and contains(@class, 'secondary') and contains(@class, 'ext-secondary')]"
    
    # Input username
    WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, user_bar_xpath)))  
    enter_user = ActionChains(driver).send_keys(username, Keys.ENTER).perform()
    print("STATUS: Username was SUCCESSFULY passed in")
    
    # Input password
    WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, pass_bar_xpath)))
    enter_pass = ActionChains(driver).send_keys(password, Keys.ENTER).perform()
    print("STATUS: Password was SUCCESSFULY passed in")
    
    print("PROMPT: Please AUTHENTICATE using the Microsoft Authenticator")
    
    # Ensure that user does not stays signed in
    no_button = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, no_button_xpath)))
    time.sleep(1.5)
    signed_act = ActionChains(driver).click(no_button).perform()
    
    print("STATUS: SUCCESSFULY logged in")
    
    
def fetch_data_chat():
    print(f"STATUS: Waiting for {url} to load")
    
    delay = 5000   
    users = []
    whitelist_addresses = []
    verf_user = []
    verf_whitelist_addresses = []
    valid_ip_regex = r"^(25[0-5]|2[0-4]\d|[01]?\d\d?)\.(25[0-5]|2[0-4]\d|[01]?\d\d?)\.(25[0-5]|2[0-4]\d|[01]?\d\d?)\.(25[0-5]|2[0-4]\d|[01]?\d\d?)$"
    
    chat_xpath = f'//div[@aria-label[contains(., "{chat_name}")]]'
    messages_container_xpath = '/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div[2]/div/div/div/div/div/div[1]/div/div[1]/div/div/div/div[1]/div/div[2]'
    
    # Waits for the chat to appear before performing the action
    chat = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, chat_xpath)))
    click_chat = ActionChains(driver).click(chat).perform()
    print(f"STATUS: Found chat group {chat_name}")
    
    os.system('cls')
    
    # Waits for the messages to appear before performing the action
    WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, messages_container_xpath)))
    messages = driver.find_elements(By.XPATH, messages_container_xpath)
    print(f"STATUS: Reading messages in {chat_name}")
    
    # Split the single line of string and stores it in array
    for message in messages:
        text_messages = message.text.splitlines()

    for index, text in enumerate(text_messages):
        # If the first entry in the chat is a message it replaces it with : Forces the first index to be a user.
        if index == 0 and ":" not in text: text = ":"
        
        # Categorizes users and ip addresses in the chat array
        if ":" in text: 
            # Only appends user that is NOT NA_LEEKIE or NA_SUPPORT and discards the timestamp
            if bool(re.compile(r'(na_leekie|network)', re.IGNORECASE).search(text)): users.append("")
            else: users.append(text.split(",")[0])
           
            whitelist_addresses.append("USER")
        if ":" not in text:
            # If message contains no user it appends the previous user
            users.append(users[index-1])
            whitelist_addresses.append("".join(x for x in text if x.isdigit() or x == "."))
            
    
    # Further parses the data and only appends users and their respected whitelisted ip
    for index, message in enumerate(whitelist_addresses):
        # Appends users and valid IPs only, discards BLANK users 
        if re.search(valid_ip_regex, whitelist_addresses[index]) and not (":" in users[index] or users[index] == ""):
            verf_user.append(users[index])
            verf_whitelist_addresses.append(message)

    return verf_user, verf_whitelist_addresses


input_user_pass(username)
while(1):
    [user, whitelist_address] = fetch_data_chat()
    for index, x in enumerate(user):
        print(f"{user[index]} : {whitelist_address[index]}")
    time.sleep(10)
    
