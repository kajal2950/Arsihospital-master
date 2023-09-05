# Generated by Django 3.2.5 on 2022-01-17 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medical', '0008_alter_appointment_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carrier', models.CharField(max_length=200)),
                ('name', models.CharField(default='', max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('gender', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('exp', models.IntegerField()),
                ('resume', models.FileField(default=None, max_length=250, null=True, upload_to='news')),
                ('education', models.CharField(max_length=250)),
                ('skill', models.CharField(max_length=250)),
            ],
        ),
    ]
