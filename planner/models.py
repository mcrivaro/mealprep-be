from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.name


class Unit(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)

    def __str__(self):
        return self.name


class ItemAmount(models.Model):
    item = models.ForeignKey(Item, on_delete=models.PROTECT)
    amount = models.IntegerField()
    unit = models.ForeignKey(Unit, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.amount} {self.unit} {self.item.name}"


class Storage(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    items = models.ManyToManyField(ItemAmount, blank=True)

    def __str__(self):
        return self.name


class StoredItem(models.Model):
    storage = models.ForeignKey(Storage, on_delete=models.PROTECT)
    item_amount = models.ForeignKey(ItemAmount, on_delete=models.PROTECT)
    expiry_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.item_amount} in {self.storage}"


class MealTime(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)

    def __str__(self):
        return self.name


class Meal(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    items = models.ManyToManyField(ItemAmount, blank=True)
    daytime = models.ForeignKey(MealTime, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name


class Plan(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    amount_of_days = models.IntegerField(default=7, blank=False, null=False)
    meal_times = models.ManyToManyField(MealTime)
    meals = models.ManyToManyField(Meal)
    tags = models.ManyToManyField(Tag)

    def generate_custom_plan(self, amount_of_days, meal_times, wished_meals, tags):

        Plan.objects.create()

    def generate_shopping_list(self):
        pass

    def __str__(self):
        return self.name
