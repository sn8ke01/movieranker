import requests
import bs4
import re
import csv
import collections


MovieList = collections.namedtuple('MovieList', 'rank, title, year')

def get_html():
    url = 'https://www.imdb.com/list/ls055592025/'

    response = requests.get(url)
    # print(response.status_code)
    # print(response.text)

    return response.text


def get_movie_list(html):
    movie_data = []
    imdb_data = []
    soup = bs4.BeautifulSoup(html, 'html.parser')

    movie_headers = soup.find_all(class_='lister-item-header')

    for t in movie_headers:
        movie_title = re.search("[\da-zA-Z\s\-\.\'\:\,]{1,100}(?=\</a\>)", str(t)).group()
        movie_rank = re.search("\d{1,3}(?=\.</span)", str(t)).group()
        yr = re.search("\(\d\d\d\d\)", str(t))
        movie_year = yr.group().replace('(', '').replace(')', '')
        # print('{},{},{}'.format(rank, title, year))
        # todo: open csv and write
        data = MovieList(rank=movie_rank, title=movie_title, year=movie_year)
        print('{},{},{}'.format(data.title, data.year,data.rank))




def generate_csv_data(movie_list):
    pass


def main():
    html = get_html()
    movie_list_report = get_movie_list(html)
    # print('{},{},{}'.format(movie_list_report.rank, movie_list_report.year,movie_list_report.title))
    # generate_csv_data(movie_list)


if __name__ == '__main__':
    main()
