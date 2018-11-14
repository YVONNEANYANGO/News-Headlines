# from app import app
import urllib.request,json
from .models import *
from . import main
# from .models import Source
# from .models import Article

# News = news.News

# Getting api key 
api_key = None
# Getting the news base url
base_url = None
# base_url=None
NEWS_API_BASE_URL = None
# base_url=




def configure_request(app):
    global api_key,base_url,article_url
    api_key = app.config['API_KEY']
    # print(api_key)
    
    base_url = app.config['NEWS_API_BASE_URL']
    # article_url = app.config['ARTICLE_API_BASE_URL']
    
    # print(base_url.format("bbc-news",api_key))


# Getting the movie base url
# base_url = app.config["MOVIE_API_BASE_URL"]


def get_news(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(category,api_key)
    print(get_news_url)
    news_results = None

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)


        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results = process_articles(news_results_list)

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
        author = news_item.get('author')
        description = news_item.get('description')
        urlToImage = news_item.get('urlToImage')
        category = news_item.get('category')
        language = news_item.get('language')
        country = news_item.get('country')

        # id = news_item.get('id')
        # title = news_item.get('original_title')
        # overview = movie_item.get('overview')
        # poster = movie_item.get('poster_path')
        # vote_average = movie_item.get('vote_average')
        # vote_count = movie_item.get('vote_count')

        if urlToImage:
            news_object = News(id,name,description,poster,category,language,country)
            news_results.append(news_object)

    return news_results
def process_articles(source):
    source_articles = []
    for item_article in source:
        author = item_article.get('author')
        title = item_article.get('title')
        description = item_article.get('description')
        url = item_article.get('url')
        urlToImage = item_article.get('urlToImage')
        publishedAt = item_article.get('publishedAt')
        if urlToImage:
            articles_object = Articles(author,title,description,url,urlToImage,publishedAt)
            source_articles.append(articles_object)
    return source_articles
# def get_news(id):
#     get_news_url = base_url.format(id,api_key)
#     print(get_news_url)

#     with urllib.request.urlopen(get_news_url) as url:
#         news_data = url.read()
#         news_response = json.loads(news_data)

#         news_object = None
#         if news_response:
#             id = news_response.get('id')
#             name = news_response.get('original_name')
#             description = news_response.get('description')
#             poster = news_response.get('poster_path')
#             category = news_response.get('category')
#             language = news_response.get('language')
#             country = news_response.get('country')

#             news_object = News(id,name,description,poster,category,language,country)

#     return news_object

# def search_news(news_name):
#     search_news_url = 'https://api.themoviedb.org/3/search/movie?api_key={}&query={}'.format(api_key,news_name)
#     with urllib.request.urlopen(search_news_url) as url:
#         search_movie_data = url.read()
#         search_movie_response = json.loads(search_movie_data)

#         search_movie_results = None

#         if search_movie_response['results']:
#             search_movie_list = search_movie_response['results']
#             search_movie_results = process_results(search_movie_list)


#     return search_news_results
    
    
    
    