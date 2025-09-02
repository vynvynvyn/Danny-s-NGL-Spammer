import pyautogui
import webbrowser
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

def findImage(image_path, confidence=0.8):
    position = pyautogui.locateOnScreen(image_path, confidence=confidence)
    if position:
        return pyautogui.center(position)
    return None

while True:
    url = input(Fore.LIGHTBLUE_EX + "Enter NGL Link: " + Fore.WHITE)
    text = input(Fore.LIGHTBLUE_EX + "Enter Message: " + Fore.WHITE)
    quantifier = int(input(Fore.LIGHTBLUE_EX + "Enter Message Amount: " + Fore.WHITE))

    if url and text and quantifier > 0:
        webbrowser.open(url)
        time.sleep(1)
        for i in range(quantifier - 1): 
            pyautogui.moveTo(945,245)
            pyautogui.click()
            pyautogui.write(text)

            submit= findImage('Images/sendbtn.png')
            if submit:
                pyautogui.moveTo(submit)
                pyautogui.click()
                time.sleep(1)
                newmsg = findImage('Images/newmsg.png')
                if newmsg:
                    pyautogui.moveTo(newmsg)
                    pyautogui.click()
                    print(f"{Fore.YELLOW}Sent {i + 1} messages...")
                    time.sleep(0.5)

        print(f"{Fore.LIGHTGREEN_EX}Sent {quantifier} messages to {url}.")