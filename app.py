from flask import Flask, render_template
from fastapi import FastAPI, Depends, Request, Query
import uvicorn
app = FastAPI()


@app.get('/')
def index():
    return 'Hello, World!'

@app.get('/about')
def about():
    return 'This is the about page.'

@app.get('/user/<username>')
def user_profile(username):
    return f'Hello, {username}!'

if __name__ == '__main__':
    #  localhost:5000
    uvicorn.run('app:app', port=8080, host='0.0.0.0')
