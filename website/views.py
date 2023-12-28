from django.shortcuts import render

def home(request):
	return render(request, 'home.html', {})

def contact(request):
	if request.method == "POST":

		Your_Name = request.POST['Your Name']
		Your_Email = request.POST['Your Email']
		Message = request.POST['Message']

		return render(request, 'contact.html', {'Your_name': Your_Name})

	else:	
		return render(request, 'contact.html', {})

def about(request):
	return render(request, 'about.html', {})

def services(request):
	return render(request, 'services.html', {})

def doctors(request):
	return render(request, 'doctors.html', {})

def appointment(request):
	if request.method == "POST":
		'''
		Your_Name = request.POST['Your Name']
		Your_Email = request.POST['Your Email']
		Message = request.POST['Message']
'''
		return render(request, 'appointment.html', {})

	else:	
		return render(request, 'appointment.html', {})

