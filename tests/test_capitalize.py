from capitalize import capitalize

if capitalize('hello') != 'Hello':
    raise Exception('Функция работает неверно!')

if capitalize('') != '':
    raise Exception('Функция работает неверно!')

if capitalize(2) != 4:
    raise Exception('Бугага! А функция-то с ошибочкой!!!')

print('Все тесты пройдены!')