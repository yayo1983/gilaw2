# Generated by Django 4.1.7 on 2023-02-18 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.IntegerField(blank=True, max_length=12, null=True, verbose_name='Phone'),
        ),
    ]
