import requests

url_full_list = 'https://akabab.github.io/superhero-api/api/all.json'
heroes_to_compare = ['Hulk', 'Captain America', 'Thanos']


def search_heroes(url, heroes_list):
    intelligence_level = int()
    hero_with_top_intelligence_level = ''
    response = requests.get(url).json()
    for name in heroes_list:
        for item in response:
            if item['name'] == name:
                intelligence = item['powerstats']['intelligence']
                if intelligence > intelligence_level:
                    hero_with_top_intelligence_level = item['name']
                    intelligence_level = item['powerstats']['intelligence']
    return f'Самый умный герой - {hero_with_top_intelligence_level}. Его уровень интеллекта = {intelligence_level}!'


if __name__ == '__main__':
    print(search_heroes(url_full_list, heroes_to_compare))
