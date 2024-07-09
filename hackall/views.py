from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib import messages


def homepage(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def error_404(request, exception):
    return render(request, '404.html', status=404)


def submit(request):
    return render(request, 'submit.html')

def submit_form_view(request):
    if request.method == 'POST':
        form = UserSubmissionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')  # Redirect to a success page
    else:
        form = UserSubmissionForm()
    return render(request, 'services.html', {'form': form})
