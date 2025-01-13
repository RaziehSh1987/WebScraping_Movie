from bs4 import BeautifulSoup
import requests #to get whole of the data

response=requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")  # get whole of data of website
yc_web_page= response.text #it's the same when we rk on the website>source

soup=BeautifulSoup(yc_web_page,"html.parser")
# print(soup.prettify())
titlee=soup.find_all("h3",class_="title")

# for title in titlee:
#     print(title.getText())
# or:
movie_title=[title.getText() for title in titlee]

# for n in range(len(movie_title)-1,0,-1):
#   print(n)
# or:
movies=movie_title[::-1] #[star of the list:stop(end of the list):-1(inverse the order of list)]

with open("movies.text",mode='w') as file:
    for movie in movies:
        print(movie)
        file.write(f"{movie}\n")
