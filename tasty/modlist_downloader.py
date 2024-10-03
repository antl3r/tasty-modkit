import subprocess
import json

def download_from_modlist(mod_ids: list, steamcmd_path, appid):

    # Build the SteamCMD command string with all workshop download commands
    cmd = [
        steamcmd_path,
        "+login", "anonymous"  # Login anonymously, or provide credentials if needed
    ]

    # Add all workshop download commands to the command list
    for workshop_id in mod_ids:
        cmd += ["+workshop_download_item", appid, workshop_id]

    # Add the quit command at the end to exit SteamCMD after downloads
    cmd.append("+quit")

    # Run the bulk command via subprocess
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error during the bulk download: {e}")