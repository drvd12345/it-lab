# studentData/views.py
from django.shortcuts import render, redirect
from .forms import StudentDataForm

def first_page(request):
    if request.method == 'POST':
        form = StudentDataForm(request.POST)
        if form.is_valid():
            request.session['name'] = form.cleaned_data['name']
            request.session['roll'] = form.cleaned_data['roll']
            request.session['subjects'] = form.cleaned_data['subjects']
            return redirect('studentData:second_page')
    else:
        form = StudentDataForm()
    return render(request, 'studentData/firstPage.html', {'form': form})

def second_page(request):
    name = request.session.get('name')
    roll = request.session.get('roll')
    subjects = request.session.get('subjects')
    return render(request, 'studentData/secondPage.html', {'name': name, 'roll': roll, 'subjects': subjects})
