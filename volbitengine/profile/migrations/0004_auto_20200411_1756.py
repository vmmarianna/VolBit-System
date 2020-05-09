# Generated by Django 3.0.5 on 2020-04-11 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0003_auto_20200411_1751'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='last_name',
            new_name='surname',
        ),
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(default=-1, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='patronymic',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='ph_number',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
    ]
