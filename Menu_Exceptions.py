from Product import Product

product1 = Product()

menu = '''1. Изменить название
2. Изменить количество
3. Изменить поставщика
4. Изменить производителя
5. Изменить стоимость
6. Изменить местоположение (адрес)
7. Изменить срок годности
8. Изменить категорию
9. Добавить примечание
10. Подтвердить получение товара
11. Списать товар 
12. Получить полную информацию о товаре
13. Выйти из программы

'''

print('Добро пожаловать в программу, получен новый товар, выберите желаемое действие')


user_choice = 0

# Цикл работает, пока пользователь не выберет выход или товар не будет списан
while user_choice != 13 and product1.condition != 'Списан':

    try:
        user_choice = int(input(menu))

        if user_choice not in range(1, 14):
            raise ValueError('Выберите число от 1 до 13')

    except ValueError as ve:
        print(ve)
        continue

    user_change = None

    if 1 <= user_choice <= 9:
        user_change = input('Введите новое значение: ')

    match user_choice:
        case 1:
            product1.set_name(user_change)
        case 2:
            product1.set_quantity(user_change)
        case 3:
            product1.set_supplier(user_change)
        case 4:
            product1.set_manufacturer(user_change)
        case 5:
            product1.set_cost(user_change)
        case 6:
            product1.set_location(user_change)
        case 7:
            product1.set_expiry_date(user_change)
        case 8:
            product1.set_category(user_change)
        case 9:
            product1.set_note(user_change)
        case 10:
            product1.confirm_receipt()
        case 11:
            product1.write_off()
        case 12:
            print(product1)
