# Generated by Django 4.2.4 on 2023-08-07 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medication',
            name='medication_name',
            field=models.CharField(choices=[('blood_pressure', '혈압약'), ('diabetes', '당뇨약'), ('digestive', '소화제'), ('cholesterol', '고지혈증약'), ('constipation', '변비약'), ('digestive_system', '위장약'), ('antibiotics', '항생제'), ('antihistamines', '항히스타민제'), ('thyroid_disorder', '갑상선질환 치료제'), ('gout_treatment', '통풍 치료제'), ('anti-inflammatory', '소염 진통제'), ('antidepressants', '우울증약'), ('hormone_therapy', '성호르몬제'), ('add', '직접 입력')], max_length=100, verbose_name='복용 중인 약'),
        ),
        migrations.AlterField(
            model_name='nutrition',
            name='nutrition_name',
            field=models.CharField(choices=[('probiotics', '유산균'), ('omega3', '오메가3'), ('lutein', '루테인'), ('multivitamin', '종합비타민'), ('vitaminC', '비타민C'), ('vitaminD', '비타민D'), ('vitaminA', '비타민A'), ('collagen', '콜라겐'), ('iron', '철분'), ('propolis', '프로폴리스'), ('aronia', '아로니아'), ('folic_acid', '엽산'), ('magnesium', '마그네슘'), ('vitaminE', '비타민E'), ('calcium', '칼슘'), ('add', '직접 입력')], max_length=100, verbose_name='복용 중인 영양제'),
        ),
    ]
