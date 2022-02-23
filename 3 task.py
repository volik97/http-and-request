import requests
from datetime import datetime


def stackoverflow_questions(days, tag):
    start_time = int(datetime.timestamp(datetime.now()))
    end_time = start_time - days * 86400
    url = 'https://api.stackexchange.com/2.3/questions'
    params = {
        'fromdate': end_time,
        'todate': start_time,
        'tagged': tag,
        'site': 'stackoverflow'
    }
    response = requests.get(url, params=params)
    for question in response.json().get('items'):
        print(f'Title: {question["title"]}\n'
              f'Tags: {question["tags"]}\n'
              f'-----')


stackoverflow_questions(2, 'python')
