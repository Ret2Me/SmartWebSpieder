def dnsDump(self):
    pass


# # import modules.dnsDump.Sublist3r.sublist3r as sublist3r

# import os,sys
# sys.path.append(os.path.realpath('.'))

# sys.path.append(os.path.realpath('./modules/dnsDump/'))
# sys.path.append(os.path.realpath('./modules/dnsDump/subbrute'))

# from . import sublist3r # as sublist3r

# # search other webistes in DNSrecords



# def dnsDump(self):

#     url = self.targets[0]

#     # make  special url format for sublist3r domain.com
#     if (url[:7] == 'http://'):
#         url = url[7:]
#     elif (url[:8] == 'https://'):
#         url = url[8:]
#     if  (url[-1] == "/"):
#         url = url[:-1]
    

#     print("[!] ", url)

#     subdomains = sublist3r.main(url, 1, '', "", silent=True, verbose=False, enable_bruteforce=False, engines="google,bing,dnsdumpster,threatcrowd,ssl,passivedns")
#     for subdomain in subdomains:  # baidu,yahoo,google,bing,ask,netcraft,dnsdumpster,threatcrowd,ssl,passivedns
        
#         if (subdomain not in self.past_websites and subdomain not in self.targets):
#             self.targets.append("https://" + subdomain + "/")

