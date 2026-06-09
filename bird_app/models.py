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