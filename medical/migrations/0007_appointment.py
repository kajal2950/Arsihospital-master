# Generated by Django 3.2.5 on 2022-01-15 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medical', '0006_alter_post_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254, unique=True)),
                ('phone', models.CharField(max_length=200)),
                ('department', models.CharField(max_length=200)),
                ('doctor_name', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('msg', models.CharField(max_length=500)),
            ],
        ),
    ]