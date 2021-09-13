# Generated by Django 3.0.5 on 2021-09-13 11:09

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('artwork', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='name',
            field=models.TextField(db_column='name', db_tablespace='name'),
        ),
        migrations.AlterField(
            model_name='categories',
            name='slug',
            field=models.SlugField(db_column='slug', db_tablespace='slug'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='author',
            field=models.ForeignKey(db_column='author', db_tablespace='author', on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comments',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, db_column='pub_date', db_tablespace='pub_date'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='reviws',
            field=models.ForeignKey(db_column='review_id', db_tablespace='review_id', on_delete=django.db.models.deletion.CASCADE, related_name='commets', to='artwork.Reviws'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='text',
            field=models.TextField(db_column='text', db_tablespace='text'),
        ),
        migrations.AlterField(
            model_name='genre_title',
            name='genre',
            field=models.ForeignKey(db_column='genre_id', db_tablespace='genre_id', on_delete=django.db.models.deletion.CASCADE, to='artwork.Genres'),
        ),
        migrations.AlterField(
            model_name='genre_title',
            name='title',
            field=models.ForeignKey(db_column='title_id', db_tablespace='title_id', on_delete=django.db.models.deletion.CASCADE, to='artwork.Titles'),
        ),
        migrations.AlterField(
            model_name='genres',
            name='name',
            field=models.TextField(db_column='name', db_tablespace='name'),
        ),
        migrations.AlterField(
            model_name='genres',
            name='slug',
            field=models.SlugField(db_column='slug', db_tablespace='slug', max_length=20),
        ),
        migrations.AlterField(
            model_name='reviws',
            name='author',
            field=models.ForeignKey(db_column='author', db_tablespace='author', on_delete=django.db.models.deletion.CASCADE, related_name='reviws', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='reviws',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, db_column='pub_date', db_tablespace='pub_date'),
        ),
        migrations.AlterField(
            model_name='reviws',
            name='score',
            field=models.IntegerField(db_column='score', db_tablespace='score', validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='reviws',
            name='text',
            field=models.TextField(db_column='text', db_tablespace='text'),
        ),
        migrations.AlterField(
            model_name='reviws',
            name='titles',
            field=models.ForeignKey(db_column='title_id', db_tablespace='title_id', on_delete=django.db.models.deletion.CASCADE, related_name='reviws', to='artwork.Titles'),
        ),
        migrations.AlterField(
            model_name='titles',
            name='category',
            field=models.ForeignKey(db_column='category', db_tablespace='category', on_delete=django.db.models.deletion.CASCADE, to='artwork.Categories'),
        ),
        migrations.AlterField(
            model_name='titles',
            name='name',
            field=models.TextField(db_column='name', db_tablespace='name'),
        ),
        migrations.AlterField(
            model_name='titles',
            name='year',
            field=models.PositiveIntegerField(db_column='year', db_tablespace='year'),
        ),
    ]
