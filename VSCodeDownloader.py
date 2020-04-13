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

class downloadVisualStudioCode:
    def Downloader(self,URL):
        try:
            print("Now downloading Visual Studio Code... \nIt'll take some minutes....")
            sublimeWebURL = URL
            # 'https://go.microsoft.com/fwlink/?Linkid=850641'
            mkSublimeDirectory = dirNow + "\\" + 'Visual Studio Code'
            os.mkdir(mkSublimeDirectory)
            fp = requests.get(sublimeWebURL)
            z = zipfile.ZipFile(BytesIO(fp.content))
            z.extractall(mkSublimeDirectory)
        except FileExistsError as e:
            print("File name 'Visual Studio Code' already exist. Please check again.")
    def download32bit(self):
        url32bit = 'https://go.microsoft.com/fwlink/?LinkID=623231'
        self.Downloader(url32bit)
    def download64bit(self):
        url64bit = 'https://go.microsoft.com/fwlink/?Linkid=850641'
        self.Downloader(url64bit)