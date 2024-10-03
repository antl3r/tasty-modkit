import os
import requests
import re
import json
from prompt_user import yes_no_prompt
from modlist_downloader import download_from_modlist

def check_missing(mod_directory):
    app_id = os.path.basename(mod_directory)
    
    steamcmd_directory = os.path.abspath(os.path.join(mod_directory, os.pardir, os.pardir, os.pardir, os.pardir))
    steamcmd_exe = os.path.abspath(os.path.join(steamcmd_directory, "steamcmd.exe"))
    
    url = 'https://gist.githubusercontent.com/antl3r/a95bff1abe7378e7f96f351fd039f77b/raw/7be76aad36039d2e71c477d58d8146a5565b886c/modlist_output.json'
    
    response = requests.get(url)

    # Load the JSON data into mod_ids
    if response.status_code == 200:
        data = response.json()
        mod_ids = data.get("mod_ids", [])
    else:
        print(f"Failed to fetch the JSON file. Status code: {response.status_code}")
        mod_ids = []

    subdirectories = [
        d for d in os.listdir(mod_directory)
        if os.path.isdir(os.path.join(mod_directory, d)) and re.match(r'^\d', d)
    ]

    mod_ids_set = set(mod_ids)  # Convert to set for faster lookups
    subdirectories_set = set(subdirectories)  # Convert to set for faster lookups

    # Find missing and existing subdirectories
    missing_mod_ids = mod_ids_set - subdirectories_set

    if missing_mod_ids:
        print("Missing subdirectories (from mod_ids):")
        for mod_id in missing_mod_ids:
            print(mod_id)
            
        if yes_no_prompt("There are missing mods! Would you like to download them now?"):
            download_from_modlist(missing_mod_ids, steamcmd_exe, app_id)
        else:
            print("Exiting...")
    else:
        print("No subdirectories from mod_ids are missing!")
        
    return missing_mod_ids