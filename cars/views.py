from django.shortcuts import render

# Create your views here.
from django.shortcuts import render 
from .forms import cars
def car_selection(request):
	manufacturer = 'None'
	name = 'None'

	if request.method == 'POST':
		form = cars(request.POST)
		if form.is_valid():
			manufacturer = form.cleaned_data['manufacturer']
			name = form.cleaned_data['name']
			data = {'manufacturer': manufacturer, 'name': name}
			return render(request, 'cars/car_details.html', data)
		else:
			data = {'manufacturer': 'None', 'name': 'None'}
			return render(request, 'cars/car_details.html', data)
	else:
		form = cars()
	return render(request, 'cars/car_selection.html', {'form': form})



