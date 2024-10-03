import os
import json
import re
from prompt_user import yes_no_prompt
from git_publish import publish_github

def export_modlist_json(mods_directory):
    mod_ids = [d for d in os.listdir(mods_directory) 
            if os.path.isdir(os.path.join(mods_directory, d)) and re.match(r'^\d', d)]

    output_data = {"mod_ids": mod_ids}

    output_file_path = 'modlist_output.json'

    # Write the output data to a JSON file
    with open(output_file_path, 'w') as json_file:
        json.dump(output_data, json_file, indent=4)

    print(f"JSON file created: {output_file_path}")

    if yes_no_prompt("Would you like to publish this to your gist?"):
        print("Publishing...")
        try:
            publish_github(output_file_path)
        except:
            print("\n" + "An error has occured! The gist was not updated.")
        else:
            print("\n" + f"Success! {output_file_path} was uploaded to the gist.")