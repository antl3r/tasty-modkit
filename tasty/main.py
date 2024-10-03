import argparse
from modlist_downloader import download_from_modlist
from verify_mods import check_missing
from prompt_user import yes_no_prompt
from export_modlist import export_modlist_json

def main():
    parser = argparse.ArgumentParser(description='Mod Sync Tool for Non-Steam Games')
    
    # Define subparsers for different commands
    subparsers = parser.add_subparsers(dest='command')

    # Subparser for mod check
    mod_check_parser = subparsers.add_parser('check', help='Check your mod folders')
    mod_check_parser.add_argument('--path', type=str, required=True, help='Path to the mod folder')

    # Subparser for uploading modlist to GitHub Gist
    upload_parser = subparsers.add_parser('upload', help='Export modlist / Upload modlist to GitHub Gist')
    upload_parser.add_argument('--path', type=str, required=True, help='Path to the mod folder')

    # Parse arguments
    args = parser.parse_args()

    # Execute commands based on user input
    if args.command == 'check':
        check_missing(args.path)
    elif args.command == 'upload':
        export_modlist_json(args.path)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()