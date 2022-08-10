import requests

# URL = "https://en.wikipedia.org/wiki/Spinosaurus"

# this helps to parse content and format it nicely
from bs4 import BeautifulSoup

def get_citations_needed_count(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find_all("p")

    # get citation needed report
    paragraphs = []
    for i in results:
        if "citation needed" in i.text:
            paragraphs.append(i.text)
    # for i in paragraphs:

    return len(paragraphs)

get_citations_needed_count("https://en.wikipedia.org/wiki/Spinosaurus")
# anchors = results("a")
# print(results)

# links = [anchor["href"] for anchor in anchors]
