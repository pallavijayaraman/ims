from django.shortcuts import render
from django.utils import timezone
from .models import Catalogue

def cat_list(request):
	catalogues = Catalogue.objects.filter(entry_date__lte=timezone.now()).order_by('entry_date')
	return render(request, 'inventory/cat_list.html', {'catalogues':catalogues})