# Generated by Django 3.0.6 on 2020-07-29 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0027_auto_20200729_2312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionnaire',
            name='nilai_no_1',
            field=models.IntegerField(),
        ),
    ]
