import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
from multiprocessing.managers import Server
import threading
import sys,os
# sys.path.append(os.path.realpath('./modules/dnsDump/'))
# sys.path.append(os.path.realpath('./modules/dnsDump/subbrute'))



class website_crawler:
    def __init__(self, targets, download, past_websites):

        self.targets = targets
        self.download = download
        self.past_websites = past_websites



    # import modules
    from modules.git._git import git, downloadGit
    from modules.svn._svn import svn
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
    url_queue = ['https://www.onet.pl/', 'http://konfederacjalewiatan.pl/']
    number_of_threads = 3  
    

    # create threads with new branches
    threads = []
    crawlers_obj  = []

    for i in range(0, number_of_threads):
        if (len(url_queue) <= i):
            break

        crawlers_obj.append(website_crawler([url_queue[i]], True, black_list))
        thread = threading.Thread(target=crawlers_obj[i].run)
        thread.start()
        threads.append(thread)


    for thread in threads:
        thread.join()  




    crawlers = website_crawler(url_queue, 1, False, black_list)
    crawlers.run()


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
