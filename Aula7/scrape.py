import requests
from bs4 import BeautifulSoup
import shelve
from tqdm import tqdm

r = requests.get("https://www.jn.pt/")
soup = BeautifulSoup(r.text, features="html.parser")

pattern = r"jn.pt/\w+/"
articles = soup.find_all("article")

news_dict = shelve.open("news_dict.db")

def visit_noticia(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, features="html.parser")
    title = soup.find("h1", {'rel' : 'headline'}).text
    content = soup.find('div', {'class': 't-article-content-inner'})
    tags_section = soup.find('div', {'class': 't-article-funcs-tags-1'})
    tags = []
    if tags_section:
        tags = [ t.text for t in tags_section.findAll('li') ]
    

    date = content.find("time")["content"]
    content.div.decompose()
    noticia = {
        'title': title,
        'date': date,
        'content' : content.text,
        'tags': tags
    }
    # TODO: get related news urls

    return noticia

noticias = []
for article in articles:
    header = article.h3
    if header is None:
        continue

    url = header.a
    if url is None:
        continue

    url_address = url["href"]
    title = article.h2.a.text
    if url_address.startswith("http"):
        continue

    noticias.append((title, url_address))

for noticia in tqdm(noticias):
    url = 'https://jn.pt' + noticia[1]
    if url not in news_dict:
        noticia_parsed = visit_noticia(url)
        news_dict[url] = noticia_parsed

news_dict.close()   