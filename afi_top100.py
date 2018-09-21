import requests
import bs4
import re
import csv
import collections


def get_html():
    url = 'https://www.afi.com/100Years/movies10.aspx'
    response = requests.get(url)
    return response.text


def get_movie_list(html):
    movie_data = []

    soup = bs4.BeautifulSoup(html, 'html.parser')
    title = soup.find_all(class_='filmTitle')

    for t in title:
        movie_data.extend(t)

    return movie_data


def generate_csv_data(movie_list):
    for index, entry in enumerate(movie_list):
        entry = entry.strip()
        entry = entry.replace('(', '').replace(')', '').replace('.', '')

        entry = re.sub(' ', ',', entry, 1)
        entry = re.sub('\s(?=\d{4})', ',', entry)
        print('{},{}'.format(entry, index + 1))




def main():
    # print(response.status_code)
    # print(response.text)
    html = get_html()
    movie_list = get_movie_list(html)
    generate_csv_data(movie_list)


if __name__ == '__main__':
    main()
