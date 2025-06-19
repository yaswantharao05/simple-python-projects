import random
import requests


sure = 'https://opentdb.com/api.php?amount=1&category=32&type=boolean'

parameters = {
    'amount': 15,
    'category': random.randint(9, 32),
    'type': 'boolean'
}
response = requests.get(f'https://opentdb.com/api.php', params=parameters)
response.raise_for_status()
question_data = response.json()['results']

print(question_data)
