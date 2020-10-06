# Generated by Django 3.0.6 on 2020-07-30 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0030_auto_20200730_1211'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionnaire',
            name='keterangan_identifikasi_hazard',
            field=models.TextField(default='Isi Laporan'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='keterangan_inventarisasi_informasi_dan_pencatatan',
            field=models.TextField(default='Isi Laporan'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='keterangan_pengendalian_dan_monitoring',
            field=models.TextField(default='Isi Laporan'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='keterangan_pengendalian_risiko',
            field=models.TextField(default='Isi Laporan'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='keterangan_penyimpanan_bahan_biologik_dan_bahan_berbahaya_lainnya',
            field=models.TextField(default='Isi Laporan'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='keterangan_peran_dan_tanggung_jawab',
            field=models.TextField(default='Isi Laporan'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='keterangan_proses_metode_dan_prosedur',
            field=models.TextField(default='Isi Laporan'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='keterangan_ruang_lingkup_dan_penjadwalan',
            field=models.TextField(default='Isi Laporan'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='keterangan_transfer_bahan_biologik_dan_bahan_berbahaya_lainnya',
            field=models.TextField(default='Isi Laporan'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='nilai_no_14',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='nilai_no_15',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='nilai_no_16',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='nilai_no_17',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='nilai_no_18',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='nilai_no_19',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='nilai_no_20',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='nilai_no_21',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='nilai_no_22',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='rekomendasi_identifikasi_hazard',
            field=models.TextField(default='Isi Laporan'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='rekomendasi_inventarisasi_informasi_dan_pencatatan',
            field=models.TextField(default='Isi Laporan'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='rekomendasi_pengendalian_dan_monitoring',
            field=models.TextField(default='Isi Laporan'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='rekomendasi_pengendalian_risiko',
            field=models.TextField(default='Isi Laporan'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='rekomendasi_penyimpanan_bahan_biologik_dan_bahan_berbahaya_lainnya',
            field=models.TextField(default='Isi Laporan'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='rekomendasi_peran_dan_tanggung_jawab',
            field=models.TextField(default='Isi Laporan'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='rekomendasi_proses_metode_dan_prosedur',
            field=models.TextField(default='Isi Laporan'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='rekomendasi_ruang_lingkup_dan_penjadwalan',
            field=models.TextField(default='Isi Laporan'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='rekomendasi_transfer_bahan_biologik_dan_bahan_berbahaya_lainnya',
            field=models.TextField(default='Isi Laporan'),
        ),
    ]
