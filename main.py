from aliasmodify import *

    
[address_arr, descriptions_arr] = fetch_data()
user = input("\nSpecify the name of the user to be whitelisted: ")
user_index = find_index_of_user(descriptions_arr, user)
user_address = find_address_of_user(address_arr, user_index)
modify_address_of_user(user_index)