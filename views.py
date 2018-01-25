from flask import render_template
from app import app

#views
@app.route('/')
def index():

	'''
	view root page function that returns the index page and its data
	'''
	message = 'News Highlights'
	return render_template('index.html', message = message)

	@app.route('/articles/<source_id>')
	def articles(source_id):

		'''
		view source page function that returns the news details page and its data
		'''
		return render_template('articles.html,'id = source_id)