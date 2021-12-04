import feedparser
import requests
from tqdm import tqdm   # progress bar

d=feedparser.parse('<Feed>')   # <Feed> can be either the URL of the RSS feed or the path to an xml file

for entry in tqdm(d.entries):
    file_name = entry.title + '.mp3'
    links = entry.links

    for link in links:
        if link.type == 'audio/mpeg':
            r = requests.get(link.href, stream = True)
            with open(file_name, 'wb') as f:
                for chunk in r.iter_content(chunk_size = 1024*1024):
                    if chunk:
                        f.write(chunk)

print("All episodes downloaded!")