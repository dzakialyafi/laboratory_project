# Generated by Django 3.0.7 on 2020-08-30 03:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0037_auto_20200820_0327'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionnaire',
            name='date_updated',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='judul_laporan',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
