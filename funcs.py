import json
import datetime


def filter_transactions(filename):
    """Функция фильтрует транзакции по Executed и приводит дату и время к необходимому формату"""
    with open(filename, 'r', encoding='utf-8') as f:
        operations = json.load(f)

    new_operations = []

    for operation in operations:
        if not (operation.get('from') and operation.get('state')):
            continue
        if operation['state'] == 'EXECUTED':
            date = datetime.datetime.strptime(operation['date'], '%Y-%m-%dT%H:%M:%S.%f')
            date = date.strftime('%d.%m.%Y')
            new_operations.append(
                {'date': date,
                 'description': operation['description'],
                 'from': operation['from'],
                 'to': operation['to'],
                 'operationAmount': operation['operationAmount']
                 })

    return new_operations


def sort_dict(operations):
    """Функция сортирует список транзакций по дате"""
    sorted_dict = sorted(operations, key=lambda x: datetime.datetime.strptime(x['date'], '%d.%m.%Y'), reverse=True)
    return sorted_dict


def hide_digits(account):
    """Функция скрывает часть строки звездочками"""
    account_number = account.split(' ')[-1]
    card_name = ' '.join(account.split(" ")[:-1])
    if len(account_number) == 20:
        return f'Счет **{account_number[16:]}'
    else:
        return f'{card_name} {account_number[:7] + "*"*6 + account_number[12:]}'


def get_transactions(filename):
    """Функция получает нужное количество транзакций"""
    counter = 0
    sorted_dict = sort_dict(filter_transactions(filename))
    while counter != 5:
        print(f'''{sorted_dict[counter]["date"]} {sorted_dict[counter]["description"]}
{hide_digits(sorted_dict[counter]["from"])} -> {hide_digits(sorted_dict[counter]["to"])}
{sorted_dict[counter]["operationAmount"]['amount']} {sorted_dict[counter]["operationAmount"]['currency']['name']}
''')
        counter += 1
