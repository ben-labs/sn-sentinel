from ftplib import FTP, error_perm
import requests


class Ftp:
    '''Handles FTP communications with ServiceNow FTP Server'''

    def __init__(self) -> None:
        self.logged_in = False

    @property
    def patches(self):
        return self._patches

    @patches.setter
    def patches(self, props):
        self._patches = props

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

        self.patches = self.svr.nlst(filter)
        return True

    def list_patches(self, filter=""):
        if self.get_patches(filter):
            return self._patches
        return []


class Telegram:
    '''Handles telegram functions'''

    def __init__(self, token):
        """
        Initialize Token
        """
        self.last_processed_message = 0
        self.req = f"https://api.telegram.org/bot{token}/"

    def __request(self, resource, **kwargs):
        """
        Process Telegram API Request
        """
        if "data" in kwargs:
            r = requests.post(f"{self.req}{resource}", kwargs["data"]).json()
        else:
            r = requests.post(f"{self.req}{resource}").json()
        return r

    def send_message(self, chat_id, text, parse_mode='html'):
        """
        Sends a telegram message
        Can't send a message to a person if they do not already have an initial chat with you.
        """
        payload = {
            "chat_id": chat_id,
            "text": text,
            "parse_mode": parse_mode
        }
        result = self.__request("sendMessage", data=payload)
        return result
