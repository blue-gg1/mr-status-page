import os, ntpath, shutil

# planned way to call this
#  5 * * * * /usr/sbin/python /app/code/main.py


def CheckPagePing(Url):
    pass

def CheckPageHttp(Url, Method):
    pass

def CheckPageBrowser(Url):
    pass

def AddInfoToJson():
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