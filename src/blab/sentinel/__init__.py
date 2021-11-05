import os, json
from ftplib import FTP, error_perm

class Ftp:
    '''Handles FTP communications with ServiceNow FTP Server'''

    def __init__(self) -> None:
        self.logged_in = False
        self._patches = []

    def connect(self, uid, pwd):
        try:
            self.svr = FTP('ftp.service-now.com')
            if self.svr.login(uid, pwd)[:3] == '230':
                print('[ + ] Successfully Logged In')
                self.logged_in = True
        except error_perm:
            print("[ - ] Could not connect")
    

    def disconnect(self):
        if not self.logged_in:
            return False

        if self.svr.quit()[:3] == '221':
            print("[ + ] Disconnected")
            return True


    def get_patches(self, filter=""):
        if not self.logged_in:
            print("[ - ] Not logged in")
            return False
        
        self._patches = self.svr.nlst(filter)
        return True


    def list_patches(self, filter=""):
        if self.get_patches(filter):
            return self._patches
        return []
