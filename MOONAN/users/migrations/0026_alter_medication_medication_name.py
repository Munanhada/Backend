# Generated by Django 4.2.4 on 2023-08-16 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0025_alter_medication_medication_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medication',
            name='medication_name',
            field=models.CharField(choices=[('혈압약', '혈압약'), ('당뇨약', '당뇨약'), ('소화제', '소화제'), ('고지혈증약', '고지혈증약'), ('변비약', '변비약'), ('위장약', '위장약'), ('항생제', '항생제'), ('항히스타민제', '항히스타민제'), ('갑상선질환 치료제', '갑상선질환 치료제'), ('통풍 치료제', '통풍 치료제'), ('소염 진통제', '소염 진통제'), ('우울증약', '우울증약'), ('성호르몬제', '성호르몬제')], max_length=100, unique=True, verbose_name='복용 중인 약'),
        ),
    ]
