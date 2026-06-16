from django.conf import settings
from django.db import models

MAX_LENGTH = 255


class Category(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Наименование')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Collection(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Наименование')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Коллекция'
        verbose_name_plural = 'Коллекции'


class Supplier(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Наименование')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    phone = models.CharField(max_length=20, verbose_name='Телефон')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'


class Manufacturer(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Наименование')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'


class Accessory(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Наименование')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.FloatField(verbose_name='Цена')
    size = models.CharField(max_length=50, verbose_name='Размер')
    color = models.CharField(max_length=MAX_LENGTH, verbose_name='Цвет')
    photo = models.ImageField(upload_to='Image/%Y/%m/%d', null=True, blank=True, verbose_name='Изображение')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления на сайт')
    is_exists = models.BooleanField(default=True, verbose_name='Доступность к заказу')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория')
    collection = models.ManyToManyField(Collection, verbose_name='Коллекция')

    def __str__(self):
        return f"{self.name} ({self.price} руб.)"

    class Meta:
        verbose_name = 'Аксессуар'
        verbose_name_plural = 'Аксессуары'


class Bird(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Наименование')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.FloatField(verbose_name='Цена')
    age = models.PositiveIntegerField(verbose_name='Возраст (мес.)')
    color = models.CharField(max_length=MAX_LENGTH, verbose_name='Окрас')
    photo = models.ImageField(upload_to='Image/%Y/%m/%d', null=True, blank=True, verbose_name='Изображение')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления на сайт')
    is_exists = models.BooleanField(default=True, verbose_name='Доступность к заказу')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория')
    collection = models.ManyToManyField(Collection, verbose_name='Коллекция')

    def __str__(self):
        return f"{self.name} ({self.price} руб.)"

    class Meta:
        verbose_name = 'Птица'
        verbose_name_plural = 'Птицы'


class Cage(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Наименование')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.FloatField(verbose_name='Цена')
    size = models.CharField(max_length=50, verbose_name='Размер')
    material = models.CharField(max_length=MAX_LENGTH, verbose_name='Материал')
    photo = models.ImageField(upload_to='Image/%Y/%m/%d', null=True, blank=True, verbose_name='Изображение')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления на сайт')
    is_exists = models.BooleanField(default=True, verbose_name='Доступность к заказу')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория')
    collection = models.ManyToManyField(Collection, verbose_name='Коллекция')

    def __str__(self):
        return f"{self.name} ({self.price} руб.)"

    class Meta:
        verbose_name = 'Клетка'
        verbose_name_plural = 'Клетки'


class Feed(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Наименование')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.FloatField(verbose_name='Цена')
    weight = models.FloatField(verbose_name='Вес (кг)')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления на сайт')
    is_exists = models.BooleanField(default=True, verbose_name='Доступность к заказу')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория')
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.PROTECT, verbose_name='Производитель')
    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.PROTECT,
        verbose_name='Поставщик',
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.name} ({self.price} руб.)"

    class Meta:
        verbose_name = 'Корм'
        verbose_name_plural = 'Корма'


class Order(models.Model):
    SHOP = "SH"
    COURIER = "CR"
    PICKUPPOINT = "PP"
    TYPE_DELIVERY = [
        (SHOP, 'Вывоз из магазина'),
        (COURIER, 'Курьер'),
        (PICKUPPOINT, 'Пункт выдачи заказов'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        verbose_name='Пользователь',
        related_name='orders',
    )
    buyer_firstname = models.CharField(max_length=MAX_LENGTH, verbose_name='Фамилия покупателя')
    buyer_name = models.CharField(max_length=MAX_LENGTH, verbose_name='Имя покупателя')
    buyer_surname = models.CharField(max_length=MAX_LENGTH, blank=True, null=True, verbose_name='Отчество покупателя')
    comment = models.CharField(max_length=MAX_LENGTH, blank=True, null=True, verbose_name='Комментарий к заказу')
    delivery_address = models.CharField(max_length=MAX_LENGTH, verbose_name='Адрес доставки')
    delivery_type = models.CharField(max_length=2, choices=TYPE_DELIVERY, default=SHOP, verbose_name='Способ доставки')
    price = models.FloatField(default=0, verbose_name='Сумма заказа')
    date_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания заказа')
    date_finish = models.DateTimeField(null=True, blank=True, verbose_name='Дата завершения заказа')
    accessory = models.ManyToManyField('Accessory', through='Pos_order', verbose_name='Товар', blank=True)

    def __str__(self):
        return f'#{self.pk} - {self.buyer_firstname} {self.buyer_name} ({self.date_create})'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class Pos_order(models.Model):
    accessory = models.ForeignKey(
        Accessory,
        on_delete=models.PROTECT,
        verbose_name='Аксессуар',
        null=True,
        blank=True
    )
    bird = models.ForeignKey(
        Bird,
        on_delete=models.PROTECT,
        verbose_name='Птица',
        null=True,
        blank=True
    )
    cage = models.ForeignKey(
        Cage,
        on_delete=models.PROTECT,
        verbose_name='Клетка',
        null=True,
        blank=True
    )
    order = models.ForeignKey(Order, on_delete=models.PROTECT, verbose_name='Заказ')
    count = models.PositiveIntegerField(default=1, verbose_name='Количество продукта')
    discount = models.PositiveIntegerField(default=0, verbose_name='Скидка на позицию')

    def get_product(self):
        return self.accessory or self.bird or self.cage

    def __str__(self):
        product = self.get_product()
        product_name = product.name if product else 'Без товара'
        return f'{self.order.pk} {product_name} ({self.order.buyer_firstname} {self.order.buyer_name})'

    class Meta:
        verbose_name = 'Позиция заказа'
        verbose_name_plural = 'Позиции заказов'