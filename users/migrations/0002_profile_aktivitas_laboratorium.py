# Generated by Django 3.0.5 on 2020-05-07 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='aktivitas_laboratorium',
            field=models.CharField(blank=True, choices=[('Penelitian', 'Penelitian'), ('Diagnostik', 'Diagnostik'), ('Produksi Bahan Biologis', 'Produksi Bahan Biologis'), ('Lainnya', 'Lainnya')], max_length=50, null=True),
        ),
    ]
