from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "LiaItzhakov0822"
password = "87654"
facebook_friends=["Ella","Polina","Lour", "Roei", "Mahmoud", "Yuval"]


@app.route('/', methods=["GET", "POST"])
def login():
		error = None
		if request.method == 'POST':
			if request.form['username'] == username and request.form['password'] == password:
				return render_template("home.html", friends_list=facebook_friends)
			else:
				error = 'Invalid Credentials. Please try again.'
				return error
		else: 
			return render_template('login.html')

@app.route('/friend_exist/<string:name>')
def hello_name_route(name):
    return render_template(
        'friend_exists.html', n = name, facebook_friends= facebook_friends)
  
if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)