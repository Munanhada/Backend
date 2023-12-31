# Generated by Django 4.2.4 on 2023-08-13 23:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expression', models.CharField(choices=[('best', '최고예요'), ('okay', '무난해요'), ('soso', '그럭저럭'), ('notgood', '안좋아요'), ('bad', '나빠요')], max_length=20, null=True, verbose_name='표정')),
                ('eating', models.CharField(blank=True, choices=[('입맛이 없었어.. 시원한게 먹고 싶구나', 1), ('소화가 잘 안되네..', 2), ('맛이 없었어..', 3), ('이가 아파서 먹기 힘들었어..', 4), ('더부룩하고 체기가 있었어..', 5), ('먹고싶은 음식이 아니었어..', 6)], max_length=100, null=True, verbose_name='식사')),
                ('health', models.CharField(blank=True, choices=[('무릎이 아프네..', 1), ('비가 오려나 몸이 쑤시네..', 2), ('머리가 아프네..', 3), ('허리가 아프네..', 4), ('가슴이 답답하네..', 5), ('감기기운이 있나봐..', 6)], max_length=100, null=True, verbose_name='건강')),
                ('sleep', models.CharField(blank=True, choices=[('밤새악목을 꿨어', 1), ('잠이 안와서 뒤척였어..', 2), ('자꾸 깼어ㅠㅠ', 3), ('화장실을 자주 갔어..', 4), ('자는데 소음때문에 힘들었어', 5)], max_length=100, null=True, verbose_name='수면')),
                ('mood', models.CharField(blank=True, choices=[('오늘은 좀 울적하네..', 1), ('오늘은 좀 꿀꿀해', 2), ('오늘 좀 심심했어', 3), ('오늘 답답한 일이 있었어..', 4), ('화가나는 일이 있었어!', 5), ('짜증나는 일이 있었어!', 6)], max_length=100, null=True, verbose_name='기분')),
                ('accident', models.CharField(blank=True, choices=[('부딪혀서 멍이 들었어', 1), ('요리하다 살짝 데였어', 2), ('요리하다 살짝 베었어', 3), ('발에 걸려서 넘어졌어', 4), ('교통사고 났어', 5)], max_length=100, null=True, verbose_name='사고')),
                ('customContent', models.TextField(blank=True, null=True)),
                ('created_date', models.DateField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
