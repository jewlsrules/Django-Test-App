# Generated by Django 3.0.1 on 2019-12-20 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20191220_2051'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='last_name',
            field=models.CharField(default='', max_length=72),
            preserve_default=False,
        ),
    ]
