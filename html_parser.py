# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 22:49:25 2015

@author: Nishant
"""
from BeautifulSoup import BeautifulSoup
import urllib
pageFile = urllib.urlopen("https://www.iitm.ac.in/students/sinfo/EE14B097")
pageHtml = pageFile.read()
pageFile.close()
soup = BeautifulSoup("".join(pageHtml))
menu1= soup.find("div", {"class":"block block-system no-title"})
menu2= menu1.find("strong")
print menu2.text
name= menu2.text