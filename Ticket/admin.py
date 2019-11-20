from django.contrib import admin
from .models import LichTrinh, HangXe, LoaiXe, Xe, KhachHang, Ghe, GiaVe, VeXe, TrangThaiDatVeXe

class LichTrinhAdmin(admin.ModelAdmin):
    list_display = ['id','TenLichTrinh','DiemDi', 'DiemDen','DiemDi', 'ThoiGian','GioDi', 'NgayDi','TinhTrang']
    list_filter = ['NgayDi']
    search_fields = ['NgayDi']
    # lấy khoá ngoại
    # def get_Tuyen(self, obj):
    #         return obj.IDTuyen.TenTuyen
    # get_Tuyen.admin_order_field  = 'IDTuyen'  #Allows column order sorting
    # get_Tuyen.short_description = 'Ten Tuyen lay tu bang tuyen'  #Renames column head
#     def get_DiemDi_DiemDen(self, obj):
#             return obj.IDTuyen.DiemDi, obj.IDTuyen.DiemDen
#     get_DiemDi_DiemDen.admin_order_field  = 'IDTuyen'
#     get_DiemDi_DiemDen.short_description = 'Diem Di va Diem Den'
admin.site.register(LichTrinh, LichTrinhAdmin)

class HangXeAdmin(admin.ModelAdmin):
    list_display = ['id','TenHangXe', 'AnhHangXe','DienThoai', 'TinhTrang']
    list_filter = ['TenHangXe']
    search_fields = ['TenHangXe']
admin.site.register(HangXe, HangXeAdmin)

class LoaiXeAdmin(admin.ModelAdmin):
    list_display = ['id','TenLoaiXe', 'SoLuongGhe', 'TinhTrang']
    list_filter = ['TenLoaiXe']
    search_fields = ['TenLoaiXe']
admin.site.register(LoaiXe, LoaiXeAdmin)

class XeAdmin(admin.ModelAdmin):
    list_display = ['id','TenXe','get_LT','get_TenHX','get_AnhHX','get_TenLX']
    list_filter = ['TenXe']
    search_fields = ['TenXe']
    def get_TenHX(self, obj):
        return obj.IDHangXe.TenHangXe
    get_TenHX.admin_order_field  = 'IDHangXe'  
    get_TenHX.short_description = 'Ten Hang Xe'
    def get_AnhHX(self, obj):
        return obj.IDHangXe.AnhHangXe
    get_TenHX.admin_order_field  = 'IDHangXe'  
    get_TenHX.short_description = 'Anh Hang Xe'
    def get_TenLX(self, obj):
        return obj.IDLoaiXe.TenLoaiXe
    get_TenLX.admin_order_field  = 'IDLoaiXe'
    get_TenLX.short_description = 'Ten Loai Xe'
    def get_LT(self, obj):
        return obj.IDLichTrinh.TenLichTrinh
    get_LT.admin_order_field  = 'IDLichTrinh'  
    get_LT.short_description = 'Lich Trinh'
admin.site.register(Xe, XeAdmin)

class KhachHangAdmin(admin.ModelAdmin):
    list_display = ['id','TenKhachHang','DienThoai', 'Email', 'DiemDon', 'GhiChu']
    list_filter = ['id']
    search_fields = ['TenKhachHang']
admin.site.register(KhachHang, KhachHangAdmin)

# class GheAdmin(admin.ModelAdmin):
#     list_display = ['id','get_LT','SoGhe', 'TinhTrang', 'MoTa']
#     list_filter = ['id']
#     search_fields = ['TenKhachHang']
#     def get_LT(self, obj):
#         return obj.IDLichTrinh.TenLichTrinh
#     get_LT.admin_order_field  = 'IDLichTrinh'  
#     get_LT.short_description = 'Lich Trinh'
# admin.site.register(Ghe, GheAdmin)
class GheAdmin(admin.ModelAdmin):
    list_display = ['id','get_Xe','SoGhe', 'TinhTrang', 'MoTa']
    list_filter = ['id']
    search_fields = ['TenKhachHang']
    def get_Xe(self, obj):
        return obj.IDXe.TenXe
    get_Xe.admin_order_field  = 'IDXe'  
    get_Xe.short_description = 'Xe'
admin.site.register(Ghe, GheAdmin)

class GiaVeAdmin(admin.ModelAdmin):
    list_display = ['id','get_LT','get_Xe','GiaVeXe', 'TinhTrang', 'MoTa']
    list_filter = ['id']
    search_fields = ['TenKhachHang']
    def get_LT(self, obj):
        return obj.IDLichTrinh.TenLichTrinh
    get_LT.admin_order_field  = 'IDLichTrinh'  
    get_LT.short_description = 'Lich Trinh'
    def get_Xe(self, obj):
        return obj.IDXe.TenXe
    get_Xe.admin_order_field  = 'IDXe'  
    get_Xe.short_description = 'Xe'
admin.site.register(GiaVe, GiaVeAdmin)

class VeXeAdmin(admin.ModelAdmin):
    list_display = ['id','get_LT','get_Ghe','get_KH','get_GiaVe','TinhTrang', 'MoTa']
    list_filter = ['id']
    search_fields = ['TenKhachHang']
    def get_LT(self, obj):
        return obj.IDLichTrinh.TenLichTrinh
    get_LT.admin_order_field  = 'IDLichTrinh'  
    get_LT.short_description = 'Lich Trinh'
    def get_Ghe(self, obj):
        return obj.IDGhe.SoGhe
    get_Ghe.admin_order_field  = 'IDGhe'  
    get_Ghe.short_description = 'So Ghe'
    def get_KH(self, obj):
        return obj.IDKhachHang.TenKhachHang
    get_KH.admin_order_field  = 'IDKhachHang'  
    get_KH.short_description = 'Khach Hang'
    def get_GiaVe(self, obj):
        return obj.IDGiaVe.GiaVeXe
    get_GiaVe.admin_order_field  = 'IDGiaVe'  
    get_GiaVe.short_description = 'Gia Ve'
admin.site.register(VeXe, VeXeAdmin)

class TrangThaiDatVeXeAdmin(admin.ModelAdmin):
    list_display = ['id','get_LT','SoGhe','TrangThai']
    list_filter = ['id']
    search_fields = ['TenKhachHang']
    def get_LT(self, obj):
        return obj.IDLichTrinh.TenLichTrinh
    get_LT.admin_order_field  = 'IDLichTrinh'  
    get_LT.short_description = 'Lich Trinh'
admin.site.register(TrangThaiDatVeXe, TrangThaiDatVeXeAdmin)



