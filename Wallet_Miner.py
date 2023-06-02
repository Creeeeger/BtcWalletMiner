import time
import random
import string
import hashlib
import binascii
import base58
from colorama import init, Fore

# Initialize colorama
init(convert=True)

# Constants
LICENSE_KEY = "mcabar2205"
VALID_WALLET_MESSAGE = "Wallet found!"
INVALID_WALLET_MESSAGE = "Wallet not found!"
WITHDRAWING_MESSAGE = "Initialise withdrawing to your Wallet..."
WITHDRAWING_DONE_MESSAGE = "Initialising done!"
TRIAL_MODE_MESSAGE = "Trial mode (without transfer keys + slow)"
WAIT_FOR_WITHDRAWAL_MESSAGE = "For withdrawing is the key required"
QUIT_MESSAGE = "Press Enter to quit!"

# Prompt for key input
def prompt_for_key():
    key_availability = input(Fore.RED + "Do you have a key? (y/n): ")
    return key_availability.lower() == "y"

# Check if wallet is valid
def is_valid_wallet(wallet):
    base58_decoder = base58.b58decode(wallet).hex()
    prefix_and_hash = base58_decoder[:len(base58_decoder) - 8]
    checksum = base58_decoder[len(base58_decoder) - 8:]
    hash_value = prefix_and_hash
    for _ in range(1, 3):
        hash_value = hashlib.sha256(binascii.unhexlify(hash_value)).hexdigest()
    return checksum == hash_value[:8]

# Generate a random wallet ID
def generate_wallet_id(size=33, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
    return "".join(random.choice(chars) for _ in range(size))

# Generate a random transaction ID
def generate_transaction_id(size=30, chars=string.digits + string.digits):
    return "".join(random.choice(chars) for _ in range(size))

# Print a colored output for a valid wallet
def print_valid_wallet(wallet_id, transaction_id, btc_amount):
    print(Fore.CYAN + "[-]" + Fore.GREEN + " 1" + wallet_id + Fore.GREEN + " |  Valid  |  " + Fore.GREEN + " |" + transaction_id + "|  " + str(round(random.uniform(0, 2), 4)), "BTC")
    print(Fore.GREEN + WITHDRAWING_MESSAGE)
    print(Fore.GREEN + "This takes up to 24 hours.")
    time.sleep(10)
    print(Fore.GREEN + WITHDRAWING_DONE_MESSAGE)

# Print a colored output for an invalid wallet
def print_invalid_wallet(wallet_id):
    print(Fore.CYAN + "[-]" + Fore.RED + " 1" + wallet_id + Fore.CYAN + " | InValid |  " + Fore.RED + " | No Transfer Key|  " + Fore.CYAN + "0.0000 BTC")

# Main program
def main():
    has_key = prompt_for_key()

    if has_key:
        license_key = input(Fore.RED + 'Input License Key: ')
        if license_key == LICENSE_KEY:
            print(Fore.GREEN + "Key is Valid!")
            time.sleep(0.5)
            wallet = input(Fore.RED + "Wallet: ")
            if is_valid_wallet(wallet):
                print(Fore.GREEN + VALID_WALLET_MESSAGE)
            else:
                print(Fore.RED + INVALID_WALLET_MESSAGE)
                exit()
            time.sleep(0.2)
            print(Fore.BLUE + "Setting up workspace for you...")
            time.sleep(3)
            tries = 0
            while True:
                if tries > random.randint(100, 200000000):
                    print_valid_wallet(generate_wallet_id(), generate_transaction_id(), round(random.uniform(0, 2), 4))
                    print(Fore.GREEN + WITHDRAWING_MESSAGE)
                    print(Fore.GREEN + "This takes up to 24 hours.")
                    time.sleep(10)
                    tries = 0
                    print(Fore.GREEN + WITHDRAWING_DONE_MESSAGE)
                    time.sleep(1)
                else:
                    print_invalid_wallet(generate_wallet_id())
                    tries += 1
        else:
            print(Fore.RED + "Invalid Key!")
            input(QUIT_MESSAGE)
            exit()
    else:
        print(TRIAL_MODE_MESSAGE)
        wallet = input(Fore.RED + "Wallet: ")
        if is_valid_wallet(wallet):
            print(Fore.GREEN + VALID_WALLET_MESSAGE)
        else:
            print(Fore.RED + INVALID_WALLET_MESSAGE)
            exit()
        time.sleep(0.2)
        print(Fore.BLUE + "Setting up workspace for you...")
        time.sleep(3)
        tries = 0
        while True:
            if tries > random.randint(100, 20000):
                print_valid_wallet(generate_wallet_id(), generate_transaction_id(), round(random.uniform(0, 2), 4))
                print(Fore.GREEN + WAIT_FOR_WITHDRAWAL_MESSAGE)
                time.sleep(10)
                tries = 0
            else:
                print_invalid_wallet(generate_wallet_id())
                time.sleep(0.2)
                tries += 1

# Run the main program
if __name__ == "__main__":
    main()
    input(QUIT_MESSAGE)

