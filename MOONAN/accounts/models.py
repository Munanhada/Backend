from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
Medication = get_user_model()
Nutrition = get_user_model()

class Child(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='child_user', null=True)
    parents = models.ManyToManyField('Parent', related_name='child_parents')
    medications = models.ManyToManyField(Medication, blank=True, related_name='children_medications', through='ChildMedication')
    nutritions = models.ManyToManyField(Nutrition, blank=True, related_name='children_nutritions', through='ChildNutrition')

    def __str__(self):
        return self.user.name

class ChildMedication(models.Model):
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    medication = models.ForeignKey(Medication, on_delete=models.CASCADE)

class ChildNutrition(models.Model):
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    nutrition = models.ForeignKey(Nutrition, on_delete=models.CASCADE)

class Parent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='parent_user', null=True)
    children = models.ManyToManyField('Child', related_name='parent_children')
    medications = models.ManyToManyField(Medication, blank=True, related_name='parents_medications', through='ParentMedication')
    nutritions = models.ManyToManyField(Nutrition, blank=True, related_name='parents_nutritions', through='ParentNutrition')

    def __str__(self):
        return self.user.name

class ParentMedication(models.Model):
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
    medication = models.ForeignKey(Medication, on_delete=models.CASCADE)

class ParentNutrition(models.Model):
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
    nutrition = models.ForeignKey(Nutrition, on_delete=models.CASCADE)
