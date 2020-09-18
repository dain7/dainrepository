from flask import Flask, redirect, render_template, request, url_for
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import requests
from selenium import webdriver
import time
import pandas as pd
import random
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)


UPLOAD_FOLDER = 'templates/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result3', methods=['POST'])
def upload_image():
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # flash('성공적으로 업로드 되었습니다.')
        return render_template('result3.html', filename= 'templates/' + filename)

# @app.route('/result3')
# def display_image(filename):
#     return render_template('result3.html', filename='uploads/' + filename)

@app.route('/result1', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        number = request.form['number']
        concept = request.form['concept']
        place = request.form['place']

        baseUrl = 'https://www.pinterest.co.kr/search/pins/?q='
        if number == 'solo':
            url = baseUrl + str(number) + ' ' + str(place) + ' photoshoot'
        else:
            url = baseUrl + str(number) + ' ' + str(concept) + ' ' + str(place) + ' poses'

        crawl_num = 15

        browser = webdriver.Chrome()
        browser.get(url)
        time.sleep(3)
        ret = browser.page_source
        browser.close()
        soup = bs(ret, "html.parser")
        img = soup.find_all('img')


        img_list = []
        n = 1

        for i in img:
            imgUrl = i['src']
            img_list.append(imgUrl)

            n += 1
            if n > crawl_num:
                break

        list1 = img_list[0:4]
        list2 = img_list[4:8]
        list3 = img_list[8:12]

        return render_template('result1.html', list1=list1, list2=list2, list3=list3, len = len(img_list))



@app.route('/result2', methods=['POST', 'GET'])
def result2():
    if request.method == 'POST':
        area = request.form['area']
        search = request.form['search']

        place_df = pd.read_excel('./place.xlsx')

        place_df2 = place_df.loc[place_df['address'].str.contains(area, na=False)]
        place_df3 = place_df2.loc[place_df['title'].str.contains(search, na=False)]

        place_list = place_df3.values.tolist()
        place_list2 = random.sample(place_list, 5)

    return render_template('result2.html', list1=place_list2)
        # , area=area , search=search, list1=place_list2, len1 = len(place_list2))


if __name__ == '__main__':
    app.run( debug=True)
