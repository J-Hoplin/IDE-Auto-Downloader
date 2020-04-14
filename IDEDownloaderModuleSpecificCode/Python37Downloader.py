from bs4 import BeautifulSoup
from urllib.request import urlopen
import zipfile
from io import BytesIO
import subprocess
import requests
import platform
import os
import time
from Downloader import Downloader

#This module directory
dirNow = os.getcwd()

class downloadPython37:
    IDEName = 'Python 3.7.6'
    directoryName = 'Python376'

    def download32bit(self):
        url32bit = 'https://www.python.org/ftp/python/3.7.6/python-3.7.6-embed-win32.zip'
        Downloader(self.directoryName,self.IDEName,url32bit)
    def download64bit(self):
        url64bit = 'https://www.python.org/ftp/python/3.7.6/python-3.7.6-embed-amd64.zip'
        Downloader(self.directoryName,self.IDEName,url64bit)