from flask import render_template
from app import app

#views
@main.route('/')
def index():

	'''
	view root page function that returns the index page and its data
	'''
	 title = 'Home - Welcome to The best News Highlights Website Online'
	news_sources = get_sources('sources')
    return render_template('index.html', title=title, sources=news_sources)

@main.route('/articles/<int:source_id>')
def articles(source_id):
	'''
	view source page function that returns the news details page and its data
	'''
	title = f"{source_id} page"
    #title = "Hello"
    articles = get_articles(source_id)
    return render_template('articles.html',title = title, articles = articles)