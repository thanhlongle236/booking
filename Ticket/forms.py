from django import forms
from .models import KhachHang

# Form tự định nghĩa, tự tạo
# class BookingKH(forms.Form):
#     TenKhachHang = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
#     DienThoai = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class': 'form-control'}))
#     Email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))
#     DiemDon = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
#     GhiChu = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

class BookingKH(forms.ModelForm):
    class Meta:
        model = KhachHang
        fields = ('TenKhachHang', 'DienThoai', 'Email', 'DiemDon', 'GhiChu')
        widgets = {
            'TenKhachHang': forms.TextInput(attrs={'class': 'form-control'}),
            'DienThoai': forms.TextInput(attrs={'class': 'form-control'}),
            'Email': forms.TextInput(attrs={'class': 'form-control'}),
            'DiemDon': forms.TextInput(attrs={'class': 'form-control'}),
            'GhiChu': forms.TextInput(attrs={'class': 'form-control'}),
        }
