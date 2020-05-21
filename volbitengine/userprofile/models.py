from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import reverse


class UserProfile(models.Model):
    """Класс-модель для профилей студентов"""
    id_profile = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    surname = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=50)
    number_school = models.IntegerField(max_length=5)
    date_of_birth = models.DateField(null=True)
    ph_number = models.CharField(max_length=12)
    # email = models.EmailField()
    group = models.ManyToManyField('Group', blank=True, related_name='profiles')

    def get_absolute_url(self):
        return reverse('profile_detail_url', args=[str(self.id_profile)])

    def __str__(self):
        return '%s, %s, %s' % (self.surname, self.name, self.patronymic)


class Group(models.Model):
    id_group = models.AutoField(primary_key=True)
    name_group = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('group_detail_url', args=[str(self.id_group)])

    def __str__(self):
        return '%s' % self.name_group


class CompClass(models.Model):
    id_comp = models.AutoField(primary_key=True)
    name_comp = models.ManyToManyField('Group', blank=True, related_name='compclass')
    # Цена не должна быть целой
    price = models.FloatField()
    beg_hours = models.TimeField()
    end_hours = models.TimeField()

    def get_absolute_url(self):
        return reverse('compclass_detail_url', args=[str(self.id_comp)])

    def __str__(self):
        return '%s' % self.name_comp


class Places(models.Model):
    id_place = models.AutoField(primary_key=True)
    name_place = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    floor = models.IntegerField(max_length=2)
    office = models.CharField(max_length=5)

    def get_absolute_url(self):
        return reverse('places_detail_url', args=[str(self.id_place)])

    def __str__(self):
        return '%s' % self.name_place


class TeacherProfile(models.Model):
    """Класс-модель для профилей преподавателей"""
    id_teacher = models.AutoField(primary_key=True)
    surname = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=50)
    date_of_birth = models.DateField(null=True)
    ph_number = models.CharField(max_length=12)

    def get_absolute_url(self):
        return reverse('teacher_detail_url', args=[str(self.id_teacher)])

    def __str__(self):
        return '%s, %s, %s' % (self.surname, self.name, self.patronymic)
