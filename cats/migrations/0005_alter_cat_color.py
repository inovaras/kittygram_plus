# Generated by Django 3.2 on 2023-04-21 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0004_cat_achievements'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='color',
            field=models.CharField(choices=[('Gray', 'Серый'), ('Black', 'Чёрный'), ('White', 'Белый'), ('Ginger', 'Рыжий'), ('Mixed', 'Смешанный')], max_length=16),
        ),
    ]
