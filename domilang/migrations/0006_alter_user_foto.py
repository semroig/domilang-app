# Generated by Django 3.2 on 2021-05-21 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domilang', '0005_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='foto',
            field=models.CharField(default='none', max_length=255),
        ),
    ]