# Generated by Django 4.0.1 on 2022-02-13 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Saveuser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentname', models.CharField(max_length=50)),
                ('mno', models.CharField(max_length=50)),
                ('collegename', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('cls', models.CharField(max_length=50)),
            ],
        ),
    ]
