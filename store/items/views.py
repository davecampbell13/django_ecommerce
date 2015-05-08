from django.shortcuts import render
from .models import Item, Order
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect, HttpResponse
from django.core import serializers
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse


# Create your views here.

def index(request):
	page = request.GET.get('page')
	search = request.GET.get('search')
	price = request.GET.get('price')

	our_items = Item.objects.all()	

	if search:
		our_items = Item.objects.filter(name__icontains=search)	

	if price:
		our_items = our_items.filter(price__lte=price)
	
	paginator = Paginator(our_items, 10)

	try:
		items = paginator.page(page)
	except PageNotAnInteger:
		items = paginator.page(1)
	except EmptyPage:
		items = paginator.page(paginator.num_pages)
	if request.GET.get('json'):
		data = serializers.serialize("json", our_items)
		return HttpResponse(data, content_type='application/json')
	else:	
		return render(request, 'items/index.html', {"items_list": items, "search_price" : price})

def show(request, item_id):
	#get_object_or_404(Disease, pk=disease_id)
	try:
	    item = Item.objects.get(pk=item_id)
	except Item.DoesNotExist:
	    raise Http404("Item does not exist")
	return render(request, 'items/show.html', {'item': item})

def cart(request):
	#check if they're logged in
	user = request.user
	if not user.is_authenticated():
		return render(request, 'users/login.html')

	all_orders = Order.objects.all()
	
	#check if they have orders staus of 1
	order = all_orders.filter(user=user.id).filter(status=1)
	if not order:
		return render(request, 'items/cart.html', {"items": [], "total" : 0})
		# print order
	items = order[0].items.all()
	total = 0

	for item in items:
		total += item.price

	return render(request, 'items/cart.html', {"items": items, "total" : total})

def add(request, item_id):
	user = request.user
	#check if they're logged in
	if not user.is_authenticated():
		return render(request, 'user/login.html')

		# refactor into method
	all_orders = Order.objects.all()
	
	#check if they have orders staus of 1
	order = all_orders.filter(user=user.id).filter(status=1)
	item = Item.objects.get(pk=item_id)
	
	if order:
		order[0].items.add(item)
	else:
		o = Order(user=user, status=1)
		o.save()
		o.items.add(item)
	
		
	return HttpResponseRedirect(reverse("items:cart"))

def delete(request, item_id):
	user = request.user
	if not user.is_authenticated():
		return render(request, 'user/login.html')

	all_orders = Order.objects.all()
	
	#check if they have orders staus of 1
	order = all_orders.filter(user=user.id).filter(status=1)
	item = Item.objects.get(pk=item_id)
	
	order[0].items.remove(item)

	return HttpResponseRedirect(reverse("items:cart"))

def payment(request):
	return render(request, 'items/payment.html')

def thankyou(request):
	user = request.user
	#check if they have orders staus of 1
	order = Order.objects.all().filter(user=user.id).filter(status=1)[0]
	order.status = 2
	order.save()
	return render(request, 'items/thankyou.html')




