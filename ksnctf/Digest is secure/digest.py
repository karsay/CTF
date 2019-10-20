import requests
import hashlib
from bs4 import BeautifulSoup as bs

url = "http://ctfq.sweetduet.info:10080/~q9/flag.html"

md5a1 = "c627e19450db746b739f41b64097d449"
nonce = ""
nc = "00000001"
cnonce = "5f70c9b7a0f15b7d"
pop = "auth"
a2 = "GET:/~q9/flag.html"
md5a2 = "ffffdd8b8029499600f95a69beb239c2"

username = "q9"
realm = "secret"
algorithm = "MD5"
uri = "/~q9/flag.html"

def get_md5(arg):
    return hashlib.md5(arg.encode("utf-8")).hexdigest()