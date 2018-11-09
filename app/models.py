class News:
    '''
    Movie class to define Movie Objects
    '''

    def __init__(self,id,name,description,poster,category,language,country):
        
        
        # self.id =id
        # self.title = title
        # self.overview = overview
        # self.poster = "https://image.tmdb.org/t/p/w500/" + poster
        # self.vote_average = vote_average
        # self.vote_count = vote_count
        self.id = fox-news,
        self.name = Fox News,
        self.description = Breaking News, Latest News and Current News from FOXNews.com. Breaking news and video. Latest Current News: U.S., World, Entertainment, Health, Business, Technology, Politics, Sports.,
        self.poster = "http://www.foxnews.com",
        self.category = general,
        self.language = en,
        self.country = us




class Article:

    all_articles = []

    def __init__(self,news_id,title,imageurl,article):
        self.news_id = news_id
        self.title = title
        self.imageurl = imageurl
        self.article = article


    def save_article(self):
        Article.all_articles.append(self)


    @classmethod
    def clear_articles(cls):
        Article.all_articles.clear()

    @classmethod
    def get_articles(cls,id):

        response = []

        for article in cls.all_articles:
            if article.movie_id == id:
                response.append(article)

        return response