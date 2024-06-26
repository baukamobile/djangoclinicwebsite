# Generated by Django 4.2 on 2024-04-16 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_post', models.DateTimeField(auto_created=True)),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField(max_length=1500)),
                ('photo', models.ImageField(upload_to='static/%Y/%M/%d/')),
            ],
        ),
        migrations.CreateModel(
            name='UserAuth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
