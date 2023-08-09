# Generated by Django 4.2.4 on 2023-08-10 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_medication_user_input_name_nutrition_user_input_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nutrition',
            name='nutrition_name',
            field=models.CharField(choices=[('probiotics', '유산균'), ('omega3', '오메가3'), ('lutein', '루테인'), ('multivitamin', '종합비타민'), ('vitaminC', '비타민C'), ('vitaminD', '비타민D'), ('vitaminA', '비타민A'), ('collagen', '콜라겐'), ('iron', '철분'), ('propolis', '프로폴리스'), ('aronia', '아로니아'), ('folic_acid', '엽산'), ('magnesium', '마그네슘'), ('vitaminE', '비타민E'), ('calcium', '칼슘')], max_length=100, verbose_name='복용 중인 영양제'),
        ),
    ]
