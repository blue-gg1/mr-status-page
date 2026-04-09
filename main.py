import os, ntpath, shutil
from datetime import date, datetime

# planned way to call this
#  5 * * * * /usr/sbin/python /app/code/main.py

def SetDateGlobals(): # set up dates that will be true when the code is run
    global today
    global this_year
    global this_month
    global this_day
    global this_hour
    global now
    now = datetime.now()
    this_hour = now.strftime("%H")
    this_day = now.day
    this_month = now.month
    this_year = now.year


def CheckPagePing(Url: str):
    pass

def CheckPageHttp(Url: str, Method: str):
    pass

def CheckPageBrowser(Url: str):
    pass

def AddInfoToJson(TimeOfCheck, StatusData):
    pass

def RenderHtmlFromJson(JsonFile):
    pass

def AddHtmlToGit():
    print("making the git commit")
    GitCommitMessage = "Updated the HTML from live now here: https://*.pages.dev/index.html"
    ntpath.realpath = ntpath.abspath
    shutil.copy("example.html", "prod-cf/index.html")
    print(os.system("git add ."))
    print(os.system("git commit -am "+chr(34)+GitCommitMessage+chr(34)))
    print(os.system("git push"))

SetDateGlobals()
print(now)
print(this_year)
print(this_month)
print(this_day)
print(this_hour)