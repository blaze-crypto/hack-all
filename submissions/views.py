# views.py

from django.shortcuts import render, redirect
from .forms import UserSubmissionForm

def submit_form_view(request):
    if request.method == 'POST':
        form = UserSubmissionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')  # Redirect to a success page
    else:
        form = UserSubmissionForm()
    return render(request, 'services.html', {'form': form})
