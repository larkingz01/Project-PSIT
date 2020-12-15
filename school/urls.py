from django.urls import include, path
from .views import * #ดึงฟังก์ชัน HomePage มาทำงาน

urlpatterns = [
	path('',HomePage, name='home-page'),
	path('register/', Register, name='register-page'),
	path('booking/', Booking, name='booking-page'),
	path('table/', Table, name='table-page'),
	]

