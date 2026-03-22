import threading
import random
import string
import json
import datetime
import secrets
import hmac
import hashlib
import base64
import uuid
import bcrypt

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from secret_key_generator import secret_key_generator
from keycove import hash, generate_token, encrypt, decrypt, generate_secret_key
from cryptography.fernet import Fernet
from generateApiKey import generateApiKey
from nanoid import generate
from sqids import Sqids

sqids = Sqids(min_length=24)

def password_hash(plain: str):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(plain.encode(), salt)

def password_check(check: str, hashed: str):
    return bcrypt.checkpw(check.encode(), hashed.encode())


def md5_hash(value: str) -> str:
    return hashlib.md5(value.encode('utf-8')).hexdigest()

def sha1_hash(value: str) -> str:
    return hashlib.sha1(string=value.encode('utf-8')).hexdigest()

def sha256_hash(value: str) -> str:
    return hash(value)

def hashid_encode(id: int) -> str:
    return sqids.encode([id])

def hashid_decode(id: str) -> int:
    return sqids.decode(id)[0]

async def generate_api_key(secret: str, dashes: bool = False) -> str:
    seed = uuid.uuid4()
    api_key = await generateApiKey(secret=secret, seed=seed, add_dashes=dashes)
    return api_key

def generate_api_key_secret(length) -> str:
    char_set = string.ascii_letters + string.punctuation                    
    urand = random.SystemRandom()                                           
    return ''.join([urand.choice(char_set) for _ in range(length)])

def generate_random_secret_key() -> str:
    secret = generate_secret_key()
    return secret

def generate_random_token(length: int = 16) -> str:
    return generate_token(length)


def generate_request_id() -> str:
    return generate(size=32)

    
    

    
    

    