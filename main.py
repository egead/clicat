import os
import random
import json
import time
import argparse
from datetime import datetime, timedelta
from clicat import CliCat
from pet_ascii import PET_HAPPY, PET_HUNGRY, PET_SLEEPY, PET_SICK, PET_PLAYING

def main():
    parser = argparse.ArgumentParser(description='CLI Virtual Pet')
    parser.add_argument('--feed', action='store_true', help='Feed your pet')
    parser.add_argument('--play', action='store_true', help='Play with your pet')
    parser.add_argument('--rest', action='store_true', help='Let your pet rest')
    parser.add_argument('--heal', action='store_true', help='Give medicine to your pet')
    parser.add_argument('--rename', type=str, help='Rename your pet')
    parser.add_argument('--status', action='store_true', help='Check your pet status (default if no args)')
    
    args = parser.parse_args()
    
    pet = CliCat()
    
    if args.feed:
        pet.feed()
    elif args.play:
        pet.play()
    elif args.rest:
        pet.rest()
    elif args.heal:
        pet.heal()
    elif args.rename:
        pet.rename(args.rename)
    else:  
        pass 
    
    pet.display()
    pet.save_state()

if __name__ == "__main__":
    main()