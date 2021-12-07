from urllib.parse import urlparse
import nmap
import os



def nmap_scan(self):
    scanner = nmap.PortScanner()
    url = self.targets[0]


    dir_path = "output/" + str(urlparse(url).hostname) 
    if (os.path.isdir(dir_path) == False):
        os.mkdir("output/" + str(urlparse(url).hostname))



    try:
        a = str(urlparse(url).hostname)
        print(a)
        res = scanner.scan(a, "443", arguments="--script vuln", sudo=False)
        file = open(dir_path + "/nmap.out", 'w')
        file.write(str(res))
        file.close()
    except Exception as e:
        print(e)
