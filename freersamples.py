#!/usr/bin/python3
import requests
import json
import logging
from termcolor import colored
from colorlog import ColoredFormatter
import argparse
import os,sys

VERSION = '0.2.0'

DEFAULT_SAMPLES_PATH = 'data/samples.json'

BANNER = '''

  _____                                                         .__                 
_/ ____\______  ____  ___________    __________    _____ ______ |  |   ____   ______
\   __\\_  __ \/ __ \/ __ \_  __ \  /  ___|__  \  /     \\____ \|  | _/ __ \ /  ___/
 |  |   |  | \|  ___|  ___/|  | \/  \___ \ / __ \|  Y Y  \  |_> >  |_\  ___/ \___ \ 
 |__|   |__|   \___  >___  >__|    /____  >____  /__|_|  /   __/|____/\___  >____  >
                   \/    \/             \/     \/      \/|__|             \/     \/ 

'''

def get_args():
    parser = argparse.ArgumentParser(description="FreerSamples - A tool for maximising juice per squeeze.")
    parser.add_argument('--version', action='version', version=VERSION, help='Show version information')
    parser.add_argument('-s', '--silent', action='store_true', help='Silent output')
    parser.add_argument('-d', '--debug', action='store_true', help='Enable debug mode')    
    parser.add_argument('-i', '--input-file', help='Input JSON file containing sample data')
    
    args = parser.parse_args()
    
    return args

def setup_logger(args):
    """
    Sets up verbose/debug logging with colour formatting.
    """
    
    formatter = ColoredFormatter(
    "[%(log_color)s%(levelname)s%(reset)s] %(message)s",
    log_colors={
        "DEBUG":    "cyan",
        "INFO":     "green",
        "WARNING":  "yellow",
        "ERROR":    "red",
        "CRITICAL": "bold_red",
    })
    
    logger = logging.getLogger()
    
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.handlers = []  # Clear existing handlers
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG if args.debug else (logging.WARNING if args.silent else logging.INFO))

    return logger 

def add_item(path, samples):
    
    logger = logging.getLogger()
    
    logger.info("Prompting for new machine data...")
    
    name = input("Please enter the " + colored("name", "light_magenta", attrs=["bold"]) + " of the product/company for future reference: ")
    url = input("Please enter the " + colored("URL", "light_magenta", attrs=["bold"]) + " of the machine's QR code: ")
    
    # TODO: Validate the URL through a dummy req
    
    item = {"name": name, "url": url}
    samples.append(item)
    
    with open(path, 'w') as f:
        logger.info(f"Writing to {path}...")
        json.dump(samples, f, indent=4)

    return item

def choose_item(path):
    
    logger = logging.getLogger()
    
    path = path or DEFAULT_SAMPLES_PATH
    
    if not os.path.exists(path):
        logger.error(f"The JSON sample data at {path} does not exist.")
        sys.exit(1)
    else:
        with open(path) as f:
            try:
                samples = json.load(f)
            except Exception as e:
                logger.error(f"The JSON data at {path} is malformed and cannot be parsed.")
                sys.exit(1)
                
        print("Please select one of the following (e.g. 1 for Burberry), or alternatively type " + colored("add", "light_magenta", attrs=["bold"]) + " to add a new machine:")
        [print(f"{i}) {item['name']}") for i, item in enumerate(samples)]
        while True:
            choice = input("Choice: ")
            try: 
                if choice == "add":
                    chosen_item = add_item(path, samples)
                elif choice in ["exit", "quit", "q"]:
                    logger.info("Exiting...")
                    sys.exit(0)
                else:
                    chosen_item = samples[int(choice)]
                break
            
            except Exception as e:
                print("Bad choice! Try again...")
                continue
        
        return chosen_item["name"], chosen_item["url"]                
    

def main():
    
    args = get_args()
    
    print(colored(BANNER, 'light_magenta'))
    
    logger = setup_logger(args)
    
    logger.debug(f"got args {args}")
    
    name, url = choose_item(args.input_file)

    slugs = url.split("/")

    qrKey = slugs[-3]
    deviceKey = slugs[-2]
    check = slugs[-1]
    site = url.split(qrKey)[0]

    # Call API
    logger.info(f"Calling {name} API...")
    try:
        req = requests.get(site + f"api/survey?qrkey={qrKey}&deviceKey={deviceKey}&check={check}")
    except Exception as e:
            logger.error(f"Failed to reach the {name} API")
            exit(1)

    logger.info(f"Got session variables...")
    sessionVars = req.json()
    
    logger.debug(sessionVars)

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
        logger.debug(f"\n{push.content}")
    except Exception as e:
        logger.error("Failed to submit \"answers\" to the API. No free samples :(")
        exit(1)

    logger.info("Successfully submitted answers to the API. Pick your poison >:)")
    
    
if __name__ == '__main__':
    main()