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
name= menu2.text
menu1.findAll("td")
print "Name: {}".format(name)
para=menu1.text
#print para
a= para.find("Gender")
index_gender= a+ len("Gender")
gender= para[index_gender]
print "Gender: {}".format(gender) 
