import requests
from bs4 import BeautifulSoup


def create_soup(url):
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup

def scrape_weather():
    url = "https://blog.naver.com/youngcheart"
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    soup.find("p", attrs={"class": "cast_txt"}).get_text()
    curr_temp = soup
    

def scrape_headline_news():
    url = "https://blog.naver.com/youngcheart"
    soup = create_soup(url)
    news_list = soup.find("ul", attrs={"class": "clear"}).find_all("li")
    for index, news in enumerate(news_list):
        title = news.find("a").get_text.strip()
        link = url + news.find("a")["href"]
        print("{} . {}".format(index+1, title))



if __name__ == "__main__":
    scrape_headline_news();