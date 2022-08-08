from debug import *
import requests, threading, bs4, re
config(True)

def getFirstLink(link):
    wikipedia = requests.get(link)
    wikipedia.raise_for_status()

    soup = bs4.BeautifulSoup(wikipedia.text, 'html.parser')
    paths = soup.select('p a[href]')

    #Ban stuff in parentheses, italized, current page links
    i = 0
    while '#' in paths[i].get('href') or ':' in paths[i].get('href') or 'Latin' in paths[i].get('href') or 'Greek' in paths[i].get('href') or 'translation' in paths[i].get('href'):
        i += 1

    wiki_link = 'https://en.wikipedia.org' + paths[i].get('href')
    return wiki_link

start = 'https://en.wikipedia.org/wiki/Wikipedia:Getting_to_Philosophy'
next = getFirstLink(start)

print(next)
while next != 'https://en.wikipedia.org/wiki/Philosophy' and next != 'https://en.wikipedia.org/wiki/Latin':
    next = getFirstLink(next)
    print(next)
