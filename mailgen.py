# mailgen.py

# Banner Information
BANNER = """
███    ███  █████  ██ ██       ██████  ███████ ███    ██ 
████  ████ ██   ██ ██ ██      ██       ██      ████   ██ 
██ ████ ██ ███████ ██ ██      ██   ███ █████   ██ ██  ██ 
██  ██  ██ ██   ██ ██ ██      ██    ██ ██      ██  ██ ██ 
██      ██ ██   ██ ██ ███████  ██████  ███████ ██   ████ 
┌─────────────────────────────────────────────────────┐
│ Version: 0.5 │ Github: @fernstedt | Created by math0x │
└─────────────────────────────────────────────────────┘
"""
print(BANNER)  # Print the banner at the start

import sys
import random
import requests  # Add this import

def load_names(file_paths):
    names = []
    for file_path in file_paths:
        if file_path.startswith('http'):
            response = requests.get(file_path)  # Fetch the content from the URL
            names = response.text.splitlines()  # Split the content into lines
        else:
            with open(file_path, 'r') as file:
                names = file.readlines()  # Read from the file
    return names

def load_hosts(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def generate_emails(first_names, last_names, hosts, num_emails):
    emails = []
    for _ in range(num_emails):  # Generate specified number of emails
        first_name = random.choice(first_names).lower()  # Convert to lowercase
        last_name = random.choice(last_names).lower()    # Convert to lowercase
        host = random.choice(hosts).lower()              # Convert to lowercase
        
        # Generate different email formats
        emails.append(f"{first_name}.{last_name}@{host}")
        emails.append(f"{first_name}{last_name}@{host}")

    return emails

def save_emails(emails, output_file):
    with open(output_file, 'w') as file:
        for email in emails:
            file.write(email + '\n')

def print_help():
    help_text = """
Usage: python mailgen.py [options]

Options:
  -h            Show this help message and exit
  -n <number>   Specify the number of emails to create (default: 100)
  -o <file>     Specify the output file name (default: emails.txt)

Example:
  python mailgen.py -n 50 -o my_emails.txt
"""
    print(help_text)

def main():
    # Default values
    num_emails = 100
    output_file = 'emails.txt'

    # Command-line argument parsing
    args = sys.argv[1:]
    for i in range(len(args)):
        if args[i] == '-h':
            print_help()
            return
        elif args[i] == '-n' and i + 1 < len(args):
            num_emails = int(args[i + 1])
        elif args[i] == '-o' and i + 1 < len(args):
            output_file = args[i + 1]

    first_name_files = [
        'https://raw.githubusercontent.com/fernstedt/SecLists/master/Usernames/Names/femalenames-usa-top1000.txt',
        'https://raw.githubusercontent.com/fernstedt/SecLists/master/Usernames/Names/forenames-india-top1000.txt',
        'https://raw.githubusercontent.com/fernstedt/SecLists/master/Usernames/Names/malenames-usa-top1000.txt',
        'https://raw.githubusercontent.com/fernstedt/SecLists/master/Usernames/Names/names.txt'
    ]  # Add more paths as needed
    last_names = load_names(['https://raw.githubusercontent.com/fernstedt/SecLists/master/Usernames/Names/familynames-usa-top1000.txt'])  # Update with actual path
    hosts = load_hosts('hosts.txt')  # Update the path to the correct location

    first_names = load_names(first_name_files)
    emails = generate_emails(first_names, last_names, hosts, num_emails)
    save_emails(emails, output_file)

if __name__ == "__main__":
    main()
