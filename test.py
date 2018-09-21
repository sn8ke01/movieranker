import bs4
import collections
import re
import csv

with open('movie_ratings.csv') as csvfile:
    read_csv = csv.reader(csvfile, delimiter=',')
    x = "TITANIC"
    for row in read_csv:
        #print(row)
        print(re.search(x, str(row)))


# reMovieList = collections.namedtuple('MovieList', 'rank, title, year')
#
# html = '''<h3 class="lister-item-header">
# <span class="lister-item-index unbold text-primary">1.</span>
# <a href="/title/tt0081398/?ref_=ttls_li_tt">Raging Bull</a>
# <span class="lister-item-year text-muted unbold">(1980)</span>
# </h3>
# <h3 class="lister-item-header">
# <span class="lister-item-index unbold text-primary">2.</span>
# <a href="/title/tt0081398/?ref_=ttls_li_tt">Godfather</a>
# <span class="lister-item-year text-muted unbold">(1977)</span>
# </h3>'''
#
# # print(html)
#
# soup = bs4.BeautifulSoup(html, 'html.parser')
# tags = soup.find_all('a')
# print(tags)
# t = tags[0]
# print(t)
# print(t.text)
# print('---')
# # movie_rank = [a for a in (h3.find(class_="lister-item-index unbold text-primary") for h3 in soup.find_all('h3')) if a]
# movie_title = [a for a in (h3.find('a') for h3 in soup.findAll('h3')) if a]
# m = movie_title[0]
# print(m)
# print(m.text)
# print('---')
# movie_headers = soup.find_all(class_='lister-item-header')
# print(type(movie_headers))
#
# x = 0
# while x < 2:
#     m = movie_headers[x]
#     #print(type(m))
#     print(m.text.strip())
#     print(type(m.text))
#     x = x + 1
#     #data = MovieList(rank=movie_rank, title=movie_title, year=movie_year)
    #print(data)

# movie_year = [a for a in (h3.find(class_="lister-item-year text-muted unbold") for h3 in soup.findAll('h3')) if a]
#
# print(type(movie_title))
#
# movie_rank = re.search("\d{1,3}(?=\.</span)", str(movie_rank)).group()
# yr = re.search("\(\d\d\d\d\)", str(movie_year))
# movie_year = yr.group().replace('(', '').replace(')', '')
#
# print(type(movie_title))
#
# data = MovieList(rank=movie_rank, title=movie_title, year=movie_year)
#
# print('rank:{}, title:{}, year:{}'.format(data.rank, data.title, data.year))

