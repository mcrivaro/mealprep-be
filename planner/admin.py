from django.contrib import admin
from .models import (
    Tag,
    Item,
    ItemAmount,
    Storage,
    Meal,
    Plan,
    Unit,
    MealTime,
    StoredItem,
)

# Register your models here.

admin.site.register(Tag)
admin.site.register(Item)
admin.site.register(ItemAmount)
admin.site.register(Storage)
admin.site.register(Meal)
admin.site.register(Plan)
admin.site.register(Unit)
admin.site.register(MealTime)
admin.site.register(StoredItem)
