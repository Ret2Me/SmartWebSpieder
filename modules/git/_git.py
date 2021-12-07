import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from urllib.parse import urlparse
import subprocess
import os

# check is git exposed to the internet 
def git(self):
    
    url = self.targets[0]

    if (url[-1] != '/'):
        url += '/'
    git_url = url + ".git/config"



    print("trying: ", git_url)
    try:
        exist = self.session.get(url = git_url, allow_redirects=False, verify=True, timeout=5)
        if (exist.status_code != 200 or "[core]" not in str(exist.content)):
            return False
    except:
        return False


    if (self.download == True):
        self.downloadGit(url)     
        return True






# download git repository  
def downloadGit(self, url):


    try:
        dir_path = "./output/" +  str(urlparse(url).hostname)

        if (os.path.isdir(dir_path) == False):
            os.mkdir(dir_path)
            dir_path += "/git/" 
            os.mkdir(dir_path)

        subprocess.run(["python", "./tools/git_dumper/git_dumper.py" , url, dir_path])
    except Exception as e:
        print("[!] Error while opening ./tools/git_dumper/git_dumper.py [!]")
        print(e)