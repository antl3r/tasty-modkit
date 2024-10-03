import subprocess
import os
import json
import requests
from modlist_downloader import download_from_modlist
from verify_mods import check_missing
from prompt_user import yes_no_prompt

# Get the current script's directory
modkit_directory = os.path.dirname(os.path.abspath(__file__))

# Get the parent directory
mod_directory = os.path.dirname(modkit_directory)

# Define the path to your SteamCMD executable
steamcmd_directory = os.path.abspath(os.path.join(mod_directory, os.pardir, os.pardir, os.pardir, os.pardir))
steamcmd_exe = os.path.abspath(os.path.join(steamcmd_directory, "steamcmd.exe"))

#Grab AppID from mods directory
app_id = os.path.basename(mod_directory) 

print("\n" + steamcmd_directory + "\n")

missing_ids = check_missing(mod_directory)

if missing_ids:
    if missing_ids:
        if yes_no_prompt("There are missing mods! Would you like to download them now?"):
            download_from_modlist(missing_ids, steamcmd_exe, app_id)
        else:
            print("Exiting...")
    else:
        print("No mods are missing! Quitting this program now...")