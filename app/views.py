from flask import render_template, request, jsonify
from bs4 import BeautifulSoup
import requests
from app import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/getPreview', methods=['GET'])
def get_preview():
    url = request.args.get('url')
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find('title').get_text()
    description = soup.find('meta', attrs={'name': 'description'})['content']
    image = soup.find('meta', attrs={'property': 'og:image'})['content']
    return jsonify({'title': title, 'description': description, 'image': image})
