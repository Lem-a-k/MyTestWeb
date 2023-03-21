# import json

# with open("api_test.json") as in_file:
#     json_news = json.load(in_file)
# print(json_news)

from requests import get

all_news = get('http://localhost:5000/api/news').json()
print(all_news)
for news_ in all_news['news']:
    if 'Вторая' in news_['title']:
        news_from_api = get(f'http://localhost:5000/api/news/q{news_["id"]}').json()
        print('--', news_from_api)
