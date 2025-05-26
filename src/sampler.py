import requests
from colorama import Fore, Back, Style
import json

BANNER = '''

  _____                                                         .__                 
_/ ____\______  ____  ___________    __________    _____ ______ |  |   ____   ______
\   __\\_  __ \/ __ \/ __ \_  __ \  /  ___|__  \  /     \\____ \|  | _/ __ \ /  ___/
 |  |   |  | \|  ___|  ___/|  | \/  \___ \ / __ \|  Y Y  \  |_> >  |_\  ___/ \___ \ 
 |__|   |__|   \___  >___  >__|    /____  >____  /__|_|  /   __/|____/\___  >____  >
                   \/    \/             \/     \/      \/|__|             \/     \/ 

'''


URL = "https://burberry.freesamples.net.au/TRSYULK8/WFXXJZ/5" # Replace this with QR code URL

def announce(msg: str, err=False):
    print(f"{Fore.GREEN + '[+' if not err else Fore.RED + '[-'}]{Fore.RESET} {msg}")    

slugs = URL.split("/")

qrKey = slugs[-3]
deviceKey = slugs[-2]
check = slugs[-1]
site = URL.split(qrKey)[0]

print(BANNER)
# Call API
announce("Calling API...")
try:
    req = requests.get(site + f"api/survey?qrkey={qrKey}&deviceKey={deviceKey}&check={check}")
except Exception as e:
        announce("Failed to reach the Freesamples API", True)
        exit(1)

announce(f"Got session variables...")
sessionVars = req.json()

data = {
    "qrKey": qrKey,
    "deviceKey": deviceKey,
    "check": check,
    "session": sessionVars["session"],
    "yoke": sessionVars["yoke"],
    "answers": []
}


try:
    push = requests.post(site + "api/survey", json=data)
except Exception as e:
    announce("Failed to submit \"answers\" to the API. No free samples :(", True)
    exit(1)

announce("Successfully submitted answers to the API. Pick your poison >:)")



#req = requests.get()


# Get 