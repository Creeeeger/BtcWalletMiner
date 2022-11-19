import random
import string
import hashlib
import binascii
import base58

# Constants
VALID_WALLET_MESSAGE = "Wallet found!"
INVALID_WALLET_MESSAGE = "Wallet not found!"

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

