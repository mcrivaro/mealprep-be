from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class ItemSerializer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(
        slug_field="name", many=True, queryset=Tag.objects.all()
    )

    class Meta:
        model = Item
        fields = "__all__"


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = "__all__"


class ItemAmountSerializer(serializers.ModelSerializer):
    item = serializers.SlugRelatedField(slug_field="name", queryset=Item.objects.all())
    unit = serializers.SlugRelatedField(slug_field="name", queryset=Unit.objects.all())

    class Meta:
        model = ItemAmount
        fields = "__all__"


class StorageSerializer(serializers.ModelSerializer):
    items = ItemAmountSerializer(many=True)

    class Meta:
        model = Storage
        fields = "__all__"


class StoredItemSerializer(serializers.ModelSerializer):
    storage = serializers.SlugRelatedField(
        slug_field="name", queryset=Storage.objects.all()
    )
    item_amount = ItemAmountSerializer()

    def create(self, validated_data):
        storage = validated_data.pop("storage")
        try:
            Storage.objects.get(storage)
        except Storage.DoesNotExist:
            Storage.object.create(storage)
        Storage.objects.create(storage)
        expiry_date = validated_data.pop("expiry_date")
        item_amount = ItemAmount.objects.create(**validated_data.pop("item_amount"))
        new_data = {
            "storage": storage,
            "item_amount": item_amount,
            "expiry_date": expiry_date,
        }
        stored_item = StoredItem.objects.create(**new_data)
        return stored_item

    class Meta:
        model = StoredItem
        fields = "__all__"


class MealTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealTime
        fields = "__all__"


class MealSerializer(serializers.ModelSerializer):
    daytime = serializers.SlugRelatedField(
        slug_field="name", queryset=MealTime.objects.all()
    )
    tags = serializers.SlugRelatedField(
        slug_field="name", many=True, queryset=Tag.objects.all()
    )
    items = ItemAmountSerializer(many=True)

    class Meta:
        model = Meal
        fields = "__all__"


class PlanSerializer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(
        slug_field="name", many=True, queryset=Tag.objects.all()
    )

    class Meta:
        model = Plan
        fields = "__all__"
