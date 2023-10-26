from flask import Flask, render_template, request
import requests
import json
import asyncio
from truecallerpy import search_phonenumber
app = Flask(__name__)
url='http://api.open-notify.org/astros.json'


@app.route('/', methods=['GET', 'POST'])
def index():
    response = None
    if request.method == 'POST':
        user_question = request.form['question']
        response=truecaller(user_question)
        
        
    return render_template('index.html', response=response)

def truecaller(question):
    country_code = "IN"
    installation_id = "a1i0i--ifRmGhkcVk07rjaLoknY47JojN95rZ35OKIl0taoPXcjnLyUR67-rK_o3"

    response = asyncio.run(search_phonenumber(question, country_code, installation_id))
    
    return response


if __name__ == '__main__':
    app.run(debug=True)