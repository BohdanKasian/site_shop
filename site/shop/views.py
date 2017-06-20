from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from .models import Base, Product
from django.views.generic.detail import DetailView
from .forms import ProductForm


def index(request):
	template = "shop/index.html"

	return render(request, template)


# def laptop(request):

# 	item = product.objects.filter(title__icontains="оутбу")
# 	template = "shop/laptop.html"
# 	context = {
# 		"laptops": item
# 	}

# 	return render(request, template, context)


def pc(request):	
	template = "shop/pc.html"

	return render(request, template)


class laptop:
	laptop_all = Product.objects.filter(title__icontains="оутбу")

	def all_laptop(request):
		kort = []
		i = 1
		recs = []
		for rec in laptop.laptop_all:
			if i % 3 == 0:
				recs.append(rec)
				kort.append(tuple(recs))
				recs = []
			else:
				recs.append(rec)
				if i == len(laptop.laptop_all):
					kort.append(tuple(recs))
			i += 1

		return render (request, "shop/laptop.html", locals())


	def simple(request):
		laptop_simple = laptop.laptop_all.filter(price__lte=15000)
		kort = []
		i = 1
		recs = []
		for rec in laptop_simple:
			if i % 3 == 0:
				recs.append(rec)
				kort.append(tuple(recs))
				recs = []
			else:
				recs.append(rec)
				if i == len(laptop_simple):
					kort.append(tuple(recs))
			i += 1
		context={
			"simple":kort
		}
		return render(request, "shop/simple.html", context)

	def universal(request):
		laptop_universal = laptop.laptop_all.exclude(price__lte=10000)
		kort = []
		i = 1
		recs = []
		for rec in laptop_universal:
			if i % 3 == 0:
				recs.append(rec)
				kort.append(tuple(recs))
				recs = []
			else:
				recs.append(rec)
				if i == len(laptop_universal):
					kort.append(tuple(recs))
			i += 1
		context={
			"universal":kort
		}
		return render(request, "shop/universal.html", context)

	def lungs(request):
		laptop_lungs = laptop.laptop_all.filter(weight__lte=1.5)
		kort = []
		i = 1
		recs = []
		for rec in laptop_lungs:
			if i % 3 == 0:
				recs.append(rec)
				kort.append(tuple(recs))
				recs = []
			else:
				recs.append(rec)
				if i == len(laptop_lungs):
					kort.append(tuple(recs))
			i += 1
		context={
			"lungs": kort
		}
		return render(request, "shop/lungs.html", context)

	def gaming(request):
		laptop_gaming = laptop.laptop_all.exclude(price__lte=25000)
		kort = []
		i = 1
		recs = []
		for rec in laptop_gaming:
			if i % 3 == 0:
				recs.append(rec)
				kort.append(tuple(recs))
				recs = []
			else:
				recs.append(rec)
				if i == len(laptop_gaming):
					kort.append(tuple(recs))
			i += 1
		context = {
			"gaming":kort
		}
		return render(request, "shop/gaming.html", context)

	def detail(request, item_id):
		laptop_detail = get_object_or_404(laptop.laptop_all, id=item_id)
		template = "shop/detail.html"
		context = {
			"detail": laptop_detail
		}
		return render(request, template, context)

