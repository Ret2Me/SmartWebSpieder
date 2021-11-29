from urllib.parse import urlparse
import subprocess
import requests

# check is git exposed to the internet 

def git(self):
    
    url = self.targets[0]

    if (url[-1] != '/'):
        url += '/'
    git_url = url + ".git/config"

    print("trying: ", git_url)
    try:
        exist = requests.get(url = git_url, allow_redirects=False, verify=False, timeout=5)
        if (exist.status_code != 200 or "[core]" not in str(exist.content)):
            return False
    except Exception as e:
        print(e)
        return False


    print("[!!!] hit git: " + git_url + " [!!!]")
    if (self.download == True):
        self.download_git()     
        return True



    
    # resources downloading  
    def downloadGit(self):
        root = urlparse(self.url)[1]
        try:
            print("-" * 10 + "running git_dumper.py" + "-" * 10)
            subprocess.run(["python", "./tools/git_dumper/git_dumper.py" , self.url, "./git/" + root])
            print("-" * 41)
        except:
            print("[!] Error while opening ./tools/git-dumper/git-dumper.py [!]")


