from bs4 import BeautifulSoup
import requests
import os

loc = input("Enter the base location : ")
url = input("Enter the url : " )

os.chdir(loc)

base = "https://codeforces.com"

res = requests.get(url)

soup = BeautifulSoup(res.text, 'html.parser')

prblms = (soup.find("table", {"class":"problems"})).find_all("tr")

links = []

for i in range(1, len(prblms)):
    links.append(prblms[i].find("a")['href'])

if(len(links)>0):
    os.system("mkdir sample-test")

os.chdir(".\\sample-test")

base_dir = os.getcwd()
    
for link in links:
    p = list(link.split('/'))

    os.chdir(base_dir)
    os.system("mkdir " + p[len(p) - 1])
    os.chdir(base_dir + "\\" + p[len(p) - 1])

    cur = base + link
    res1 = requests.get(cur)
    soup1 = BeautifulSoup(res1.text, 'html.parser')

    sample = soup1.find('div', {'class': 'sample-test'})

    inputs = sample.find_all('div', {'class': 'input'})
    
    i = 0

    os.mkdir("inputs")
    os.chdir(base_dir + "\\" + p[len(p) - 1] + "\\inputs")

    for inp in inputs:
        name = str(i) + ".txt"
        f = open(name, "w")
        f.write(inp.find('pre').text)
        i += 1

    outputs = sample.find_all('div', {'class': 'output'})

    i = 0

    os.chdir(base_dir + "\\" + p[len(p) - 1])
    os.mkdir("outputs")
    os.chdir(base_dir + "\\" + p[len(p) - 1] + "\\outputs")

    for out in outputs:
        name = str(i) + ".txt"
        f = open(name, "w")
        f.write(out.find('pre').text)
        i += 1