from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'This is the about page.'

@app.route('/user/<username>')
def user_profile(username):
    return f'Hello, {username}!'

if __name__ == '__main__':
    #  localhost:5000
    app.run(debug=True, port=8080)
