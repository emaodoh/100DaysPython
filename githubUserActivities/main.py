from urllib.request import urlopen
from urllib.error import HTTPError, URLError
import sys
import json


def fetch(user_name):
    url = f"https://api.github.com/users/{user_name}/events"

    try:
        response = urlopen(url)
        

    except HTTPError as e:
        if e.code == 404:
            print("user not found")
        
        return

    except URLError as e:
        print("Http error", e.reason)
        return 

    events = json.load(response)

    

    if not events:
         
        print(f"{user_name} has no recent public activity")
        return

    for event in events:

        event_type = event["type"]

        if event_type == "PushEvent":
            payload = event["payload"]
            
            commit = payload.get("commits")

            if commit:
                print(f"\n{commit}\n")
                print("-" * 40)
            else:
                print("\nNo commit message found\n")
                print("-" * 40)

        

        repo = event.get("repo", None)
        if repo:
            repo = repo.get("name")
        else:
            repo = "No repository found"

        repo_type = event.get("public",None)

        if repo_type:
            repo_type = "public"
        else:
            repo_type = "private"
        creation_date = event.get("created_at", None)

        if event_type and creation_date and repo_type and repo:
            print(f"Type of event {event_type}  Created at {creation_date} repository name {repo} and it is a {repo_type} repo")
        
    
if len(sys.argv) != 2:
    print("usage: <file_name.py> <user_name>")
    sys.exit(1)

user_name = sys.argv[1]

fetch(user_name)