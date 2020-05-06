def myDecorator(func):
    def wrapper():
        print('Обертка!')
        print(f'Оборачиваем функцию: {func}.')
        print('Выполняю функцию:')
        func()
        print('Закончили работать!')
    return wrapper





def multiple():
    c = 5 * 4
    print(c)

def speedTest(func):

    import time

    def wrapper():

        start = time.time()
        func()
        finish = time.time()
        print(f'Прошло {finish - start} сек')
    return wrapper



@speedTest
def search():
    import requests

    s = requests.get('https://apple.com/')

search()