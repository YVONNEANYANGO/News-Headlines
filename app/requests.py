# from app import app
import urllib.request,json
from .models import News

# News = news.News

# Getting api key 
api_key = None
# Getting the news base url
base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']

    print(base_url)


# Getting the movie base url
# base_url = app.config["MOVIE_API_BASE_URL"]


def get_news(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(category,api_key)
    print(get_news_url)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['results']:
            news_results_list = get_news_response['results']
            news_results = process_results(news_results_list)

    return news_results


def process_results(news_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news details

    Returns :
        news_results: A list of news objects
    '''
    news_results = []
    for news_item in news_list:

        id = news_item.get('id')
        name = news_item.get('original_name')
        description = news_item.get('description')
        poster = news_item.get('poster_path')
        category = news_item.get('category')
        language = news_item.get('language')
        country = news_item.get('country')

        # id = news_item.get('id')
        # title = news_item.get('original_title')
        # overview = movie_item.get('overview')
        # poster = movie_item.get('poster_path')
        # vote_average = movie_item.get('vote_average')
        # vote_count = movie_item.get('vote_count')

        if poster:
            news_object = News(id,name,description,poster,category,language,country)
            news_results.append(news_object)

    return news_results

def get_news(id):
    get_news_details_url = base_url.format(id,api_key)

    with urllib.request.urlopen(get_news_details_url) as url:
        news_details_data = url.read()
        news_details_response = json.loads(news_details_data)

        news_object = None
        if news_details_response:
            id = news_details_response.get('id')
            name = news_details_response.get('original_title')
            description = news_details_response.get('description')
            poster = news_details_response.get('poster_path')
            category = news_details_response.get('category')
            language = news_details_response.get('language')
            country = news_details_response.get('country')

            news_object = News(id,name,description,poster,category,language,country)

    return news_object

def search_movie(movie_name):
    search_movie_url = 'https://api.themoviedb.org/3/search/movie?api_key={}&query={}'.format(api_key,movie_name)
    with urllib.request.urlopen(search_movie_url) as url:
        search_movie_data = url.read()
        search_movie_response = json.loads(search_movie_data)

        search_movie_results = None

        if search_movie_response['results']:
            search_movie_list = search_movie_response['results']
            search_movie_results = process_results(search_movie_list)


    return search_movie_results
    
    
    
    