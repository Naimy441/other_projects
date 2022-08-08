import requests, bs4, webbrowser, re

wiki = requests.get('https://en.wikipedia.org/wiki/Donald_Trump')
wiki.raise_for_status()

wiki_html = bs4.BeautifulSoup(wiki.text, 'html.parser')
urls = wiki_html.select('a[href]')

wiki_urls = []
expression = re.compile(r'/wiki/.*')
for url in urls:
    wiki_path = expression.search(url.attrs['href'])
    if wiki_path is not None:
        colon_found = False
        for char in wiki_path.group():
            if char == ':':
                colon_found = True
        if not colon_found:
            wiki_urls.append(wiki_path.group())

for wiki_url in wiki_urls[:10]:
    webbrowser.open('https://en.wikipedia.org' + wiki_url)
