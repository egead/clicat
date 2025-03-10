import os
import random
import json
import time
import argparse
from datetime import datetime, timedelta
from clicat import CliCat

# ASCII Art for different pet states
PET_HAPPY = r"""
   /\_/\  
  ( ^.^ ) 
   > ^ <  
"""

PET_HUNGRY = r"""
   /\_/\  
  ( o.o ) 
  ( u u ) 
"""

PET_SLEEPY = r"""
   /\_/\  
  ( -.- ) 
   z z z  
"""

PET_SICK = r"""
   /\_/\  
  ( x.x ) 
  ( - - ) 
"""

PET_PLAYING = r"""
   /\_/\  
  ( ^o^ ) 
  ( > < ) 
"""

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