# Generated by Django 3.0.2 on 2020-01-24 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0003_auto_20200124_0028'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='people',
            name='color',
        ),
        migrations.AddField(
            model_name='people',
            name='favorite_color',
            field=models.CharField(choices=[('green', 'GREEN'), ('blue', 'BLUE'), ('red', 'RED'), ('orange', 'ORANGE'), ('black', 'BLACK'), ('purple', 'PURPLE'), ('yellow', 'YELLOW'), ('pink', 'PINK'), ('brown', 'BROWN'), ('white', 'WHITE')], default='green', max_length=6),
        ),
    ]
