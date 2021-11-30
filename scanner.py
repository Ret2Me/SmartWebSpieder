import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
from multiprocessing.managers import Server
import threading
import multiprocessing
import sys,os
# sys.path.append(os.path.realpath('./modules/dnsDump/'))
# sys.path.append(os.path.realpath('./modules/dnsDump/subbrute'))



class website_crawler:
    def __init__(self, targets, download, past_websites):
        self.session = requests.Session()
        self.targets = targets
        self.download = download
        self.past_websites = past_websites



    # import modules
    from modules.git._git import git, downloadGit
    from modules.svn._svn import svn, downloadSvn
    from modules.dnsDump._dnsDump import dnsDump
    from modules.urlDump._urlDump import urlDump
    



    def run(self):

        while len(self.targets) > 0:


            # add new urls to list  
            self.dnsDump()
            self.urlDump()


            #search for sensitive data exposure
            self.git()
            self.svn()




            # ------------END------------
            self.past_websites.append(self.targets.pop(0))

            

















def main():
    black_list = ['facebook', 'wiktionary', 'youtube', 'instagram', 'wikipedia', 'wikimedia', 'pinterest', 'linkedin', 'messenger', 'google']
    url_queue = ['https://optimizely.techtarget.com/', 'http://gazeta.pl/']
    number_of_threads = 3  
    

    # create threads with new branches
    processes = []
    crawlers_obj  = []

    for i in range(0, number_of_threads):
        if (len(url_queue) <= i):
            break
        

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
^   |---> git 
|   |---> svn
|   |---> more files
|   |---> your actions   
|   |---+ adding new urls to queque
|   |   |---> sublist3r (to find subdomains)
|___|

"""
