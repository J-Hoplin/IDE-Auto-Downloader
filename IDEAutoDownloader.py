from bs4 import BeautifulSoup
from urllib.request import urlopen
import zipfile
from io import BytesIO
import subprocess
import requests
import platform
import os
import sys
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

class downloadPython37:
    IDEName = ''
    directoryName = ''
    
    def __init__(self,IDEName,directoryName):
        self.IDEName = IDEName
        self.directoryName = directoryName
    
    def download32bit(self):
        url32bit = 'https://www.python.org/ftp/python/3.7.6/python-3.7.6-embed-win32.zip'
        Downloader(self.directoryName,self.IDEName,url32bit)
    def download64bit(self):
        url64bit = 'https://www.python.org/ftp/python/3.7.6/python-3.7.6-embed-amd64.zip'
        Downloader(self.directoryName,self.IDEName,url64bit)

class downloadVisualStudioCode:
    IDEName = ''
    directoryName = ''
    
    def __init__(self,IDEName,directoryName):
        self.IDEName = IDEName
        self.directoryName = directoryName
    
    def download32bit(self):
        url32bit = 'https://go.microsoft.com/fwlink/?LinkID=623231'
        Downloader(self.directoryName,self.IDEName,url32bit)
    def download64bit(self):
        url64bit = 'https://go.microsoft.com/fwlink/?Linkid=850641'
        Downloader(self.directoryName,self.IDEName,url64bit)

class downloadSublimeText3:
    IDEName = ''
    directoryName = ''
    def __init__(self,IDEName,directoryName):
        self.IDEName = IDEName
        self.directoryName = directoryName
    
    def download32bit(self):
        url32bit = 'https://download.sublimetext.com/Sublime Text Build 3211.zip'
        Downloader(self.directoryName,self.IDEName,url32bit)
    def download64bit(self):
        url64bit = 'https://download.sublimetext.com/Sublime Text Build 3211 x64.zip'
        Downloader(self.directoryName,self.IDEName,url64bit)
outerLoop = True


#Check PC platform type. This program only support Windows 32bit,64bit
platformChecker = platform.architecture()
#(bit,OS)

supportingIDEs = {
    1 : ['Sublime Text3',dST,'Sublime_Text3'],
    2 : ['Visual Studio Code',dVSC,'Visual_Studio_Code'],
    3 : ['Python 3.7.6',dPY3,'Python376']
}

dST = downloadSublimeText3(supportingIDEs[1][0],supportingIDEs[1][2])
dVSC = downloadVisualStudioCode(supportingIDEs[2][0],supportingIDEs[2][2])
dPY3 = downloadPython37(supportingIDEs[3][0],supportingIDEs[3][2])

while outerLoop:
    os.system('cls')
    if platformChecker[1] != 'WindowsPE':
        print("Unsupported Operating System. This program only support Windows 32bit, 64bit.")
        os.system("pause")
    else:
        print("IDE Auto Downloader Made by Hoplin.")
        print("Programs will be downloaded in directory : " + os.getcwd())
        print("=" * 25)
        print("0 . Exit")
        for p in range(len(supportingIDEs.keys())):
            print(str(p + 1) + ". " + supportingIDEs[p + 1][0])
        print(str(list(supportingIDEs.keys())[-1] + 1) + ". Download All")
        print("=" * 25)
        opNum = None
        optionLoop = True
        while optionLoop:
            opNum = int(input("Select IDE option number you want to download : "))
            if opNum == 0:
                sys.exit()
            elif opNum == list(supportingIDEs.keys())[-1] + 1:
                optionLoop = False
                if platformChecker[0] == '32bit':
                    os.system('cls')
                    for al in list(supportingIDEs.keys()):
                        evalState = "supportingIDEs[" + str(al)+"][1].download32bit()"
                        eval(evalState)
                    print("Download Complete.... Go back to menu")
                else:
                    os.system('cls')
                    for al in list(supportingIDEs.keys()):
                        evalState = "supportingIDEs[" + str(al)+"][1].download64bit()"
                        eval(evalState)
                    print("Download Complete.... Go back to menu")
            elif opNum not in supportingIDEs.keys():
                os.system('cls')
                optionLoop = False
                print("Error : Selected option number isn't exist. Please enter proper option Number\n")
            else:
                optionLoop = False
                if platformChecker[0] == '32bit':
                    os.system('cls')
                    eval("supportingIDEs[opNum][1].download32bit()")
                else:
                    os.system('cls')
                    eval("supportingIDEs[opNum][1].download64bit()")
