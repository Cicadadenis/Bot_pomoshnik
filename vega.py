import ftplib
import re
import requests
from threading import Timer
from threading import *

host = 'vegaswork.cc'
ftp_user = 'cicada@vegaswork.cc'
ftp_password = 'Tramadol1989'
ftp = ftplib.FTP(host, ftp_user, ftp_password)


def sa():
    t1=Thread(target=sawe)
    t1.start()

def zagruzka():
    t1=Thread(target=dowl)
    t1.start()


def smena():
    t1=Thread(target=zamena)
    t1.start()


def sawe():
    local_file = "index.html"
    ftp_file  = "index.html"
    with open(local_file, 'wb') as local_file: 
        ftp.retrbinary('retr ' + ftp_file, local_file.write)
    ftp.close()

def dowl():
    file = "index.html"
    file_to_upload = open('index.html', 'rb')
    ftp.storbinary('STOR ' + file, file_to_upload)
    ftp.close()

def zamena(pattern, repl):
    local_file = "index.html"
    ftp_file  = "index.html"
    string = open("index.html", "r", encoding="utf-8").read()
    dd = re.sub(f"{pattern}", f"{repl}", string)
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(str(dd))



sa()



