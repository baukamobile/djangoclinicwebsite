# Generated by Django 4.2.7 on 2024-04-16 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyCrud', '0003_rename_searitem_searchitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='photo',
            field=models.ImageField(upload_to='static/'),
        ),
    ]
