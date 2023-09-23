# + Web Scraping com Python usando requests e bs4 BeautifulSoup
# - Web Scraping é o ato de "raspar a web" buscando informações de forma
# automatizada, com determinada linguagem de programação, para uso posterior.
# - O módulo requests consegue carregar dados da Internet para dentro do seu
# código. Já o bs4.BeautifulSoup é responsável por interpretar os dados HTML
# em formato de objetos Python para facilitar a vida do desenvolvedor.
# - Doc: https://www.crummy.com/software/BeautifulSoup/bs4/doc.ptbr/
# + Instalação
# - pip install requests types-requests bs4

import requests
from bs4 import BeautifulSoup

url = "http://localhost:5500/Python's%20Module/HTTP%20Protocolo/page/"
resposnse = requests.get(url)
raw_html = resposnse.text  # html puro
# transformadno em objetos python
parsed_html = BeautifulSoup(raw_html, "html.parser", from_encoding="utf8")

# podemos usar as tags do html como props
print(parsed_html.title)
if parsed_html.title is not None:
    print(parsed_html.title.text)
# pegando textos com selector
tag_top_jobs = parsed_html.select_one("#intro > div > div > article > h2")
if tag_top_jobs is not None:
    print(tag_top_jobs.text)
    if tag_top_jobs.parent is not None:
        for p in tag_top_jobs.parent.select("p"):
            print(p.text)
