#~ /usr/bin/env python3

import os

url = "https://www.dvlv.co.uk/"
urls = [url]

for file in os.listdir("output"):
    if file.endswith(".html"):
        urls.append(url + file)

for file in os.listdir("output/pages"):
    print(file)
    if file.endswith(".html"):
        urls.append(url + "pages/" + file)

with open("output/sitemap.txt", "w") as f:
    for line in urls:
        f.write(line + "\n")


