"""main.py"""
from fastapi import FastAPI
#importing the fastapi framework

#create an instance of the FastAPI class

#an application object
app = FastAPI()

#decorator pattern
@app.get('/')
def home():
    return 'Hello World!!!!!'

@app.get('/contact')
def contact():
    return "Contact Us"
