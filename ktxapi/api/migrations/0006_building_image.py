# Generated by Django 4.0.4 on 2022-08-03 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_reflect'),
    ]

    operations = [
        migrations.AddField(
            model_name='building',
            name='image',
            field=models.ImageField(null=True, upload_to='uploads/building/%Y/%m'),
        ),
    ]