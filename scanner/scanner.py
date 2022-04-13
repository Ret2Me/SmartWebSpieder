"""
Scanner engine that runs extensions
main
|
|---+ website-scan
^   |---> env
|   |---> git
|   |---> svn
|   |---> more extensions
|   |---> your actions
|   |---+ adding new urls to queque
|   |   |---> sublist3r (to find subdomains)
|___|
"""


import warnings
import requests
import urllib3
import sqlalchemy
import scanner

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
warnings.filterwarnings("ignore")


class WebsiteCrawler:
    """ Main crawler class here is stored all information and behaviors of running crawler"""
    def __init__(self, targets, download, past_websites, vulnerable_websites, drop_counter=20000):
        self.drop_counter_start_value = drop_counter
        self.past_websites = past_websites
        self.session = requests.Session()
        self.drop_counter = drop_counter
        self.black_list = past_websites
        self.history = self.black_list
        self.download = download
        self.targets = targets
        self.renew_size = 100

    def run(self):
        """ Run crawler """

        # dump arrays for better optimization
        if self.drop_counter == 0:
            self.drop_counter = self.drop_counter_start_value
            self.history = self.black_list
            del self.targets[self.renew_size:]

        while len(self.targets) > 0:

            # add new urls to list
            # self.dnsDump()
            self.url_dump()

            # search for sensitive data exposure
            nmap = False
            self.env()
            if self.git():
                nmap = True

            if self.svn():
                nmap = True

            # ToDo add nmap support
            if nmap:
                pass

            # ------------END------------
            self.past_websites.append(self.targets.pop(0))
            self.drop_counter -= 1
