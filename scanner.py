import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from multiprocessing.managers import Server
import multiprocessing
import sys,os
# sys.path.append(os.path.realpath('./modules/dnsDump/'))
# sys.path.append(os.path.realpath('./modules/dnsDump/subbrute'))



class website_crawler:
    def __init__(self, targets, download, past_websites, drop_counter = 10000):
        self.session = requests.Session()
        self.targets = targets
        self.download = download
        self.black_list = past_websites
        self.past_websites = past_websites
        self.drop_counter_startval = drop_counter
        self.drop_counter = drop_counter
        self.renew_size = 100


 
    # appending new targets 
    from modules.dnsDump._dnsDump import dnsDump
    from modules.urlDump._urlDump import urlDump
    
    # scan for vulnerabilities 
    from modules.env._env import env
    from modules.nmapVuln._nmap import nmap_scan
    from modules.git._git import git, downloadGit
    from modules.svn._svn import svn, downloadSvn





    def run(self):

        # dump arrays for better optymalization
        if (self.drop_counter == 0):
            self.drop_counter = self.drop_counter_startval
            self.history = self.black_list
            del self.targets[self.renew_size:]


        while len(self.targets) > 0:


            # add new urls to list  
            self.dnsDump()
            self.urlDump()


            #search for sensitive data exposure
            nmap = False
            self.env()

            if (self.git() == True):
                nmap = True

            if (self.svn() == True):
                nmap = True

            if (nmap == True):
                self.nmap_scan()                



            # ------------END------------
            self.past_websites.append(self.targets.pop(0))
            self.drop_counter -= 1

            

















def main():

    # standard config
    black_list = ['facebook', 'wiktionary', 'youtube', 'amazon', 'instagram', 'wikipedia', 'wikimedia',  'pinterest', 'linkedin', 'messenger', 'google', 'twitter', 'apache', "html5", 'githubassets', 'w3c', 'json-ld']
    url_queue =  []










    # create threads with new branches
    processes = []
    crawlers_obj  = []

    for i in range(0, len(url_queue)):

        crawlers_obj.append(website_crawler([url_queue[i]], True, black_list))
        process = multiprocessing.Process(target=crawlers_obj[i].run)

        process.start()
        processes.append(process)


    for process in processes:
        process.join()  



if __name__=="__main__":
   main()


"""

main 
|
|---+ website-scan
^   |---> env
|   |---> git 
|   |---> svn
|   |---> more files
|   |---> your actions   
|   |---+ adding new urls to queque
|   |   |---> sublist3r (to find subdomains)
|___|

"""
