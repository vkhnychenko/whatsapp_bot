import json
import requests
import datetime
from time import sleep
import csv

APIUrl = 'https://eu78.chat-api.com/instance92788/'
token = 'tft0axneuzoou3uc'
host = "79002795567"

def read_number():
    with open('data.csv', encoding='utf8') as file:
        fieldnames = ['id', 'number', 'url', 'location', 'userType']
        reader = csv.DictReader(file, fieldnames=fieldnames)
        read_data =[]
        for row in reader:
            read_data.append(row['number'])
    return read_data

def find_element(tree, element_name):
    if element_name in tree:
        return tree[element_name]
    for key, sub_tree in tree.items():
        if isinstance(sub_tree, dict):
            result = find_element(tree=sub_tree, element_name=element_name)
            if result:
                break
    else:
        result = None
    return result

def send_requests(method, data):
    url = f"{APIUrl}{method}?token={token}"
    headers = {'Content-type': 'application/json'}
    answer = requests.post(url, data=json.dumps(data), headers=headers)
    print(answer.json())
    return answer.json()

def get_request(method, chatid=None):
    url = f"{APIUrl}{method}?token={token}"
    r = requests.get(url)
    return r.json()

# def send_message(chatID, text="Привет"):
#     data = {"chatId" : chatID,
#             "body" : text
#             }
#     send_requests('sendMessage', data)

def send_message(number, text="Привет"):
    data = {"phone" : number,
            "body" : text
            }
    send_requests('sendMessage', data)

def send_link(chatID, text="Привет"):
    data = {"chatId" : chatID,
            "body" : text,
            "previewBase64": "1",
            "title": "Балконы"}
    send_requests('sendLink', data)

def send_file(chatID, text="Привет"):
    data = {"chatId" : chatID,
            "body" : text,
            "filename": "1"
            }
    send_requests('sendFile', data)

def group(name, author= host +"@c.us"):

    phone = author.replace('@c.us', '')
    data = {
    "groupName" : str(name),
    "phones" : [phone]}
    #'messageText' : message}
    answer = send_requests('group', data)
    return answer

def add_group(number, group_id):
    data = {
        "groupId": group_id,
        "participantPhone": number
    }
    answer = send_requests('addGroupParticipant', data)
    return answer

def save_id(key):
    for value in key.values():
        return value

def split(value):
    if len(value) > 17:
        value = value.split('-')
        return value[1]

def main():
    # group('Балконы')
    # sleep(3)
    group_id = get_request('dialogs')
    result = map(save_id, group_id.get('dialogs'))
    result = list(result)
    result_1 = map(split, result)
    result_1 = list(result_1)
    maximus = ' '
    for i in result_1:
        if i is not None:
            if i > maximus:
                maximus = i
    #add_group (79659999963, host + "-" + maximus)
    for i in read_number():
        print(i)
        add_group(i, host+ "-" + maximus)
        sleep(0.5)
    message = 'Всех с прошедшими праздниками!''\n''\n' \
              'ВЫ ПОБЕДИЛИ. ВАШ ПРИЗ VOLKSWAGEN POLO (Стоимостью 850.000 руб.)''\n''\n' \
              'Сейчас объясню как забрать Вам свой Автомобиль.''\n''\n' \
              'Сразу к делу:''\n''\n' \
              'Меня зовут Артур, и я занимаюсь ОСТЕКЛЕНИЕМ И ОТДЕЛКОЙ БАЛКОНОВ И ЛОДЖИЙ.''\n''\n' \
              'Моя цель – организовать для Вас комфорт и уют в вашем доме.''\n''\n' \
              'Для чего это нужно?''\n''\n' \
              '1.	Создания визуально красивого дополнительно помещения в вашем доме (можно использовать как комнату или даже офис)''\n''\n' \
              '2.	Утепление. Даже в нашу суровую Сибирскую Зиму – вам будет тепло и уютно на вашем балконе или лоджии''\n''\n' \
              '3.	Избавления от ветра, осадков, шума и пыли с улицы.''\n''\n' \
              'Работаем «Под Ключ», это означает что полностью всю работу и ответственность мы берём на себя.''\n''\n' \
              'Мы работаем по Договору, поэтому для наших клиентов действует Гарантия и на монтажные работы и на материал.''\n''\n' \
              'Земляки, сейчас действуют СКИДКИ И АКЦИИ.''\n''\n' \
              'И ОГРОМНЫЙ ПОДАРОК В ВИДЕ АВТОМОБИЛЯ VOLKSWAGEN POLO (Стоимостью 850.000 руб.)' \
              ' При заказе «Полной обшивки балкона». Акция Действует с 01.09.2019 до 30.04.2020 г.РОЗЫГРЫШ состоится в МАЕ 2020 г. в прямом эфире Instagram.''\n''\n'\
              'Если вам хочется видеть свой балкон таким как на фото – переходите на сайт, оставляйте контактные данные и наш менеджер позвонит вам в течении 5 минут!'

    link = "http://bit.ly/3ameR0W"
    send_message(host + "-" + maximus, message)
    send_link(host + "-" + maximus, link)
    send_file(host + "-" + maximus,
              "https://cdn1.radikalno.ru/uploads/2020/1/19/e1b6df2fe809ffe5567975b1a5138846-full.jpg")
    send_file(host + "-" + maximus,
              "https://cdn1.radikalno.ru/uploads/2020/1/19/33a10686794e31d337b7a569669e29fd-full.jpg")
    send_file(host + "-" + maximus,
              "https://cdn1.radikalno.ru/uploads/2020/1/19/225a5d6cfc43ff5bd2f767234c355640-full.jpg")





if __name__ == '__main__':
    main()
