# Generated by Django 3.0.3 on 2020-03-18 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reactbackapp', '0016_auto_20200316_0122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='token',
            field=models.CharField(blank=True, default='a53e098459684691b698bc707f807851', max_length=255, null=True),
        ),
    ]
