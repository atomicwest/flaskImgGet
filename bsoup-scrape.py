# https://www.google.com/search?q=sun&source=lnms&tbm=isch&sa=X

import sys, os


bspath = os.path.join(os.path.dirname(os.path.abspath(__file__)),"BeutifulSoup")
sys.path.append(bspath)


# from deps.bs4 import BeautifulSoup as bsoup
from bs4 import BeautifulSoup as bsoup
# import bs4

# from deps.bs4py3 import BeautifulSoup as bsoup

def formatUrl(query):
  startUrl = "https://www.google.com/search?q="
  endUrl = "&source=lnms&tbm=isch&sa=X"
  q = query.split(" ")
  qword = ""
  
  for i,word in enumerate(q):
    qword+=word
    
    if i!=len(q)-1:
      qword+="+"

  return startUrl+qword+endUrl

search = "post hotel lake louise"
formatUrl(search)