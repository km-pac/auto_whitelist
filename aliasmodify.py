import requests, json, os, re, random
import urllib3
os.system('cls')
# Hides the insecurity warning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# URL and HEADERS for Pfsense API Authentication
url = 'https://192.168.233.1:441/api/v1/firewall/alias'
headers = {
    'accept': 'application/json',
    'Authorization': 'Basic YWRtaW46VkBsM250aW5A' 
}

# Name of the ALIAS to be modified
alias_name = "TEST_TEST"
params = {"name": alias_name}


def fetch_data():
    # Grabs data from pfsense and loads it into JSON format
    response = requests.get(url, params, headers=headers, verify=False)
    alias_json = json.loads(response.text)
    
    # Process the data and assign them to corresponding arrays
    for key in alias_json["data"]:
        address_arr = alias_json["data"][key]["address"].split(" ")
        descriptions_arr = alias_json["data"][key]["detail"].split("||")
        
    # Display data fetched
    print(f"\nFetched List for {alias_name}:")
    for x in range(len(address_arr)): print(f"{address_arr[x]}: {descriptions_arr[x]}")
    
    return address_arr, descriptions_arr

# def add_new_entry():

def find_index_of_user(arr, match_string):
    match_string = match_string.lower()
    arr = [x.lower() for x in arr]                              
    dict_users_index = {}
   
    # for index, user in enumerate(arr): print(f"{index}:{user}") # Prints out the array with corresponding index   
    try:
        for index, user in enumerate(arr): 
            if match_string in user: dict_users_index[user] = index 
      
        if len(dict_users_index) > 1:
            # Outputs all the matching users with their corresponding index
            print(f"Found {len(dict_users_index)} matching users")
            for index, user in enumerate(dict_users_index): print(f"{index}: {user}")
            
            # Select index from the list of matching users
            chosen_index = int(input("Select the corresponding user: "))    

            # Assigns the index of the selected user based on the dictionary {user : index}
            for index, user in enumerate(dict_users_index):
                if chosen_index == index: index_user = dict_users_index[user]
             
            # Enable RANDOMIZER automates selection between match users
            # index_user = list(dict_users_index.values())[random.randrange(len(dict_users_index))]
            
        elif len(dict_users_index) == 1:
            index_user = list(dict_users_index.values())[0]
        
        return index_user

    except: print(f"Error: {match_string} not found")


def find_address_of_user(address_arr, user_index):
    try:
        for index, address in enumerate(address_arr):
            if index == user_index: user_address = address
        return user_address
    except: print("Error: Address cannot be determined")


def modify_address_of_user(user_index):
    try: 
        address_modified = input("Change the address to: ")
            
        # Checks if IP address is valid
        valid_ip = re.match(r"^(25[0-5]|2[0-4]\d|[01]?\d\d?)\.(25[0-5]|2[0-4]\d|[01]?\d\d?)\.(25[0-5]|2[0-4]\d|[01]?\d\d?)\.(25[0-5]|2[0-4]\d|[01]?\d\d?)$", address_modified)
        
        if valid_ip:
            [address_arr, descriptions_arr] = fetch_data()
            for index, address in enumerate(address_arr):
                if user_index == index: address_arr[index] = address_modified
            
            # JSON file
            alias = {
                        "address": address_arr,
                        "id": alias_name,
                        "name": alias_name,
                        "type": "host"
                    } 
            response = requests.put(url, json=alias, headers=headers, verify=False)
        
            print("\nUpdated List:")
        else: print("Error: Enter a valid IP Address")
        
        for x in range(len(address_arr)): print(f"{address_arr[x]}: {descriptions_arr[x]}")
    
    except: print("Error: Address cannot be modified")

