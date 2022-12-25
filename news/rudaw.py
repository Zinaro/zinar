import requests
from bs4 import BeautifulSoup as bs
from headers import UserAgent as UA
print(UA)
print("^"*60)

class Rudaw:
    def __init__(self):
        self.url = ""
        self.bs = bs()
        self.r = requests
    def linkanuce(self):
        self.url = "https://www.rudaw.net/kurmanci/news"
        return self.url
    def herelinke(self):
        self.req = self.r.get(self.linkanuce(), headers=UA)
        print(self.req.headers)
        print("-"*60)

        self.soup = bs(self.req.text, "html.parser")
        print(self.soup)
        
    def penc(self):
        self.herelinke()




Rudaw().penc()  
