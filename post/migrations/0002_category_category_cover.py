# Generated by Django 2.2.3 on 2019-08-11 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_cover',
            field=models.CharField(default='/home/kabir/.face', max_length=60),
            preserve_default=False,
        ),
    ]