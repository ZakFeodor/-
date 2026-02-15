from datetime import datetime


class Product:
    """Класс для управления партией товара."""

    def __init__(self) -> None:
        """Инициализация карточки товара со значениями по умолчанию."""

        self.name = 'Не указано'
        self.quantity = 0
        self.condition = 'Не поступил/ожидает поступления'
        self.supplier = 'Не указан'
        self.manufacturer = 'Не указан'
        self.cost = 0
        self.location = 'Не указан'
        self.expiry_date = 'Не указан'
        self.category = 'Не указана'
        self.note = ''

    def set_name(self, name):
        """Устанавливает название товара.

        Args:
            name: Название товара.
        """

        if name:
            self.name = name
        else:
            print('Имя должно состоять хотя бы из одного символа')

    def set_quantity(self, quantity):
        """Устанавливает количество товара.

        Args:
            quantity: Количество товара (ожидается целое число > 0).
        """

        try:
            self.quantity = int(quantity)

            if self.quantity <= 0:
                raise ValueError('Указано некорректное количество товара (<= 0)')

        except ValueError as ve:
            print(f'Введено не целое число: {ve}')

    def set_supplier(self, supplier):
        """Устанавливает поставщика товара.

        Args:
            supplier: Имя поставщика (должно быть в списке допустимых).
        """

        list_of_possible_suppliers = ['Muscat', 'Peppe', 'Munat', 'Jerry']

        if supplier in list_of_possible_suppliers:
            self.supplier = supplier
        else:
            print(f'Поставщик должен быть из следующего списка {list_of_possible_suppliers}')

    def set_manufacturer(self, manufacturer):
        """Устанавливает производителя товара.

        Args:
            manufacturer: Имя производителя (должно быть в списке допустимых).
        """

        list_of_possible_manufacturers = ['Zimbo', 'Jelle', 'Ugma', 'Qurat', 'Oraq']

        if manufacturer in list_of_possible_manufacturers:
            self.manufacturer = manufacturer
        else:
            print(f'Производитель должен быть из следующего списка {list_of_possible_manufacturers}')

    def set_cost(self, cost):
        """Устанавливает стоимость товара.

        Args:
            cost: Стоимость товара (ожидается целое число > 0).
        """

        try:
            self.cost = int(cost)

            if self.cost < 0:
                raise ValueError('Указана некорректная стоимость товара (< 0)')

        except ValueError as ve:
            print(f'Введено не целое число: {ve}')

    def set_location(self, location):
        """Устанавливает местоположение товара на складе.

        Args:
            location: Адрес хранения (должен быть в списке допустимых).
        """

        list_of_possible_locations = ['507 E 9th St', '201 N Tryon St', '551 S Tryon St', '750 E 9th St']

        if location in list_of_possible_locations:
            self.location = location

        else:
            print(f'Локация должна быть из следующего списка {list_of_possible_locations}')

    def set_expiry_date(self, expiry_date):
        """Устанавливает срок годности товара.

        Args:
            expiry_date: Дата окончания срока годности в формате 'ДД.ММ.ГГГГ'.
        """

        try:
            datetime.strptime(expiry_date, '%d.%m.%Y')

        except ValueError as ve:
            print(f'Введена некорректная дата: {ve}')

        else:
            self.expiry_date = expiry_date

    def set_category(self, category):
        """Устанавливает категорию товара.

        Args:
            category: Категория товара (должна быть в списке допустимых).
        """

        list_of_possible_categories = ['electronics', 'food', 'jewelery', 'medicines']

        if category in list_of_possible_categories:
            self.category = category
        else:
            print(f'Категория должна быть из следующего списка {list_of_possible_categories}')

    def set_note(self, note):
        """Добавляет примечание к товару.

        Args:
            note: Текст примечания.
        """

        self.note = note

    def confirm_receipt(self):
        """Подтверждает получение товара, меняя статус на 'Поступил'."""

        if self.condition == 'Не поступил/ожидает поступление':
            self.condition = 'Поступил'
        else:
            print(f"Текущий статус {self.condition} не позволяет перейти к статусу 'Поступил'")

    def write_off(self):
        """Списывает товар, меняя статус на 'Списан'."""

        if self.condition == 'Поступил':
            self.condition = 'Списан'
        else:
            print(f"Текущий статус {self.condition} не позволяет перейти к статусу 'Списан'")

    def __str__(self):
        """Возвращает строковое представление полной информации о товаре.

        Returns:
            str: Информация о товаре, включая статус, количество, цену и характеристики.
        """

        return f'''
                Товар: {self.name}, находится находится по адресу {self.location}
                Статус товара: {self.condition}
                Количество товара: {self.quantity}
                Цена товара: {self.cost}
                Поставщик: {self.supplier}
                Производитель: {self.manufacturer}
                Срок годности до: {self.expiry_date}
                Тип товара: {self.category}
                Примечание: {self.note}
                    '''
