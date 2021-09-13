# Generated by Django 3.0.5 on 2021-09-13 12:01

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('artwork', '0004_auto_20210913_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='name',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='categories',
            name='slug',
            field=models.SlugField(),
        ),
        migrations.AlterField(
            model_name='comments',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comments',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='comments',
            name='reviws',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commets', to='artwork.Reviws'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='text',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='genre_title',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artwork.Genres'),
        ),
        migrations.AlterField(
            model_name='genre_title',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artwork.Titles'),
        ),
        migrations.AlterField(
            model_name='genres',
            name='name',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='genres',
            name='slug',
            field=models.SlugField(max_length=20),
        ),
        migrations.AlterField(
            model_name='reviws',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviws', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='reviws',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='reviws',
            name='score',
            field=models.IntegerField(db_column='score', validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='reviws',
            name='titles',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviws', to='artwork.Titles'),
        ),
        migrations.AlterField(
            model_name='titles',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artwork.Categories'),
        ),
        migrations.AlterField(
            model_name='titles',
            name='name',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='titles',
            name='year',
            field=models.PositiveIntegerField(),
        ),
    ]
