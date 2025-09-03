import requests
import time
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

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

print(Fore.MAGENTA + "Welcome to NGL Spammer!,\nMessage post speed is up to your internet.")

requestUrl = "https://ngl.link/api/submit"

while True:
    USERNAME = input(Fore.LIGHTBLUE_EX + "Enter NGL Username: " + Fore.WHITE)
    text = input(Fore.LIGHTBLUE_EX + "Enter Message: " + Fore.WHITE)
    quantifier = int(input(Fore.LIGHTBLUE_EX + "Enter Message Amount: " + Fore.WHITE))

    payload = {
        'username': USERNAME,
        'question': text,
        'deviceId': '',
        'gameSlug': '',
        'referrer': ''
    }

    for i in range(quantifier):
        while True:
            try:
                response = requests.post(requestUrl, data=payload, timeout=10)

                if response.status_code == 200:
                    print(Fore.YELLOW + f"✅ Sent {i + 1}/{quantifier} messages to {USERNAME}")
                    break
                else:
                    print(Fore.RED + f"❌ NGL.link API endpoint exhausted, retrying...")
            except requests.exceptions.RequestException as e:
                print(Fore.RED + f"⚠️ Network error: {e}, retrying...")

            time.sleep(2)

    print(Fore.GREEN + f"🎉 Completed spamming to {USERNAME}")
