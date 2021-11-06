import pytest
import dotenv
import os
from blab.sentinel import Ftp
dotenv.load_dotenv(os.path.join(os.path.dirname(__file__), '../.env'))
o = Ftp()


def test_ftp_uid():
    assert os.environ.get('ftp_uid') is not None, "FTP UID not found"


def test_ftp_pwd():
    assert os.environ.get('ftp_pwd') is not None, "FTP PWD not found"


def test_ftp_connect():
    o.connect(os.environ.get('ftp_uid'), os.environ.get('ftp_pwd'))
    assert o.logged_in, "Could not login"


def test_ftp_list_all():
    assert len(o.list_patches()) > 0, "Could not list dir"


def test_ftp_list_quebec_family():
    all_quebec = True
    for q in o.list_patches("glide*quebec*.*"):
        if "quebec" not in q:
            all_quebec = False
            break

    assert all_quebec, "Incorrect family returned"


def test_ftp_disconnect():
    assert o.disconnect(), "Could not disconnect"
