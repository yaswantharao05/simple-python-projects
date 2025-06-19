import pandas
import datetime as dt
import random
import smtplib


gmail_id = 'username@gmail.com'
gmail_password = '<password>'

birthdays_csv = pandas.read_csv('birthdays.csv')
birthdays_list = birthdays_csv.to_dict(orient='records')

today = dt.datetime.now()
today_day_month = (today.day, today.month)

for birthday_person in birthdays_list:
    if (birthday_person['day'], birthday_person['month']) == today_day_month:
        letter_file = f'letter_templates/letter_{random.randint(1, 3)}.txt'

        with open(letter_file) as letter:
            letter_text = letter.read()
            letter_text = letter_text.replace('[NAME]', birthday_person['name'])
            letter_text = letter_text.replace('Angela', 'Yaswantha Rao ')

        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=gmail_id, password=gmail_password)
            connection.sendmail(from_addr=gmail_id, to_addrs=birthday_person['email'],
                                msg=f'Subject:Birthday Wishes!!\n\n'
                                    f'{letter_text}')
