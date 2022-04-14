import urllib3
import warnings
from urllib.parse import urlparse
from datetime import datetime
import scanner

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
warnings.filterwarnings("ignore")


def env(self):
    """ check env file """
    url = self.targets[0]

    if url[-1] != '/':
        url += '/'
    url += '.env'

    try:
        response = self.session.get(url=url,
                                    allow_redirects=False,
                                    verify=False,
                                    timeout=5)
        if (response.status_code != 200 or
            "HTML" in str(response.content) or
            "html" in str(response.content) or
            "div" in str(response.content) or
            "script" in str(response.content) or
            len(response.content) == 0):
            return False
    except:
        return False

    # ToDo:
    # add real confidence measure based on git size and check is it publicly available
    if scanner.session.query(scanner.Server).filter((scanner.Server.url == url)
                                    & (scanner.Server.vulnerability_id == 3)).first() is None:
        scanner.session.add(scanner.Server(url=url, timestamp=datetime.now(), vulnerability_id=3, confidence=7))
        scanner.session.commit()

    return True
