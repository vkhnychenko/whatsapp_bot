import json
import requests
import datetime
from time import sleep
import csv

APIUrl = 'https://eu78.chat-api.com/instance92788/'
token = 'tft0axneuzoou3uc'

def read_number():
    with open('avito.csv', encoding='utf8') as file:
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

def send_message(chatID, text="Привет"):
    data = {"chatId" : chatID,
    "body" : text}
    send_requests('sendMessage', data)

def group(name, author= "79002795567@c.us"):
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
              ' При заказе «Полной обшивки балкона». Акция Действует с 01.09.2019 до 30.04.2020 г.РОЗЫГРЫШ состоится в МАЕ 2020 г. в прямом эфире Instagram.''\n''\n' \
              'Если вам хочется видеть свой балкон таким как на фото – переходите на сайт, оставляйте контактные данные и наш менеджер позвонить вам в течении 5 минут!'
    phone = author.replace('@c.us', '')
    data = {
    "groupName" : str(name),
    "phones" : [phone, 79659999963],
    'messageText' : message}
    answer = send_requests('group', data)
    return answer

def add_group(number, group_id):
    data = {
        "groupId": group_id,
        "participantPhone": number
    }
    answer = send_requests('addGroupParticipant', data)
    return answer

# def send_message(chatid, message):
#     data = {"chatId": chatid,
#             "body": message}
#     send_requests('sendMessage', data)


def main():
    #print(read_number())
    #group('Балконы')
    sleep(3)
    group_id = get_request('dialogs')
    print(group_id.get('dialogs'))
    answer = len(group_id.get('dialogs'))
    print(answer)
    for key in group_id.get('dialogs'):
        #ids = [i for i in key]
        id =find_element(key, 'id')
        print(id)
        id = id.split('-')
        try:
            print(id[1])
            ids = []
            ids.append(id[1])
        except:Exception
    print(ids)
    log = add_group(79530888073, "79002795567-" + ids[0])
    print(type(log))
    print(log.get('add'))
    num = [79530888073, 79000002442, 79659999963, 79930099309, 79537870750, 79520708038]
    for i in num:
        log = add_group(i, "79002795567-" + ids[0])
        sleep(1)
        answer = group_id.get('dialogs')
        for key in group_id.get('dialogs'):
            participants = find_element(key, 'participants')
            try:
                print(participants)
                if (len(participants) >= 5):
                    break
            except:Exception
    #send_message("79002795567-" + ids[0], "Privet")
    #for i in read_number():
        #print(i)




if __name__ == '__main__':
    main()
