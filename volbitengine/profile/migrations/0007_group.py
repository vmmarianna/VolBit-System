# Generated by Django 3.0.5 on 2020-04-11 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0006_auto_20200411_1832'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id_group', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
