
import os
import requests
import pyshorteners
while True:
    uurl = input("Username: ")
    os.system('cls')
    s = pyshorteners.Shortener()
    pr9 = (s.dagd.short(uurl))
    print(pr9)