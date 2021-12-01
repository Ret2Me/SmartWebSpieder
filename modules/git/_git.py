import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from urllib.parse import urlparse
import subprocess


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


    print("[!!!] hit git: " + git_url + " [!!!]")
    if (self.download == True):
        self.downloadGit(url)     
        return True






# download git repository  
def downloadGit(self, url):
    try:
        print("-" * 10 + "running git_dumper.py" + "-" * 10)
        subprocess.run(["python", "./tools/git_dumper/git_dumper.py" , url, ("./output/git_" + str(urlparse(url).hostname))])
        print("-" * 41)
    except:
        print("[!] Error while opening ./tools/git-dumper/git-dumper.py [!]")


