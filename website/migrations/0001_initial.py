# Generated by Django 4.2 on 2023-04-29 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=50, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=50, verbose_name='Last Name')),
                ('email', models.CharField(max_length=50, verbose_name='Email Address')),
                ('phone', models.CharField(max_length=14, verbose_name='Phone Number')),
                ('state', models.CharField(max_length=50, verbose_name='State')),
                ('city', models.CharField(max_length=50, verbose_name='City')),
                ('address', models.CharField(max_length=50, verbose_name='Address')),
                ('zip_code', models.CharField(max_length=50, verbose_name='Zip-Code')),
            ],
        ),
    ]
