# Generated by Django 4.2.4 on 2023-08-08 21:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_connectionrequest'),
        ('accounts', '0003_alter_child_parents_alter_parent_children'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='medications',
            field=models.ManyToManyField(blank=True, related_name='children_medications', through='accounts.ChildMedication', to='users.medication'),
        ),
        migrations.AlterField(
            model_name='child',
            name='nutritions',
            field=models.ManyToManyField(blank=True, related_name='children_nutritions', through='accounts.ChildNutrition', to='users.nutrition'),
        ),
        migrations.AlterField(
            model_name='childmedication',
            name='medication',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.medication'),
        ),
        migrations.AlterField(
            model_name='childnutrition',
            name='nutrition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.nutrition'),
        ),
        migrations.AlterField(
            model_name='parent',
            name='medications',
            field=models.ManyToManyField(blank=True, related_name='parents_medications', through='accounts.ParentMedication', to='users.medication'),
        ),
        migrations.AlterField(
            model_name='parent',
            name='nutritions',
            field=models.ManyToManyField(blank=True, related_name='parents_nutritions', through='accounts.ParentNutrition', to='users.nutrition'),
        ),
        migrations.AlterField(
            model_name='parentmedication',
            name='medication',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.medication'),
        ),
        migrations.AlterField(
            model_name='parentnutrition',
            name='nutrition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.nutrition'),
        ),
    ]