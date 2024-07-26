from django.shortcuts import render
from .data import retrieve_user_types, get_admin_data, get_customer_data, get_supplier_data, save_admin, delete_admin
from .forms import AdminForm
from django.http import HttpResponse

def user_types_view(request):
	print("Inside user types")
	user_data = retrieve_user_types()
	context = {'user_data': user_data}
	return render(request, 'users/manage_users.html', context)

def admin_view(request):
	print("Inside admin view")
	admin_data = get_admin_data()
	context = {'admin_data': admin_data}
	return render(request, 'users/admin_view.html', context)

def customer_view(request):
	print("Inside customer view")
	customer_data = get_customer_data()
	context = {'customer_data': customer_data}
	return render(request, 'users/customer_view.html', context)

def supplier_view(request):
	print("Inside supplier view")
	supplier_data = get_supplier_data()
	context = {'supplier_data': supplier_data}
	return render(request, 'users/supplier_view.html', context)

def admin_create_view(request):
	print("Inside Admin create view")
	form = AdminForm(request.POST or None)

	query_array = []

	if request.method == 'POST':
		query_array.append(request.POST.get("username"))
		query_array.append(request.POST.get("password"))
		query_array.append(request.POST.get("name"))
		query_array.append(int(request.POST.get("phone_number")))

		save_admin(query_array)
	context = {
		'form':form
	}
    
	if request.method != 'POST':
		return render(request, 'users/admin_create.html', context)
	else :
		return admin_view(request)

def admin_delete_view(request, user_id):
	print("inside admin delete view ",user_id)

	form = AdminForm(request.POST or None)
	delete_admin(user_id)

	context = {
	    'form':form,
	    'user_id':user_id
	}
	return admin_view(request)
	##return render(request, "users/admin_view.html", context)