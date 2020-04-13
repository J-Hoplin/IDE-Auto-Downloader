from bs4 import BeautifulSoup
from urllib.request import urlopen
import zipfile
from io import BytesIO
import subprocess
import requests
import platform
import os
import time

#This module directory
dirNow = os.getcwd()

class downloadPython37:
    def Downloader(self,URL):
        try:
            print("Now downloading Python3.7.6... \nIt'll take some minutes....")
            sublimeWebURL = URL
            # 'https://go.microsoft.com/fwlink/?Linkid=850641'
            mkSublimeDirectory = dirNow + "\\" + 'Python376'
            os.mkdir(mkSublimeDirectory)
            fp = requests.get(sublimeWebURL)
            z = zipfile.ZipFile(BytesIO(fp.content))
            z.extractall(mkSublimeDirectory)
        except FileExistsError as e:
            print("File name 'Python376' already exist. Please check again.")
    def download32bit(self):
        url32bit = 'https://www.python.org/ftp/python/3.7.6/python-3.7.6-embed-win32.zip'
        self.Downloader(url32bit)
    def download64bit(self):
        url64bit = 'https://www.python.org/ftp/python/3.7.6/python-3.7.6-embed-amd64.zip'
        self.Downloader(url64bit)