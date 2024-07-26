from django.shortcuts import render, redirect
from .data import retrieve_transmission_data, save_transmission, get_transmission, update_transmission, delete_transmission, get_compatibility, modify_compatibility
from .forms import TransmissionForm
from django.http import HttpResponse

def transmission_view(request):
    print("Inside transmission view")
    transmission_data, chassis_data = retrieve_transmission_data()
    context = {'transmission_data': transmission_data, 'chassis_data':chassis_data}
    return render(request, 'transmission/transmission_view.html', context)

def transmission_create_view(request):
    form = TransmissionForm(request.POST or None)
    print("Inside transmission create view")
    tid=-1;
    if request.method == 'POST':
        transmission_data = [
            request.POST.get("transmission_name"), request.POST.get("transmission_type"),
            int(request.POST.get("gears")), int(request.POST.get("max_torque")),
            int(request.POST.get("weight")), float(request.POST.get("transmission_cost"))
        ]
        tid = save_transmission(transmission_data)

    context = {'form': form,'tid':tid}

    if request.method != 'POST':
        return render(request, "transmission/transmission_create.html", context)
    else:
        return transmission_compatiblity_view(request,tid)

def transmission_get_view(request, my_id):
    form = TransmissionForm(request.POST or None)
    print("Inside transmission get view", my_id)

    try:
        transmission = get_transmission(my_id)
    except Exception as e:
        return HttpResponse(f'Exception: {str(e)}')

    context = {'form': form, 'transmission': transmission}

    return render(request, "transmission/transmission_update.html", context)

def transmission_delete_view(request, my_id):
    form = TransmissionForm(request.POST or None)
    print("Inside transmission delete view", my_id)

    delete_transmission(my_id)

    context = {'form': form, 'transmission_id': my_id}

    return transmission_view(request)

def transmission_update_view(request):
    form = TransmissionForm(request.POST or None)
    print("Inside transmission update view")

    if request.method == 'POST':
        transmission_data = [
            request.POST.get("tid"), request.POST.get("transmission_name"),
            request.POST.get("transmission_type"), int(request.POST.get("gears")),
            int(request.POST.get("max_torque")), int(request.POST.get("weight")),
            float(request.POST.get("transmission_cost"))
        ]
        update_transmission(transmission_data)

    context = {'form': form}

    if request.method != 'POST':
        return render(request, "transmission/transmission_update.html", context)
    else:
        return transmission_view(request)

def transmission_compatiblity_view(request, tid):
    print("Inside transmission compatibility view")
    compatible, chassis_data = get_compatibility(tid)
    context = {'compatible': compatible, 'chassis_data': chassis_data,'tid':tid}
    return render(request, 'transmission/transmission_compatibility.html', context)


def transmission_modify_compatibility_view(request):
    print("Inside transmission modify compatibility view")
    chassis_list = [int(i) for i in request.POST.getlist('selected_chassis')]
    tid =  request.POST.get('tid')
    print( chassis_list)
    print(tid)
    modify_compatibility(tid,chassis_list)
    if request.method != 'POST':
        return render(request, "transmission/transmission_compatibility.html", context)
    else:
        return transmission_view(request)