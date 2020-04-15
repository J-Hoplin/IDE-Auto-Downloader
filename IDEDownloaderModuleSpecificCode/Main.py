from bs4 import BeautifulSoup
from urllib.request import urlopen
import zipfile
from io import BytesIO
import subprocess
import requests
import platform
import os
import sys
from .SublimeDownloader import downloadSublimeText3
from .VSCodeDownloader import downloadVisualStudioCode
from .Python37Downloader import downloadPython37
from .PhantomJSDownloader import downloadPhantomJS

dST = downloadSublimeText3()
dVSC = downloadVisualStudioCode()
dPY3 = downloadPython37()
dPJS = downloadPhantomJS()

outerLoop = True


#Check PC platform type. This program only support Windows 32bit,64bit
platformChecker = platform.architecture()
#(bit,OS)

supportingIDEs = {
    1 : ['Sublime Text3',dST],
    2 : ['Visual Studio Code',dVSC],
    3 : ['Python 3.7.6',dPY3],
    4 : ['Phantom JS',dPJS]
}

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
                    print("Download Complete.... Go back to menu")
                    time.sleep(3)
                else:
                    os.system('cls')
                    eval("supportingIDEs[opNum][1].download64bit()")
                    print("Download Complete.... Go back to menu")
                    time.sleep(3)






