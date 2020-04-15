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

class downloadPhantomJS:
    IDEName = 'Phantom JS'
    directoryName = 'PhantomJS'

    def download32bit(self):
        url32bit = 'https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-windows.zip'
        Downloader(self.directoryName,self.IDEName,url32bit)
    def download64bit(self):
        url64bit = 'https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-windows.zip'
        Downloader(self.directoryName,self.IDEName,url64bit)