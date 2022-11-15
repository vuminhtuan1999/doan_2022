# Generated by Django 4.0.4 on 2022-08-14 08:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_notification'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('bod', models.DateField()),
                ('gender', models.CharField(max_length=10)),
                ('folk', models.CharField(max_length=100)),
                ('dtut', models.CharField(max_length=100)),
                ('religion', models.CharField(max_length=255)),
                ('type_study', models.CharField(max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
