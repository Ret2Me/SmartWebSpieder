from multiprocessing.managers import Server
import sys,os
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# sys.path.append(os.path.realpath('./modules/dnsDump/'))
# sys.path.append(os.path.realpath('./modules/dnsDump/subbrute'))



class website_crawler:
    def __init__(self, targets, depth, download, past_websites):

        self.targets = targets
        self.depth = depth
        self.download = download
        self.past_websites = past_websites



    # import modules
    from modules.git._git import git
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
    url_queue = [taret]
    black_list = ['facebook', 'wiktionary', 'youtube', 'instagram', 'wikipedia', 'wikimedia', 'pinterest', 'linkedin', 'messenger', 'google']
    crawlers = website_crawler(url_queue, 1, False, black_list)
    crawlers.run()


if __name__=="__main__":
   main()


"""
ToDo:
- check is .git is real git or maybe just empty website


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
