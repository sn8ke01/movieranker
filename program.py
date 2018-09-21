import requests
import collections

# todo : generate a list of movies to rank
# todo : list sources :: IMDB, IFA, rotten tomatoes, meta critic
# todo : scrap movie ticket sales amd box office
# todo: IMDB Top 100 https://www.imdb.com/list/ls055592025/
# Actor Top 100 https://www.timeout.com/newyork/movies/100-best-movies-as-chosen-by-actors
# todo: AFI Top 100 https://www.afi.com/100Years/movies10.aspx

# MovieResults = collections.namedtuple(
#     'MovieResult',
# )

key = 'c3750315'
url = 'http://www.omdbapi.com/?apikey=c3750315&t='


def print_header():
    print('---------------------------')
    print('      Movie Ranker')
    print('---------------------------')


def movie_search():
    search = input('Movie to search: ')
    return search


def movie_search_list():
    # open movie file
    # pull title
    # pass title back to to main
    pass


def pull_movie(search_parm):
    response = requests.get(search_parm)

    movie_data = response.json()
    print('MOVIE DATA: {}'.format(movie_data))

    movie_dir = movie_data.get('Director')
    print('Director: {}'.format(movie_dir))

    movie_rateings = movie_data.get('Ratings')
    print('RATEINGS: {}'.format(movie_rateings))


def main():
    print_header()
    movie = movie_search()  # get movie to lookup
    title_search = url + movie  # add movie to api url
    pull_movie(title_search)  # pass in url serach parameters


if __name__ == '__main__':
    main()
