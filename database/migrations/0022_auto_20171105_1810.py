# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-05 23:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0021_auto_20171105_1809'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='agar1log',
            table='agar1log',
        ),
        migrations.AlterModelTable(
            name='agar2log',
            table='agar2log',
        ),
        migrations.AlterModelTable(
            name='agar3log',
            table='agar3log',
        ),
        migrations.AlterModelTable(
            name='agar4log',
            table='agar4log',
        ),
        migrations.AlterModelTable(
            name='agar5log',
            table='agar5log',
        ),
        migrations.AlterModelTable(
            name='agar6log',
            table='agar6log',
        ),
        migrations.AlterModelTable(
            name='isolate',
            table='isolate',
        ),
        migrations.AlterModelTable(
            name='plate',
            table='plate',
        ),
        migrations.AlterModelTable(
            name='run',
            table='run',
        ),
        migrations.AlterModelTable(
            name='site',
            table='site',
        ),
        migrations.AlterModelTable(
            name='swabber',
            table='swabber',
        ),
    ]
