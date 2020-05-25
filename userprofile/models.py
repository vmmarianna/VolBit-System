from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import reverse


class UserProfile(models.Model):
    """Класс-модель для профилей студентов"""
    id_profile = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    surname = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    sex = models.CharField(max_length=10)
    patronymic = models.CharField(max_length=50)
    number_school = models.IntegerField(null=True)
    date_of_birth = models.DateField(null=True)
    ph_number = models.CharField(max_length=12)
    # email = models.EmailField()
    group = models.ManyToManyField('Group', null=True, related_name='profiles')

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


class TeacherProfile(models.Model):
    """Класс-модель для профилей преподавателей"""
    id_teacher = models.AutoField(primary_key=True)
    surname = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=50)
    sex = models.CharField(max_length=10)
    date_of_birth = models.DateField(null=True)
    ph_number = models.CharField(max_length=12)

    def get_absolute_url(self):
        return reverse('teacher_detail_url', args=[str(self.id_teacher)])

    def __str__(self):
        return '%s, %s, %s' % (self.surname, self.name, self.patronymic)


class CompClass(models.Model):
    id_comp = models.AutoField(primary_key=True)
    name_comp = models.ManyToManyField('Group', blank=True, related_name='compclass')
    # Цена не должна быть целой
    weekday = models.CharField(max_length=15)
    price = models.FloatField()
    long = models.FloatField(max_length=5)
    beg_hours = models.TimeField()
    end_hours = models.TimeField()
    name_teacher = models.OneToOneField('TeacherProfile', blank=True, related_name='teacher',
                                        on_delete=models.CASCADE, )

    def get_absolute_url(self):
        return reverse('compclass_detail_url', args=[str(self.id_comp)])

    def __str__(self):
        return '%s' % self.name_comp


class Place(models.Model):
    id_place = models.AutoField(primary_key=True)
    name_place = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    floor = models.IntegerField()
    office = models.CharField(max_length=5)

    def get_absolute_url(self):
        return reverse('places_detail_url', args=[str(self.id_place)])

    def __str__(self):
        return '%s' % self.name_place


class Lesson(models.Model):
    id_lesson = models.AutoField(primary_key=True)
    pay = models.BooleanField(null=True)
    date_start = models.DateField(auto_now=False, auto_now_add=False, )
    date_end = models.DateField(null=True, auto_now=False, auto_now_add=False, )
    name_place = models.OneToOneField('Place', blank=True, related_name='places', on_delete=models.CASCADE, )
    name_teacher = models.ManyToManyField('TeacherProfile', blank=True, related_name='teacherprofile')
    name_group = models.OneToOneField('Group', blank=True, related_name='group', on_delete=models.CASCADE, )
    students = models.ManyToManyField('UserProfile', blank=True, related_name='students', )

    def get_absolute_url(self):
        return reverse('lessons_detail_url', args=[str(self.id_lesson)])

    def __str__(self):
        return '%s - %s - %s' % (self.name_group, self.name_place, self.date_start)


class Statement(models.Model):
    id_statement = models.AutoField(primary_key=True)
    pay_statement = models.FloatField(null=True)
    data_statement = models.DateField(null=True, auto_now=False, auto_now_add=False, )
    name_group = models.OneToOneField('Group', blank=True, related_name='group_statements', on_delete=models.CASCADE, )
    students = models.ManyToManyField('UserProfile', blank=True, related_name='students_statements', )

    def get_absolute_url(self):
        return reverse('statement_detail_url', args=[str(self.id_statement)])

    def __str__(self):
        return '%s - %s - %s' % (self.name_group, self.data_statement, self.students)
