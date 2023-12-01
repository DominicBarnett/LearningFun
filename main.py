from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    """A homepage with handy links for your convenience."""
    return render_template('main.html')

@app.route('/createaccount')
def createpage():
    '''Create an account'''
    return render_template('create_account.html')

@app.route('/accountcreated')
def account_created_redirect():
    '''redirct to child personality'''
    return render_template('child_personality.html')


if __name__ == '__main__':
    app.config['ENV'] = 'development'
    app.run(debug=True)