import requests, bs4, debug

debug.config(False, 'wiki_crawl.bat')
debug.pause(True)

def get_wiki_article(url):
    wikipedia = requests.get(url)
    wikipedia.raise_for_status()
    return wikipedia


def get_valid_paragraph(response):
    # BUG: what if first paragraph does not have a link? (example: https://en.wikipedia.org/wiki/Methodology)
    # BUG: what if it selects the geographic coordinates paragraph? (example: https://en.wikipedia.org/wiki/Americas)
    # Make sure valid link is not '/wiki/Geographic_coordinate_system'
    # In order to fix these bugs, the code should look through all paragraphs until it finds the first valid link instead of picking the first paragraph and then finding the first valid link in that.
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    paragraphs = soup.find(id='bodyContent').select('div.mw-parser-output > p')
    for paragraph in paragraphs:
        if 'mw-empty-elt' in str(paragraph):
            continue
        debug.log('First Valid Paragraph:')
        debug.log(paragraph)
        debug.log('\n')
        return paragraph


def is_enclosed(html, url_start_index):
    html_before_url = html[:url_start_index]

    for type in ('()', '[]', '{}'):
        open_parethese_count, close_parenthese_count = 0, 0

        for char in html_before_url:
            if char == type[0]:
                open_parethese_count += 1
            elif char == type[1]:
                close_parenthese_count += 1

        if open_parethese_count > close_parenthese_count:
            return True
    return False


def is_italicized(italicized_instances, link):
    for instance in italicized_instances:
        if link in instance:
            return True
    return False


def get_first_link(parsed_html):
    links = [str(link['href']) for link in parsed_html.find_all('a') if '/wiki/' in link['href']]

    debug.log('Links:')
    debug.log(links)
    debug.log('\n')

    italicized_instances = [str(instance) for instance in parsed_html.find_all('i')]
    for link in links:
        if is_enclosed(str(parsed_html), str(parsed_html).find(link)) or is_italicized(italicized_instances, link):
            debug.log(link)
            continue

        debug.log('Chosen Link:')
        debug.log(link)
        return 'https://en.wikipedia.org' + link

    raise Exception('No Valid Link Found in Paragraph')


wiki_url = 'https://en.wikipedia.org/wiki/Italian_diaspora'
wiki_urls = [wiki_url]
print(wiki_url)

should_break = False
while not should_break:
    wiki_page = get_wiki_article(wiki_url)
    valid_paragraph = get_valid_paragraph(wiki_page)
    wiki_url = get_first_link(valid_paragraph)

    print(wiki_url)

    for url in wiki_urls:
        if wiki_url == url:
            print('Loop discovered. The Philosophy Wiki Crawl has failed!')
            should_break = True
            break

    wiki_urls.append(wiki_url)

    if wiki_url == 'https://en.wikipedia.org/wiki/Philosophy':
        print('The Philosophy Wiki Crawl is a success!')
        should_break = True
