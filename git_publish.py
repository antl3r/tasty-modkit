import requests
import json
import configparser

config = configparser.ConfigParser()

config.read("./options.cfg")

def publish_github(json_file_path):
    # Fetch options
    GITHUB_TOKEN = config['GITHUB']['GITHUB_TOKEN']
    GIST_ID = config['GITHUB']['GIST_ID']
    FILE_NAME = config['GITHUB']['FILE_NAME']
    
    print(GITHUB_TOKEN)
    print(GIST_ID)
    print(FILE_NAME)

    # Read the JSON file content
    with open(json_file_path, 'r') as json_file:
        json_content = json_file.read()

    # The API endpoint for the Gist
    url = f'https://api.github.com/gists/{GIST_ID}'

    # Create the headers
    headers = {
        'Authorization': f'token {GITHUB_TOKEN}',
        'Accept': 'application/vnd.github.v3+json',
    }

    data = {
        'files': {
            FILE_NAME: {
                'content': json_content
            }
        }
    }

    # Make the PATCH request
    response = requests.patch(url, headers=headers, json=data)

    # Check the response
    if response.status_code == 200:
        print("Gist updated successfully.")
        print(response.json())
    else:
        print(f"Failed to update Gist. Status code: {response.status_code}")
        print(response.json())
        raise Exception("Failed to update Gist")