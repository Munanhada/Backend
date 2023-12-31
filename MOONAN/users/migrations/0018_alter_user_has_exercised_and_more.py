# Generated by Django 4.2.1 on 2023-08-14 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_merge_20230813_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='has_exercised',
            field=models.BooleanField(blank=True, default=False, verbose_name='운동 여부'),
        ),
        migrations.AlterField(
            model_name='user',
            name='has_medication_or_nutrition',
            field=models.BooleanField(blank=True, default=False, verbose_name='약 및 영양제 섭취 여부'),
        ),
    ]
