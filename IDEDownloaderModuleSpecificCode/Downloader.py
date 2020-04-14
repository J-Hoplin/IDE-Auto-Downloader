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

def Downloader(directoryName,IDEName,url):
    try:
        print("Now downloading " + IDEName+"...\nIt'll take some minutes....")
        URL = url
        mkDirectory = dirNow + "\\" + directoryName
        os.mkdir(mkDirectory)
        fp = requests.get(URL)
        z = zipfile.ZipFile(BytesIO(fp.content))
        z.extractall(mkDirectory)
        print("Complete to download " + IDEName + ".")
        time.sleep(3)
    except FileExistsError as e:
        print("File name \'" + directoryName + "\' already exist. Please check again.")
        print("Download fail. Go back to menu...")
        time.sleep(3)