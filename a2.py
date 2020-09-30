import sys
import hashlib

x = hashlib.sha1()
x.update(b"Test string!")
x.hexdigest()

x = hashlib.sha256()
x.update(b"second test string!")
x.hexdigest()

x = hashlib.md5()
x.update(b"third test string!")
x.hexdigest()

filename = input("Input file name: ")
with open(filename, "rb") as f:
    text = f.read()
H1 = hashlib.sha256(text)
H1.hexdigest()

filename = input("Input file name: ")
with open(filename, "rb") as f:
    text = f.read()
H2 = hashlib.sha256(text)
H2.hexdigest()