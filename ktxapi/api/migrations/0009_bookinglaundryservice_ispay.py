# Generated by Django 4.0.4 on 2022-08-05 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookinglaundryservice',
            name='isPay',
            field=models.BooleanField(default=False),
        ),
    ]
