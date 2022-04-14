from datetime import datetime
import urllib3
import warnings
import scanner
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
warnings.filterwarnings("ignore")



def git(self):
    """ check is git exposed to the internet """
    url = self.targets[0]
    if (url[-1] != '/'):
        url += '/'
    git_url = url + ".git/config"

    try:
        exist = self.session.get(url=git_url,
                                 allow_redirects=False,
                                 verify=True,
                                 timeout=5)
        if exist.status_code != 200 or "[core]" not in str(exist.content):
            return False
    except:
        return False

    # ToDo:
    # add real confidence measure based on git size and check is it publicly available
    if scanner.session.query(scanner.Server).filter((scanner.Server.url == url)
                                                    & (scanner.Server.vulnerability_id == 1)).first() is None:
        scanner.session.add(scanner.Server(url=git_url, timestamp=datetime.now(), vulnerability_id=1, confidence=7))
        scanner.session.commit()
    return True
