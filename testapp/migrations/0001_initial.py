# Generated by Django 4.1.3 on 2022-11-29 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_name', models.CharField(max_length=120)),
                ('stu_age', models.IntegerField()),
                ('stu_city', models.CharField(max_length=120)),
                ('stu_roll_no', models.IntegerField()),
            ],
        ),
    ]
