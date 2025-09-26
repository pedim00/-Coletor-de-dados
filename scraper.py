import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "http://quotes.toscrape.com"

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

quotes = []

for q in soup.select("div.quote"):
    text = q.select_one("span.text").get_text(strip=True)
    tags = ";".join([t.get_text(strip=True) for t in q.select("a.tag")])
    author = q.select_one("small.author").get_text(strip=True)
    quotes.append({"frase": text, "autor": author, "tags": tags})

df = pd.DataFrame(quotes)

df.to_csv("quotes.csv", index=False, encoding="utf-8")
print("Arquivo 'quotes.csv' salvo com sucesso!")