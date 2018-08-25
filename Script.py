from bs4 import BeautifulSoup
import urllib.request
import shlex
import subprocess
import os
import string

title = "Kanaa"
url = "http://tamilmusiq.net/Movie/Kanaa"
head = {'User-Agent': 'Mozilla/5.0'}
req = urllib.request.Request(url,headers=head)
response = urllib.request.urlopen(req)
page = response.read()
soup = BeautifulSoup(page,'html.parser')

tags = soup.find_all('a',attrs={'class':'btn-download btn btn-success'})
links = []
for tag in tags :
    links.append(tag['href'])

for link in links:
    link = link.replace(" ","%20")
    print(link)
    subprocess.call(shlex.split('bash ./download.sh ' + link + ' "' + title + '"'))
