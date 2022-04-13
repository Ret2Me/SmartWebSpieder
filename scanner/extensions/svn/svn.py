from datetime import datetime
import urllib3
import subprocess
import warnings
import scanner


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
warnings.filterwarnings("ignore")


def svn(self):
    """ Check is svn exposed to the internet """
    
    url = self.targets[0]
    if url[-1] != '/':
        url += '/'
    url += ".svn/wc.db"

    try:
        exist = self.session.get(url=url,
                                 allow_redirects=False,
                                 verify=False,
                                 timeout=5)
        if exist.status_code != 200 or "SQLite format" not in str(exist.content):
            return False
    except:
        return False

    if scanner.session.query(scanner.Server)\
                        .filter((scanner.Server.url == url)
                                & (scanner.Server.vulnerability_id == 2)).first() is None:
        scanner.session.add(scanner.Server(url=url, timestamp=datetime.now(), vulnerability_id=2, confidence=7))
        scanner.session.commit()

    return True