import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from urllib.parse import urlparse




# check env file
def env(self):
    url = self.targets[0]

    if (url[-1] != '/'):
        url += '/'
    git_url = url + ".env"



    print("trying: ", git_url)
    try:
        response = self.session.get(url=url, allow_redirects=False, verify=False, timeout=5)
        if (response.status_code != 200       or 
            "HTML" in str(response.content)   or 
            "html" in str(response.content)   or 
            "div" in str(response.content)    or
            "script" in str(response.content) or
            len(response.content) == 0):
            
            
            return False
    except:
        return False

    if (self.download == True):
        file = open("./output/env_" +  str(urlparse(url).hostname), 'w')
        file.write(str(response.content))
        file.close()
        return True
