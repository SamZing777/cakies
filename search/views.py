from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from store.models import Cake, Category, Writer


def search(request):
	search = request.GET.get('q')
	cakes = Cake.objects.all()
	if search:
		cakes = cakes.filter(
			Q(name__icontains=search)|Q(category__name__icontains=search)|Q(writer__name__icontains=search)

		)

	paginator = Paginator(cakes, 10)
	page = request.GET.get('page')
	cakes = paginator.get_page(page)

	context = {
		"cake": cakes,
		"search": search,
	}
	return render(request, 'store/category.html', context)
