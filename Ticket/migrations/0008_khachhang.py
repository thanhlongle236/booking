# Generated by Django 2.2.5 on 2019-11-06 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ticket', '0007_hangxe_lichtrinh_loaixe_tuyen_xe'),
    ]

    operations = [
        migrations.CreateModel(
            name='KhachHang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TenKhachHang', models.CharField(default='', max_length=100)),
                ('DienThoai', models.CharField(default='', max_length=10)),
                ('Email', models.CharField(default='', max_length=100)),
                ('DiemDon', models.CharField(default='', max_length=100)),
                ('GhiChu', models.TextField(default='', max_length=100)),
            ],
        ),
    ]
