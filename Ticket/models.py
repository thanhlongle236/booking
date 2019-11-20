from django.db import models

# Create your models here.
class HangXe(models.Model):
    TenHangXe = models.CharField(max_length=100, default='')
    AnhHangXe = models.ImageField(default='')
    DienThoai = models.CharField(max_length=10, default='')
    TinhTrang = models.BooleanField(default=True)
    MoTa = models.TextField(max_length=100, default='', null=True)
    NgayThem = models.DateField(auto_now=True)
    def __str__(self):
        return self.TenHangXe

class LoaiXe(models.Model):
    TenLoaiXe = models.CharField(max_length=100, default='')
    SoLuongGhe = models.SmallIntegerField(default='')
    TinhTrang = models.BooleanField(default=True)
    MoTa = models.TextField(max_length=100, default='', null=True)
    NgayThem = models.DateField(auto_now=True)
    def __str__(self):
        return self.TenLoaiXe


class LichTrinh(models.Model):
    # IDXe = models.ForeignKey(Xe, on_delete=models.CASCADE)
    TenLichTrinh = models.CharField(max_length=100, default='')
    DiemDi = models.CharField(max_length=100, default='')
    DiemDen = models.CharField(max_length=100, default='')
    ThoiGian = models.FloatField(default='')
    GioDi = models.TimeField(default='')
    NgayDi = models.DateField(default='')
    TinhTrang = models.BooleanField(default=True)
    MoTa = models.TextField(max_length=100, default='', null=True)
    NgayThem = models.DateField(auto_now=True)
    def __str__(self):
        return self.TenLichTrinh

class Xe(models.Model):
    IDLichTrinh = models.ForeignKey(LichTrinh, on_delete=models.CASCADE)
    IDHangXe = models.ForeignKey(HangXe, on_delete=models.CASCADE)
    IDLoaiXe = models.ForeignKey(LoaiXe, on_delete=models.CASCADE)
    TenXe = models.CharField(max_length=100, default='') 
    TinhTrang = models.BooleanField(default=True)
    MoTa = models.TextField(max_length=100, default='', null=True)
    NgayThem = models.DateField(auto_now=True)
    def __str__(self):
        return self.TenXe

# class Ghe(models.Model):
#     IDLichTrinh = models.ForeignKey(LichTrinh, on_delete=models.CASCADE)
#     SoGhe = models.SmallIntegerField(default='')
#     TinhTrang = models.BooleanField(default=True)
#     MoTa = models.TextField(max_length=100, default='', null=True)
#     NgayThem = models.DateField(auto_now=True)
#     def __str__(self):
#         return self.MoTa
class Ghe(models.Model):
    IDXe = models.ForeignKey(Xe, on_delete=models.CASCADE)
    SoGhe = models.SmallIntegerField(default='')
    TinhTrang = models.BooleanField(default=True)
    MoTa = models.TextField(max_length=100, default='', null=True)
    NgayThem = models.DateField(auto_now=True)
    def __str__(self):
        return self.MoTa

class KhachHang(models.Model):
    TenKhachHang = models.CharField(max_length=100, default='')
    DienThoai = models.CharField(max_length=10, default='')
    Email = models.CharField(max_length=100, default='')
    DiemDon = models.CharField(max_length=100, default='')
    GhiChu = models.TextField(max_length=100, default='')
    def __str____(self):
        return self.TenKhachHang

class GiaVe(models.Model):
    IDLichTrinh = models.ForeignKey(LichTrinh, on_delete=models.CASCADE)
    IDXe = models.ForeignKey(Xe, on_delete=models.CASCADE)
    GiaVeXe = models.IntegerField(default='')
    TinhTrang = models.BooleanField(default=True)
    MoTa = models.TextField(max_length=100, default='', null=True)
    NgayThem = models.DateField(auto_now=True)
    def __init____(self):
        return self.GiaVeXe

class VeXe(models.Model):
    IDLichTrinh = models.ForeignKey(LichTrinh, on_delete=models.CASCADE)
    IDGhe = models.ForeignKey(Ghe, on_delete=models.CASCADE)
    IDKhachHang = models.ForeignKey(KhachHang, on_delete=models.CASCADE)
    IDGiaVe = models.ForeignKey(GiaVe, on_delete=models.CASCADE)
    TinhTrang = models.BooleanField(default=True)
    MoTa = models.TextField(max_length=100, default='', null=True)
    NgayThem = models.DateField(auto_now=True)
    def __init____(self):
        return self.IDKhachHang

class TrangThaiDatVeXe(models.Model):
    IDLichTrinh = models.ForeignKey(LichTrinh, on_delete=models.CASCADE)
    SoGhe = models.SmallIntegerField(default='')
    TrangThai = models.BooleanField(default=False)
    def __init____(self):
        return self.IDLichTrinh
