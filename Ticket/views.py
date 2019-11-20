from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import LichTrinh, HangXe, Xe, GiaVe
from .forms import BookingKH
from django.views import View

# from .models import Post
# Create your views here.
# lấy từng data theo pk, xem lai video bai 6 cua sonnguyen
# def list(request):
#     list_post = get_object_or_404(Post, pk=1)
#     Data = {'Booking': list_post}
#     return render(request, 'Booking/booking.html', Data)

# def list(request):
#     Data = {'Booking': Post.objects.all().order_by('-date')}
#     return render(request, 'Booking/booking.html', Data)

# def post(request, id):
#     post = Post.objects.get(id=id)
#     return render(request, 'Booking/detailbooking.html', {'post': post})

def list(request):
    Data = {'Booking': LichTrinh.objects.all().order_by('id')}
    return render(request, 'Booking/booking.html', Data)

# get lich trinh lay thong tin khach hang
def post(request, IDLichTrinh):
    post = LichTrinh.objects.get(id=IDLichTrinh)
    form = BookingKH()
    if request.method == 'POST':
        form = BookingKH(request.POST)
        if form.is_valid():
            context = {'data': form}
            form.save()
            return render(request, 'Booking/success.html', context)
        else:
            return HttpResponse('Not Valid')
    return render(request, 'Booking/detailbooking.html', {'post': post, "f": form})

def detailView(request, IdHangXe):
    a = HangXe.objects.get(pk=IdHangXe)
    return render(request, 'Booking/detail.html', {'qs': a})

# Phải sử dụng modelform mới chạy được hàm save()
class SaveBookingKH(View):
    def get(self, request):
        a = BookingKH()
        return render(request, 'Booking/bookkh.html', {'f': a})
    def post(self, request):
        b = BookingKH(request.POST)
        if b.is_valid():
            context = {'data': b}
            b.save()
            return render(request, 'Booking/success.html', context)
        else:
            return HttpResponse('Not Valid')
    def put(self):
        pass

# def aaa(request, IDLichTrinh):
#     post = LichTrinh.objects.get(LichTrinh, id=IDLichTrinh)
#     form = BookingKH()
#     if request.method == 'POST':
#         form = BookingKH(request.POST, author=request.user,post=post)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(request.path)
#     return render(request, "blog/post.html", {"post":post, "form": form})
# class SaveBooking(View):
#     def get(self, request):
#         a = BookingKH()
#         return render(request, 'Booking/listhangxe.html', {'c': a})
#     def post(self, request):
#         b = BookingKH(request.POST)
#         if b.is_valid():
#             context = {'data': b}
#             b.save()
#             return render(request, 'Booking/success.html', context)
#         else:
#             return HttpResponse('Not Valid')
#     def put(self):
#         pass

# bảng xe phải có id lịch trình mới thêm vào đc template

