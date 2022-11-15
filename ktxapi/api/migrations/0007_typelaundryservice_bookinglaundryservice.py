# Generated by Django 4.0.4 on 2022-08-05 13:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_building_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypeLaundryService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=100)),
                ('cost', models.FloatField()),
                ('max_weight', models.IntegerField()),
                ('note', models.TextField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='BookingLaundryService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.typelaundryservice')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
