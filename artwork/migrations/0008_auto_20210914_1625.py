# Generated by Django 3.0.5 on 2021-09-14 10:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artwork', '0007_auto_20210914_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='reviws',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='artwork.Reviws'),
        ),
    ]
