# Generated by Django 3.0.2 on 2020-02-04 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi_app', '0002_auto_20200204_1437'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paradigm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Programmer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('languages', models.ManyToManyField(to='restapi_app.Language')),
            ],
        ),
    ]
