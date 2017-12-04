from bs4 import BeautifulSoup as bsp
import bs4      #only used for class check
from urllib.request import urlopen, Request
import re


#use if all inputs  are strings OR lists of strings only
def tagCleaner(raw):
    out = ""
    if type(raw)==bs4.NavigableString:
        out = re.sub('<.*?>', '', str(raw))
        # out = re.sub(r'<.*?>', '', str(raw))
    elif type(raw)==list:
        for s in raw:
            line = str(s)
            if "<" in line:
                out+=re.sub('<.*?>', '', str(s))
            else:
                out+=line
    return out


#replace spaces in a query such as "roswell, nm"
def concatQ(string, sym):
    words = string.split(" ")
    return sym.join(words)


#constructs a basic query url from the generic google search url
def formatUrl(query):
    #the full url should look like:
    #https://www.google.com/search?tbm=nws&q=new+zealand
    
    # genericUrl = "https://www.google.com/search?source=hp&q="
    genericUrl = "https://www.google.com/search?tbm=nws&q="
    
    formatQ = concatQ(query, "+")
    fullurl = genericUrl + formatQ
    
    # mod = "-slp-class"
    # fname = "read-" + query + mod + ".txt"
    
    return fullurl


def readfromf(filename):
    f = open(filename, 'r')
    for l in f:
        print(l)

def printlines(d, key):
    for l in d[key]:
        print(l)


#main api function
def scraper(url):
    
    out = {}
    
    try:
        head = {'User-Agent': 'Mozilla/5.0'}
        req = Request(url, headers=head)
        html = urlopen(req)
        bsObj = bsp(html, "html.parser")
        
        #scrape raw tags first
        imgs = bsObj.findAll('img', {'class':'th'})
        headlines = bsObj.findAll('h3', {'class':'r'})
        links = bsObj.findAll('span', {'class':'f'})
        dates = bsObj.findAll('div', {'class':'slp'})
        stories = bsObj.findAll('div', {'class':'st'})
        
        # print(len(imgs))
        # print(len(headlines))
        # print(len(links))
        # print(len(dates))
        # print(len(stories))
        
        #extract from scraped data
        #each data array may not be the same length; 
        #try to match domains to align arrays
        thumbs = [t['src'] for t in imgs]
        
        # if s is a hashed news headline link: s.split("=")[1].split("&")[0]
        hlinks = [h.a['href'].split("=")[1].split("&")[0] for h in headlines]
        datesources = [re.sub('\u200e', '', str(d.contents[0].contents[0])) for d in dates]
        hlines = [tagCleaner(h.a.contents) for h in headlines]
        
        # for i in range(len(thumbs)):
        #     print(thumbs[i])
        #     print(hlinks[i])
        #     print(hlines[i])
        #     print(datesources[i])
        
        out = {'thumbs': thumbs, "hlinks":hlinks, "hlines":hlines, "dates":datesources}
        
    except Exception as e:
        print(e)
        out = {"Exception":e}
    finally:
        print("*"*25)

    return out

        
# url = formatUrl("Roswell, NM")
url = formatUrl("Seattle, WA")
sc = scraper(url)
print(url)
print(sc)
printlines(sc, "hlines")