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
VALID_WALLET_MESSAGE = "Wallet found!"
INVALID_WALLET_MESSAGE = "Wallet not found!"
WITHDRAWING_MESSAGE = "Initialise withdrawing to your Wallet..."
WITHDRAWING_DONE_MESSAGE = "Initialising done!"

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

