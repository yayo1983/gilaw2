# Generated by Django 4.1.7 on 2023-02-17 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailnotification',
            name='category',
            field=models.CharField(choices=[('Sports', 'Sports'), ('Finance', 'Finance '), ('Movies', 'Movies')], default='Sports', max_length=70),
        ),
        migrations.AddField(
            model_name='pushnotification',
            name='category',
            field=models.CharField(choices=[('Sports', 'Sports'), ('Finance', 'Finance '), ('Movies', 'Movies')], default='Sports', max_length=70),
        ),
        migrations.AddField(
            model_name='smsnotification',
            name='category',
            field=models.CharField(choices=[('Sports', 'Sports'), ('Finance', 'Finance '), ('Movies', 'Movies')], default='Sports', max_length=70),
        ),
    ]
