from django.urls import path
from .views import * #ดึงฟังก์ชัน HomePage มาทำงาน

urlpatterns = [
	# localhost:8000/
	path('',HomePage, name='home-page'),
	path('register/', Register, name='register-page')
]