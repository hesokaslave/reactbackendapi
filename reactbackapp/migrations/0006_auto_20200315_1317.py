# Generated by Django 3.0.3 on 2020-03-15 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reactbackapp', '0005_auto_20200315_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='token',
            field=models.CharField(blank=True, default='c23c94f1d615451e86c3ef9e0bae0039', max_length=255, null=True),
        ),
    ]