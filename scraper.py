import hashlib
import requests
from bs4 import BeautifulSoup

url = 'https://www.theonion.com/latest'
print("Grabbed url")
links = []
website = requests.get(url)
website_text = website.text
soup = BeautifulSoup(website_text, features="lxml")

for link in soup.find_all('a'):
    links.append(link.get('href'))
    
print("searched for all links")


with open('url.txt', 'w') as filehandle:
    for listitem in links:
        filehandle.write('%s\n' % listitem)

print("Written unfiltered results to file")


print("scraper finished")


name = "https://entertainment.theonion.com/"
name2 = "https://www.theonion.com/"
name3 = "https://politics.theonion.com/"
name4 = "https://sports.theonion.com/"
name5 = "https://local.theonion.com/"
name6 = "https://ogn.theonion.com/"
old = open("url.txt", "r")
newfile = open('filtered.txt', 'w')
for line in old:
    if name in line:
        newfile.write(line)
    elif name2 in line:
        newfile.write(line)
    elif name3 in line:
        newfile.write(line)
    elif name4 in line:
        newfile.write(line)
    elif name5 in line:
        newfile.write(line)
    elif name6 in line:
        newfile.write(line)



newfile.close()

print("filtered all http links")


output_file_path = "final.txt"
input_file_path = "filtered.txt"


completed_lines_hash = set()


output_file = open(output_file_path, "w")


for line in open(input_file_path, "r"):
  
  hashValue = hashlib.md5(line.rstrip().encode('utf-8')).hexdigest()

  if hashValue not in completed_lines_hash:
    output_file.write(line)
    completed_lines_hash.add(hashValue)

output_file.close()

print("removed duplicates")

bad_words = ['/c/']

with open('final.txt') as oldfile, open('finished.txt', 'w') as newfile:
    for line in oldfile:
        if not any(bad_word in line for bad_word in bad_words):
            newfile.write(line)



input("Removed tags, press enter to close this windows, results are in finished.txt")