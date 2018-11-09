from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_movies,get_movie,search_movie
from ..models import Review
from .forms import ReviewForm
# Review = reviews.Review


# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular movie
    most_recent_news = get_news('most_recent')
    recent_news = get_news('recent')
    past_news = get_news('past')

    title = 'Home-Page - Welcome to News Update Review Website Online'

    search_news = request.args.get('news_query')

    if search_news:
        return redirect(url_for('main.search',news_heading=search_news))
    else:
        return render_template('index.html', title = title, most_recent = most_recent_news, recent = recent_news, past = past_news )



@main.route('/search/<news_headline>')
def search(news_headline):
    '''
    View function to display the search results
    '''
    news_headline_list = news_headline.split(" ")
    news_headline_format = "+".join(news_headline_list)
    searched_news = search_news(news_headline_format)
    title = f'search results for {news_headline}'
    return render_template('search.html',news = searched_news)


@main.route('/news/<int:id>')
def news(id):

    '''
    View news page function that returns the news details page and its data
    '''
    news = get_news(id)
    title = f'{news.title}'
    reviews = Review.get_reviews(news.id)

    return render_template('news.html',title = title,news = news,reviews = reviews)

@main.route('/news/review/news/<int:id>', methods = ['GET','POST'])
def new_review(id):
    form = ReviewForm()
    movie = get_news(id)

    if form.validate_on_submit():
        title = form.title.data
        review = form.review.data
        new_review = Review(news.id,title,news.poster,review)
        new_review.save_review()
        return redirect(url_for('main.news',id = news.id ))

    title = f'{news.title} review'
    return render_template('new_review.html',title = title, review_form=form, news=news)    