from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from .serializers import *
from .models import *


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class UnitViewSet(viewsets.ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer


class ItemAmountViewSet(viewsets.ModelViewSet):
    queryset = ItemAmount.objects.all()
    serializer_class = ItemAmountSerializer


class StorageViewSet(viewsets.ModelViewSet):
    queryset = Storage.objects.all()
    serializer_class = StorageSerializer


class StoredItemViewSet(viewsets.ModelViewSet):
    queryset = StoredItem.objects.all()
    serializer_class = StoredItemSerializer


class MealTimeViewSet(viewsets.ModelViewSet):
    queryset = MealTime.objects.all()
    serializer_class = MealTimeSerializer


class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer


class PlanViewSet(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
