# Generated by Django 3.2 on 2021-05-15 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domilang', '0003_auto_20210514_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='foto',
            field=models.CharField(default='none', max_length=24),
        ),
        migrations.AlterField(
            model_name='user',
            name='franja',
            field=models.CharField(default='none', max_length=24),
        ),
        migrations.AlterField(
            model_name='user',
            name='native_lan',
            field=models.CharField(default='none', max_length=24),
        ),
        migrations.AlterField(
            model_name='user',
            name='nivel',
            field=models.CharField(default='none', max_length=24),
        ),
        migrations.AlterField(
            model_name='user',
            name='pais',
            field=models.CharField(default='none', max_length=24),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(default='none', max_length=24),
        ),
        migrations.AlterField(
            model_name='user',
            name='study_lan',
            field=models.CharField(default='none', max_length=24),
        ),
    ]