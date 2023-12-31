# Generated by Django 4.2.2 on 2023-08-17 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0026_alter_medication_medication_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connectionrequest',
            name='relationship1',
            field=models.CharField(blank=True, choices=[('엄마', '엄마'), ('아빠', '아빠'), ('할머니', '할머니'), ('할아버지', '할아버지'), ('딸', '딸'), ('아들', '아들'), ('손자', '손자'), ('손녀', '손녀')], max_length=100, null=True, verbose_name='관계1'),
        ),
        migrations.AlterField(
            model_name='connectionrequest',
            name='relationship2',
            field=models.CharField(blank=True, choices=[('엄마', '엄마'), ('아빠', '아빠'), ('할머니', '할머니'), ('할아버지', '할아버지'), ('딸', '딸'), ('아들', '아들'), ('손자', '손자'), ('손녀', '손녀')], max_length=100, null=True, verbose_name='관계2'),
        ),
    ]
