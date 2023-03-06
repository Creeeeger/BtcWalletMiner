import time
import random
import string
import os
import hashlib
import binascii
import base58
from colorama import init, Fore
init(convert=True)
import subprocess, requests

keyav = input(Fore.RED + "Do you have a key? (y/n): ")

if keyav == "y":
    LicenseKey = input(Fore.RED + 'Input License Key: ') #Licence Key validation
    if LicenseKey == "mcabar2205":
        print(Fore.GREEN + "Key is Valid!")
        time.sleep(0.5)
        wallet = input(Fore.RED + "Wallet: ")               #input wallet
        base58Decoder = base58.b58decode(wallet).hex()      #check the checksum of wallet if it exists
        ("Base58 Decoder: ", base58Decoder)
        prefixAndHash = base58Decoder[:len(base58Decoder)-8]
        checksum = base58Decoder[len(base58Decoder)-8:]
        hash = prefixAndHash
        for x in range(1,3):
             hash = hashlib.sha256(binascii.unhexlify(hash)).hexdigest()
        if(checksum == hash[:8]):
              print(Fore.GREEN + "Wallet found!")
        else:
             print(Fore.RED + "Wallet not found!")
             exit()
        time.sleep(0.2)
        print(Fore.BLUE+ "Setting up workspace for you...")
        time.sleep(3)
        tries = 0
        def id_gen(size=33, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):  #define cryptic wallet string (size = length of string, chars = type of chars)
                return "".join(random.choice(chars) for _ in range(size))
        def id_trans(size=30, chars=string.digits + string.digits):  #define cryptic wallet string (size = length of string, chars = type of chars)
                return "".join(random.choice(chars) for _ in range(size))
        while(True):   
            if(tries > random.randint(100, 200000000)):                   # chance to get fake btc   
                print(Fore.CYAN +"[-]"+ Fore.GREEN + " 1" + id_gen() + Fore.GREEN +" |  Valid  |  " + Fore.GREEN +" |" + id_trans() +"|  " + str(round(random.uniform(0,2), 4)), "BTC") #create green valid string
                print(Fore.GREEN +"Initialise withdrawing to your Wallet...")               #Withdrawing Pause
                print(Fore.GREEN +"This takes up to 24 hours.")  
                time.sleep(10)
                tries = 0
                print(Fore.GREEN + "Initialising done!")
                time.sleep(1)
            else:
                print(Fore.CYAN +"[-]"+ Fore.RED + " 1" + id_gen() + Fore.CYAN +" | InValid |  " + Fore.RED +" | No Transfer Key|  " + Fore.CYAN+"0.0000 BTC") #create invalid wallet
                tries += 1
       
                from colorama import init, Fore

    else:
         print(Fore.RED + "Invalid Key!")                  #End when invalid
         print(Fore.RED + "Press Enter to quit!")
         input("")
         exit()
if keyav == "n":
    print("Trial mode (without transfer keys + slow)") #trial content
    wallet = input(Fore.RED + "Wallet: ")               #input wallet
    base58Decoder = base58.b58decode(wallet).hex()      #check the checksum of wallet if it exists
    ("Base58 Decoder: ", base58Decoder)
    prefixAndHash = base58Decoder[:len(base58Decoder)-8]
    checksum = base58Decoder[len(base58Decoder)-8:]
    hash = prefixAndHash
    for x in range(1,3):
          hash = hashlib.sha256(binascii.unhexlify(hash)).hexdigest()
    if(checksum == hash[:8]):
         print(Fore.GREEN + "Wallet found!")
    else:
         print(Fore.RED + "Wallet not found!")
         exit()
    time.sleep(0.2)
    print(Fore.BLUE+ "Setting up workspace for you...")
    time.sleep(3)
    tries = 0
    def id_gen(size=33, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):  #define cryptic wallet string (size = length of string, chars = type of chars)
            return "".join(random.choice(chars) for _ in range(size))
    while(True):   
            if(tries > random.randint(100, 20000)):                                             # chance to get fake btc   
                print(Fore.CYAN +"[-]"+ Fore.GREEN + " 1" + id_gen() + Fore.GREEN +" |  Valid  |  " + Fore.RED +" |Only in Pay Version|  " + str(round(random.uniform(0,2), 4)), "BTC") #create green valid string
                print(Fore.GREEN +"For withdrawing is the key required")                           #Withdrawing Pause
                time.sleep(10)
                tries = 0
            else:
                print(Fore.CYAN +"[-]"+ Fore.RED + " 1" + id_gen() + Fore.CYAN +" | InValid |  " + Fore.RED +" | No Transfer Key|  " +Fore.CYAN+"0.0000 BTC") #create invalid wallet
                time.sleep(0.2)
                tries += 1
       
                from colorama import init, Fore
else:
    exit()
