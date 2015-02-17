from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	user = {'nickname': 'Colm'} # fake user
	posts = [ # fake array of posts
		{
			'author': {'nickname': 'John'},
			'body': 'Beautiful'
		},
		{
			'author': {'nickname': 'Susan'},
			'body': 'Likes movies'
		}
	]

	return render_template('index.html',
							title='Home',
							user=user,
							posts=posts)