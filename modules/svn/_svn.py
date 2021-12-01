import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import subprocess



# check is svn exposed to the internet 
def svn(self):
    
    url = self.targets[0]

    if (url[-1] != '/'):
        url += '/'
    svn_url = url + ".svn/wc.db"

    print("trying: ", svn_url)
    try:
        exist = self.session.get(url = svn_url, allow_redirects=False, verify=False, timeout=5)
        if (exist.status_code != 200 or "SQLite format" not in str(exist.content)):
            return False
    except Exception as e:
        return False


    print("[!!!] hit svn: " + svn_url + " [!!!]")
    if (self.download == True):
        self.downloadSvn(url)     
        return True






# download svn repository  
def downloadSvn(self, url):
    try:
        print("-" * 10 + "running svn_extractor.py" + "-" * 10)
        subprocess.run(["python", "./tools/svn-extractor/svn_extractor.py" , "--url", str(url)])
        print("-" * 41)
    except:
        print("[!] Error while opening ./tools/svn-extractor/svn-extractor.py [!]")


