# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activento', '0004_auto_20151029_2028'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('salutation', models.CharField(max_length=10)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('publication_date', models.DateField()),
                ('authors', models.ManyToManyField(to='activento.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=60)),
                ('state_province', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=50)),
                ('website', models.URLField()),
            ],
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nombre',
            field=models.CharField(max_length=50),
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(to='activento.Publisher'),
        ),
    ]
