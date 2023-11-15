from flask import Flask, render_template, url_for
from parse_data import get_data_index, get_data_about, get_data_blogs
import requests
from bs4 import BeautifulSoup as BS

url_news = 'https://stopgame.ru/news/all/p1'  #Меняем страницы
req_news = requests.get(url_news)
soup_news = BS(req_news.text, 'lxml')

url_blogs = 'https://stopgame.ru/blogs/all/p1'
req_blogs = requests.get(url_blogs)
soup_blogs = BS(req_blogs.text, 'lxml')


app = Flask(__name__)

@app.route('/')
@app.route('/home')
def main_page():
    names, hrefs = get_data_index(soup_news)
    return render_template('index.html', data=zip(names, hrefs))

@app.route('/about')
def about_page():
    article_name, article_href, article_img = get_data_about(soup_news)
    return render_template('about.html', data=zip(article_name, article_href, article_img))

@app.route('/blogs')
def games_page():
    blog_name, blog_href, blog_img = get_data_blogs(soup_blogs)
    return render_template('blogs.html', data=zip(blog_name, blog_href, blog_img))

@app.route('/contact')
def contacts_page():
    return render_template('contact.html')


if __name__ == "__main__":
    app.run(debug=True)