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

class downloadSublimeText3:
    IDEName = 'Sublime Text3'
    directoryName = 'Sublime Text3'
    def download32bit(self):
        url32bit = 'https://download.sublimetext.com/Sublime Text Build 3211.zip'
        Downloader(self.directoryName,self.IDEName,url32bit)
    def download64bit(self):
        url64bit = 'https://download.sublimetext.com/Sublime Text Build 3211 x64.zip'
        Downloader(self.directoryName,self.IDEName,url64bit)
