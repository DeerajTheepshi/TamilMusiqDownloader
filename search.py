from bs4 import BeautifulSoup
import urllib.request
import shlex
import subprocess
import os
import string
import sys

end_point = ""
for i in range(len(sys.argv)-1):
    end_point += sys.argv[i+1] + "+"
base_url = "http://tamilmusiq.net/search.php?q="
url = base_url+end_point.rstrip("+")

print("Requested Search being made....awaiting results")
head = {'User-Agent': 'Mozilla/5.0'}
req = urllib.request.Request(url,headers=head)
response = urllib.request.urlopen(req)
page = response.read()
soup = BeautifulSoup(page,'html.parser')

photoTags = soup.find_all("figcaption")
info = []
links = []
for tag in photoTags:
    links.append(tag.find("a")["href"])
    for a in tag.find_all("a"):
        info.append(a.text.strip())

print("Resuts got")
if(len(info)==0):
    print("Sorry , no results found")
    exit()
for i in range(int(len(info)/2)):
    print(str(i+1) + "----->" + info[i*2])
    print(info[i*2+1]+"\n")

selection = int(input("Pick your selection : "))
link = links[selection-1]
link = "http://tamilmusiq.net"+link
subprocess.call(shlex.split('python ./Script.py ' + link))
