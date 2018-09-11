# coding: UTF-8
import requests
import json
import os
import datetime
from bs4 import BeautifulSoup

# Slack の設定
WEB_HOOK_URL = os.environ['webHookURL']

url = os.environ['qiitaURL']

def lambda_handler(event, context):
  response = requests.get(url)
  soup = BeautifulSoup(response.text, 'html.parser')
  trends = json.loads(soup.select('div[data-hyperapp-app]')[2].get('data-hyperapp-props'))
  # UTCなんで9時間ずれるっぽい
  now = datetime.datetime.now()
  now = now + datetime.timedelta(hours=9)
  text = 'QiitaトレンドランキングTop20（' + now.strftime('%Y/%m/%d %H') + '時更新）'
  rank = 1
  for (edge) in trends['trend']['edges'] :
    targetUrl = url + edge['node']['author']['urlName'] + '/items/' + edge['node']['uuid']
    text += '\n' + str(rank) + '位: <' + targetUrl + '|' + edge['node']['title'] + '>'
    rank += 1
  requests.post(WEB_HOOK_URL, data = json.dumps({
    'text': text
  }))
