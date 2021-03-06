# Generated by Django 3.0.3 on 2020-03-15 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reactbackapp', '0007_auto_20200315_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='upload/users'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='token',
            field=models.CharField(blank=True, default='f9cd91a502ed4650882e6016a7af1ac7', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='upload/products'),
        ),
    ]
