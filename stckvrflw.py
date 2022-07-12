import requests
import datetime
from pprint import pprint


def find_questions(tag=input('Введите тег для запроса:\n'), time_range=int(input('Введите количество дней:\n'))):
    finish_date = datetime.date.today()
    days_past = datetime.timedelta(days=time_range)
    start_date = finish_date - days_past
    requests_counter = 0
    for page in range(1, 10):
        url = f'https://api.stackexchange.com/2.3/questions?page={page}&fromdate={start_date}&todate={finish_date}' \
              f'&order=desc&sort=activity&pagesize=100&tagged={tag}&site=stackoverflow'
        result = []
        response = requests.get(url).json()
        if 'error_id' not in response.keys():
            for item in response['items']:
                link = item.get('link')
                result.append(link)
            requests_counter += len(result)
            pprint(f'Найдено {requests_counter} вопросов с тегом {tag}:')
            pprint(result)
        else:
            text = response['error_message'].capitalize()
            print(f'Возникла ошибка: {text}')
            break


find_questions()
