#Created by Angelo Paolo Calitis
#This is the Python backend for the Smart News Google Chrome extension
#Created for CSUMB Hackathon on the weekend of 11/3/2018

from flask import Flask, render_template, flash, redirect, Response, request
from flask_bootstrap import Bootstrap
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from textblob import TextBlob
import sys
import random, json
import requests

#import sys
#print sys.argv[0] # prints python_script.py
#print sys.argv[1] # prints var1
#print sys.argv[2] # prints var2

#NECESSARY, DON'T TOUCH
app = Flask(__name__)
app.config['SECRET_KEY'] = 'smart-news-is-the-best-fake-news-extension'
bootstrap = Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])
def index():
  #News article to open
  #THIS IS THE ONE THAT NEEEDS TO BE FED
  #feed me
  #source_site = request.get_json()

  #change this to go to a different site
  source_site = "https://www.npr.org/sections/health-shots/2018/11/03/663155917/ready-for-the-time-change-here-are-tips-to-stay-healthy-during-dark-days-ahead"

  #Pass a valid user agent for request
  req = Request(
    source_site,
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0'}
  )
  #'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0'
  #'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'

  #Open a response and pass onto BeautifulSoup
  resp = urlopen(req)
  bs_obj = BeautifulSoup(resp.read(), 'lxml')

  #retrieve the headline's tag
  headline = str(bs_obj.find('h1'))
  #TEST = headline

  #extract headline from between tag
  h1_open = headline.find('>') + 1
  h1_close = headline.find('<', h1_open)
  headline = headline[h1_open:h1_close]

  #extract noun phrases
  blob = TextBlob(headline)
  singles_count = 0
  phrase_list = []
  for np in blob.noun_phrases:
    miniblob = TextBlob(str(np))
    if len(miniblob.words) == 1:
        phrase_list.append(np)
        singles_count += 1
        if singles_count == 2:
            break
    else:
        new_np = str(np).replace(" ", "%20")
        phrase_list.append(new_np)
        break

  polarity = blob.sentiment.polarity 
  subjectivity = blob.sentiment.subjectivity 

  if polarity < 0:
    statement = "'" + str(blob) + "' has a lean towards negativity, "
  elif polarity == 0:
    statement = "'" + str(blob) + "' has a neutral stance, "
  else:
    statement = "'" + str(blob) + "' has a lean towards positivity, "

  if subjectivity < 0.499:
    statement = statement + "and a more objective stance."
  else:
    statement = statement + "and a more subjective stance."

  #retrieve Bing soup
  phrase_list = "%20".join(phrase_list)
  bing_url = "https://www.bing.com/news/search?q={0}".format(phrase_list)
  req = Request(bing_url, headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0'})
  resp = urlopen(req)
  bs_obj = BeautifulSoup(resp.read(), 'lxml')
  content_list = bs_obj.find_all('a', class_='title')
  #title_list = []
  #url_list = []
  article_dict = {}
  title_counter = 0
  for article in content_list:
    #title_list.append(article.get_text())
    #url_list.append(article.get("href"))
    title_counter += 1
    article_dict[article.get_text()] = article.get("href")
    if title_counter == 4:
        break
  #render the page
  return render_template('result.html', article_dict = article_dict, statement = statement)

#NECESSARY(?) DON'T TOUCH
#if __name__ == '__main__':    
#  app.run(host='0.0.0.0')