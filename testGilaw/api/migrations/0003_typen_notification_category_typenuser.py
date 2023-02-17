# Generated by Django 4.1.7 on 2023-02-17 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_emailnotification_category_pushnotification_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypeN',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('SMS', 'SMS'), ('Email', 'Email '), ('Push Notification', 'Push Notification')], default='SMS', max_length=70)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'type_notification',
            },
        ),
        migrations.AddField(
            model_name='notification',
            name='category',
            field=models.CharField(choices=[('Sports', 'Sports'), ('Finance', 'Finance '), ('Movies', 'Movies')], default='Sports', max_length=70),
        ),
        migrations.CreateModel(
            name='TypeNUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usernotification', to='api.typen')),
                ('usern', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='type', to='api.usernotification')),
            ],
        ),
    ]