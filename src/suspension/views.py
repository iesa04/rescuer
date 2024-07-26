from django.shortcuts import render
from .data import retrieve_data, save_suspension, get_suspension, update_suspension, delete_suspension,get_fa_compatibility,modify_fa_compatibility,get_ra_compatibility,modify_ra_compatibility
from .forms import SuspensionForm
from .models import Suspension
from django.http import HttpResponse

def suspension_view(request):
    print("Inside suspension view")
    suspension_data, chassis_front, chassis_rear = retrieve_data()
    context = {'suspension_data': suspension_data, 'chassis_front':chassis_front, 'chassis_rear':chassis_rear}
    return render(request, 'suspension/suspension_view.html', context)


def suspension_create_view(request):
    form = SuspensionForm(request.POST or None)
    print("Hello from suspension create view")
    suspension_id = -1
    if request.method == 'POST':
        suspension_data = [
            request.POST.get("suspension_name"),
            float(request.POST.get("suspension_cost"))
        ]
        suspension_id = save_suspension(suspension_data)

    context = {'form': form,"suspension_id":suspension_id}

    if request.method != 'POST':
        return render(request, "suspension/suspension_create.html", context)
    else:
        #return suspension_view(request)
        return get_fa_compatibility_view(request,suspension_id)

def suspension_get_view(request, suspension_id):
    form = SuspensionForm(request.POST or None)
    print("Inside suspension get view", suspension_id)

    try:
        suspension = get_suspension(suspension_id)
    except Exception as e:
        return HttpResponse(f'Exception: {str(e)}')

    context = {'form': form, 'suspension': suspension}

    return render(request, "suspension/suspension_update.html", context)

def suspension_delete_view(request, suspension_id):
    form = SuspensionForm(request.POST or None)
    print("Inside suspension delete view", suspension_id)

    delete_suspension(suspension_id)

    context = {'form': form, 'suspension_id': suspension_id}

    return suspension_view(request)

def suspension_update_view(request):
    form = SuspensionForm(request.POST or None)
    print("Hello from suspension update view")

    if request.method == 'POST':
        suspension_data = [
            int(request.POST.get("suspension_id")),
            request.POST.get("suspension_name"),
            float(request.POST.get("suspension_cost"))
        ]
        update_suspension(suspension_data)

    context = {'form': form}

    if request.method != 'POST':
        return render(request, "suspension/suspension_update.html", context)
    else:
        return suspension_view(request)

def get_fa_compatibility_view(request,suspension_id):
    print("Inside get_fa_compatibility_view")
    compatible, chassis_data = get_fa_compatibility(suspension_id)
    context = {'compatible': compatible, 'chassis_data': chassis_data,'suspension_id':suspension_id}
    return render(request, 'suspension/suspension_fa_compatibility.html', context)


def modify_fa_compatibility_view(request):
    print("Inside modify_fa_compatibility_view")
    chassis_list = [int(i) for i in request.POST.getlist('selected_chassis')]
    suspension_id =  request.POST.get('suspension_id')
    print( chassis_list)
    print(suspension_id)
    modify_fa_compatibility(suspension_id,chassis_list)
    if request.method != 'POST':
        return render(request, "suspension/suspension_fa_compatibility.html", context)
    else:
        #return suspension_view(request)
        return get_ra_compatibility_view(request,suspension_id)

def get_ra_compatibility_view(request,suspension_id):
    print("Inside get_ra_compatibility_view")
    compatible, chassis_data = get_ra_compatibility(suspension_id)
    context = {'compatible': compatible, 'chassis_data': chassis_data,'suspension_id':suspension_id}
    return render(request, 'suspension/suspension_ra_compatibility.html', context)


def modify_ra_compatibility_view(request):
    print("Inside modify_ra_compatibility_view")
    chassis_list = [int(i) for i in request.POST.getlist('selected_chassis')]
    suspension_id =  request.POST.get('suspension_id')
    print( chassis_list)
    print(suspension_id)
    modify_ra_compatibility(suspension_id,chassis_list)
    if request.method != 'POST':
        return render(request, "suspension/suspension_ra_compatibility.html", context)
    else:
        return suspension_view(request)        