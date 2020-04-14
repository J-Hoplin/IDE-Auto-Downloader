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

class downloadVisualStudioCode:
    IDEName = 'Visual Studio Code'
    directoryName = 'Visual Studio Code'
    def download32bit(self):
        url32bit = 'https://go.microsoft.com/fwlink/?LinkID=623231'
        Downloader(self.directoryName,self.IDEName,url32bit)
    def download64bit(self):
        url64bit = 'https://go.microsoft.com/fwlink/?Linkid=850641'
        Downloader(self.directoryName,self.IDEName,url64bit)