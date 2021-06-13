"""
6. * Реализовать структуру данных «Товары».
   Она должна представлять собой список кортежей.
   Каждый кортеж хранит информацию об отдельном товаре.
   В кортеже должно быть два элемента — номер товара и словарь с параметрами
       (характеристиками товара: название, цена, количество, единица измерения).
   Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
   Пример готовой структуры:
   [
   (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
   (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
   (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
   ]
   Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
       например название, а значение — список значений-характеристик, например список названий товаров.
   Пример:
   {
   “название”: [“компьютер”, “принтер”, “сканер”],
   “цена”: [20000, 6000, 2000],
   “количество”: [5, 2, 7],
   “ед”: [“шт.”]
   }
"""

exit_codes = ['q', 'e', 'quit', 'exit']
add_codes = ['a', 'add', 'д', 'добавить']
analytics_codes = ['an', 'analytics', 'ан', 'аналитика']


def cmd_show_help():
    print(', '.join(exit_codes), " - выйти из программы")
    print(', '.join(add_codes), " - добавить товар")
    print(', '.join(analytics_codes), " - показать аналитику")


def cmd_add(products):
    print('Добавление товара:')
    name = input('Название: ')
    price = input('Цена: ')
    count = input('Количество: ')
    dimens = input('Единица измерения: ')

    product = {'название': name,
               'цена': price,
               'количество': count,
               'eд': dimens,
               }
    products.append((len(products), product))
    print('Товар добавлен!')


def cmd_show_analytics(products):
    print('Аналитика:')
    all_keys = set()
    for product_id, product in products:
        for key in product.keys():
            all_keys.add(key)

    analytics = dict()
    for key in all_keys:
        items = set()
        analytics[key] = items
        for product_id, product in products:
            try:
                items.add(product[key])
            except:
                pass
    print(analytics)


# products = [
#     (1, {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'eд': 'шт.'}),
#     (2, {'название': 'принтер', 'цена': 6000, 'количество': 2, 'eд': 'шт.'}),
#     (3, {'название': 'сканер', 'цена': 2000, 'количество': 7, 'eд': 'шт.'})
# ]
products = []

while True:
    cmd = input(">")
    if len(cmd) == 0:
        cmd_show_help()
    elif cmd in exit_codes:
        break
    elif cmd in add_codes:
        cmd_add(products)
    elif cmd in analytics_codes:
        cmd_show_analytics(products)
    else:
        cmd_show_help()
print("end")
