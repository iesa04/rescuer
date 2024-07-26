from django.shortcuts import render
from .data import retrieve_electrical_system_data, save_electrical_system, get_electrical_system, update_electrical_system, delete_electrical_system, get_compatibility, modify_compatibility
from .forms import ElectricalSystemForm
from django.http import HttpResponse

def electrical_system_view(request):
    print("Inside electrical system view")
    electrical_system_data, chassis_data = retrieve_electrical_system_data()
    context = {'electrical_system_data': electrical_system_data, 'chassis_data':chassis_data}
    return render(request, 'electricalsystem/electrical_system_view.html', context)

def electrical_system_create_view(request):
    form = ElectricalSystemForm(request.POST or None)
    print("Inside electrical system create view")

    if request.method == 'POST':
        electrical_system_data = [
            request.POST.get("electrical_name"), float(request.POST.get("electrical_cost"))
        ]
        electrical_id = save_electrical_system(electrical_system_data)

    context = {'form': form}

    if request.method != 'POST':
        return render(request, "electricalsystem/electrical_system_create.html", context)
    else:
        return electrical_compatiblity_view(request, electrical_id)

def electrical_system_get_view(request, my_id):
    form = ElectricalSystemForm(request.POST or None)
    print("Inside electrical system get view", my_id)

    try:
        electrical_system = get_electrical_system(my_id)
    except Exception as e:
        return HttpResponse(f'Exception: {str(e)}')

    context = {'form': form, 'electrical_system': electrical_system}

    return render(request, "electricalsystem/electrical_system_update.html", context)

def electrical_system_delete_view(request, my_id):
    form = ElectricalSystemForm(request.POST or None)
    print("Inside electrical system delete view", my_id)

    delete_electrical_system(my_id)

    context = {'form': form, 'electrical_system_id': my_id}

    return electrical_system_view(request)

def electrical_system_update_view(request):
    form = ElectricalSystemForm(request.POST or None)
    print("Inside electrical system update view")

    if request.method == 'POST':
        electrical_system_data = [
            request.POST.get("electrical_id"), request.POST.get("electrical_name"),
            float(request.POST.get("electrical_cost"))
        ]
        update_electrical_system(electrical_system_data)

    context = {'form': form}

    if request.method != 'POST':
        return render(request, "electricalsystem/electrical_system_update.html", context)
    else:
        return electrical_system_view(request)

def electrical_compatiblity_view(request, electrical_id):
    print("Inside engine compatibility view")
    compatible, chassis_data = get_compatibility(electrical_id)
    context = {'compatible': compatible, 'chassis_data': chassis_data,'electrical_id':electrical_id}
    return render(request, 'electricalsystem/electrical_system_compatibility.html', context)


def electrical_modify_compatibility_view(request):
    print("Inside modify compatibility view")
    chassis_list = [int(i) for i in request.POST.getlist('selected_chassis')]
    electrical_id =  request.POST.get('electrical_id')
    print( chassis_list)
    print(electrical_id)
    modify_compatibility(electrical_id,chassis_list)
    if request.method != 'POST':
        return render(request, "electricalsystem/electrical_system_compatibility.html", context)
    else:
        return electrical_system_view(request)