import requests
from bs4 import BeautifulSoup

MOVIES_ENDPOINT = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(MOVIES_ENDPOINT)
m_list = response.text

soup = BeautifulSoup(m_list, 'html.parser')
m_titles = soup.find_all(name="h3", class_="title")

movies_list= [(title.string) for title in m_titles]
movies_list.reverse()


with open('movies.txt', 'a', encoding='utf-8') as movie_file:
    for movie in movies_list:
        movie_file.write(movie + "\n")

