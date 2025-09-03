import requests
import time
import colorama
from colorama import Fore, Style

ascii_art = r"""
 /$$   /$$  /$$$$$$  /$$      
| $$$ | $$ /$$__  $$| $$      
| $$$$| $$| $$  \__/| $$      
| $$ $$ $$| $$ /$$$$| $$      
| $$  $$$$| $$|_  $$| $$      
| $$\  $$$| $$  \ $$| $$      
| $$ \  $$|  $$$$$$/| $$$$$$$$
|__/  \__/ \______/ |________/
                              
                              
"""
print(Fore.LIGHTGREEN_EX + ascii_art)

print(Fore.MAGENTA + "Welcome to NGL Spammer!,\nIf this tool doesn't detect buttons, please replace images.")

requestUrl = "https://ngl.link/api/submit"

while True:
    USERNAME = input(Fore.LIGHTBLUE_EX + "Enter NGL Username: " + Fore.WHITE)
    text = input(Fore.LIGHTBLUE_EX + "Enter Message: " + Fore.WHITE)
    quantifier = int(input(Fore.LIGHTBLUE_EX + "Enter Message Amount: " + Fore.WHITE))

    header = {
        'username': USERNAME,
        'question': text,
        'deviceId': '',
        'gameSlug': '',
        'referrer': ''
    }

    for i in range(quantifier):
        try:
            response = requests.post(requestUrl, data=header, timeout=10)
            print(Fore.YELLOW + f"Sent {i + 1}/{quantifier} messages to {USERNAME}")
        except requests.exceptions.RequestException as e:
            print(Fore.red + e)

    print(Fore.GREEN + "Completed spamming to " + USERNAME)
