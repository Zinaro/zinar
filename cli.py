"""import requests as rq
from bs4 import BeautifulSoup as bs
import urllib.parse as urp

headers = {
    'Host' : 'e-com.secure.force.com',
    'Connection' : 'keep-alive',
    'Upgrade-Insecure-Requests' : '1',
    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64)',
    'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding' : 'gzip, deflate, sdch',
    'Accept-Language' : 'en-US,en;q=0.8'
}
url = "https://twitter.com/zinarcim"
def get_domain(url):
	return '{uri.scheme}://{uri.netloc}'.format(uri=urp.urlparse(url))
print(get_domain(url))
"""

from googletrans import Translator
import requests
from bs4 import BeautifulSoup
trans = Translator()

title= "Twitter"
link = "https://ku.wikipedia.org/wiki/" + str(title.lower())
r = requests.get(link)
soup = BeautifulSoup(r.content, "html.parser")
st1 = soup.find_all("div", attrs = {"id":"bodyContent"})
text = st1[0].text
print(text)
