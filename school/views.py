from django.shortcuts import render, redirect #ดึงมาจาก template
from django.http import HttpResponse #เขียนบนกระดาน
from django.contrib.auth.models import User
from .models import Time
import datetime

def HomePage(request):
	# return HttpResponse('<h1>Hello Nutthida</h1>')
	return render(request, 'school/home.html')

def Booking(request):
	if request.method == 'POST':
		data = request.POST.copy()
		name1 = data.get('name1')
		name2 = data.get('name2')
		name3 = data.get('name3')
		name4 = data.get('name4')
		court = data.get('court')
		time = data.get("time")

		booking = Time()
		booking.name1 = name1
		booking.name2 = name2
		booking.name3 = name3
		booking.name4 = name4 
		booking.time = time
		booking.court = court
		booking.save()
		return redirect('table-page')
		# return render(request, 'school/table.html')
	return render(request, 'school/booking.html')

def Booking2(request):
	return render(request, 'school/booking2.html')

def Table(request):
	score = Time.objects.all()
	context = {'score':score}

	return render(request, 'school/table.html', context)

def Register(request):
	if request.method == 'POST':
		data = request.POST.copy()
		first_name = data.get('first_name')
		last_name = data.get('last_name')
		email = data.get('email')
		password = data.get('password')

		newuser = User()
		newuser.username = email
		newuser.first_name = first_name
		newuser.last_name = last_name
		newuser.email = email
		newuser.set_password(password)
		newuser.save()
		return redirect('home-page')

	return render(request, 'school/register.html')


