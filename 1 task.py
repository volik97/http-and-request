import requests

token = '2619421814940190'
urls = [
    f'https://superheroapi.com/api/{token}/search/Hulk',
    f'https://superheroapi.com/api/{token}/search/Captain America',
    f'https://superheroapi.com/api/{token}/search/Thanos'
]


def get_urls(url_all):
    r = (requests.get(url) for url in url_all)
    return r


def get_hero_list():
    heroes = []
    for item in get_urls(urls):
        intelligence = item.json()
        for stats in intelligence['results']:
            heroes.append({
                'name': stats['name'],
                'intelligence': stats['powerstats']['intelligence']
            })
    return heroes


def compare():
    int_hero = 0
    name_hero = ''
    for hero in get_hero_list():
        if int_hero < int(hero['intelligence']):
            int_hero = int(hero['intelligence'])
            name_hero = hero['name']
    print(f'Самый умный герой {name_hero}')


if __name__ == '__main__':
    get_urls(urls)
    compare()
