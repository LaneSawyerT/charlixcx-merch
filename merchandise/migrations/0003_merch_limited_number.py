# Generated by Django 3.2 on 2022-03-23 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merchandise', '0002_auto_20220322_2226'),
    ]

    operations = [
        migrations.AddField(
            model_name='merch',
            name='limited_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
