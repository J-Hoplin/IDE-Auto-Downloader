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

class downloadSublimeText3:
    def Downloader(self,URL):
        try:
            print("Now downloading Sublime Text3... \nIt'll take some minutes....")
            sublimeWebURL = URL
            # 'https://go.microsoft.com/fwlink/?Linkid=850641'
            mkSublimeDirectory = dirNow + "\\" + 'Sublime Text3'
            os.mkdir(mkSublimeDirectory)
            fp = requests.get(sublimeWebURL)
            z = zipfile.ZipFile(BytesIO(fp.content))
            z.extractall(mkSublimeDirectory)
        except FileExistsError as e:
            print("File name 'Sublime Text3' already exist. Please check again.")
    def download32bit(self):
        url32bit = 'https://download.sublimetext.com/Sublime Text Build 3211.zip'
        self.Downloader(url32bit)
    def download64bit(self):
        url64bit = 'https://download.sublimetext.com/Sublime Text Build 3211 x64.zip'
        self.Downloader(url64bit)
