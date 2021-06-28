"""
## Tugas
Lakukan Web Scrapping
http://www.scifijapan.com/articles/2015/10/04/bandai-ultraman-ultra-500-figure-list/

Daftar Ultraman dan Daftar Monster
No dan Namanya
Export ke dalam file JSON

Formatnya [
  {"Ultraman" : {"01" : "Ultraman", "02" : "Ultra seven", dst...},
  "Monster" : {"01" : "Alien Baltan", "02" : "Gomora", dst...}}
]

Kirim file py dan json nya via email
"""

from bs4 import BeautifulSoup
import requests
import json

url = "http://www.scifijapan.com/articles/2015/10/04/bandai-ultraman-ultra-500-figure-list/"
web = requests.get(url)
out = BeautifulSoup(web.content, "html.parser")

kotak = []
for i in out.find_all("strong"):
  kotak.append(i.text)

# print(kotak)

# print(kotak[2:36])
# print(kotak[37:110])

ultraman = kotak[2:36]
monster = kotak[37:110]
noultraman = []
namaultraman = []
nomonster = []
namamonster = []

for i in ultraman:
    noultraman.append(i[:2])
    namaultraman.append(i[3:])

# # print(noultraman)
# # print(namaultraman)

dictultraman = dict(zip(noultraman,namaultraman))
# print(dictultraman)

for j in monster:
    nomonster.append(j[:2])
    namamonster.append(j[3:])

# print(nomonster)
# print(namamonster)
dictmonster = dict(zip(nomonster,namamonster))
# print(dictmonster)

hasil = [{
    "Ultraman" : dictultraman,
    "Monster"  : dictmonster
}]

# print(hasil)

with open("Ultraman.json", "w") as file:
    json.dump(hasil, file)
print("Ultraman.json Created")