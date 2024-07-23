# Generated by Django 5.0.7 on 2024-07-23 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='copies',
            field=models.CharField(choices=[('available', 'Available'), ('borrowed', 'Borrowed'), ('reserved', 'Reserved')], default='available', max_length=200),
        ),
    ]
