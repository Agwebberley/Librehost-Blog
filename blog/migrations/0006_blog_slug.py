# Generated by Django 4.1.1 on 2022-09-26 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_blog_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='slug',
            field=models.SlugField(default='djangodbmodelsfieldscharfield'),
        ),
    ]
