# Generated by Django 4.0.5 on 2022-06-17 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ItemAmount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('expiry_date', models.DateField(blank=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='planner.item')),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MealTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('items', models.ManyToManyField(blank=True, to='planner.itemamount')),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('amount_of_days', models.IntegerField(default=7)),
                ('meal_times', models.ManyToManyField(to='planner.mealtime')),
                ('meals', models.ManyToManyField(to='planner.meal')),
                ('tags', models.ManyToManyField(to='planner.tag')),
            ],
        ),
        migrations.AddField(
            model_name='meal',
            name='daytime',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='planner.mealtime'),
        ),
        migrations.AddField(
            model_name='meal',
            name='items',
            field=models.ManyToManyField(blank=True, to='planner.itemamount'),
        ),
        migrations.AddField(
            model_name='itemamount',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='planner.unit'),
        ),
        migrations.AddField(
            model_name='item',
            name='tags',
            field=models.ManyToManyField(blank=True, to='planner.tag'),
        ),
    ]
