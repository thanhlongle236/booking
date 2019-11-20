from django.urls import path
from . import views

urlpatterns = [
    path('booking/', views.list, name='booking'),
    path('booking/<int:IDLichTrinh>/', views.post, name='detailbooking'),
    path('detail/<int:IdHangXe>/', views.detailView, name='detail'),
    path('booking/bookkh/', views.SaveBookingKH.as_view(), name='bookkh'),
    # path('booking/<int:IDLichTrinh>/listhangxe', views.SaveBooking.as_view(), name='listhangxe'),
]