# Generated by Django 3.0.2 on 2020-04-08 18:43

from django.db import migrations, models
import items.models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0008_auto_20200407_2155'),
    ]

    operations = [
        migrations.RenameField(
            model_name='itemcategories',
            old_name='item_id',
            new_name='item',
        ),
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=items.models.user_directory_path),
        ),
    ]
