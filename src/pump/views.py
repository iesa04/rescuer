from django.shortcuts import render
from .data import retrieve_pump_data, save_pump, get_pump, update_pump, delete_pump, get_compatibility, modify_compatibility
from .forms import PumpForm
from django.http import HttpResponse

def pump_view(request):
    print("Inside pump view")
    pump_data, aerial_data = retrieve_pump_data()
    context = {'pump_data': pump_data, 'aerial_data':aerial_data}
    return render(request, 'pump/pump_view.html', context)

def pump_create_view(request):
    form = PumpForm(request.POST or None)
    print("Inside pump create view")

    if request.method == 'POST':
        pump_data = [
            request.POST.get("pump_name"), float(request.POST.get("pump_cost"))
        ]
        pump_id = save_pump(pump_data)

    context = {'form': form}

    if request.method != 'POST':
        return render(request, "pump/pump_create.html", context)
    else:
        return pump_compatiblity_view(request, pump_id)

def pump_get_view(request, my_id):
    form = PumpForm(request.POST or None)
    print("Inside pump get view", my_id)

    try:
        pump = get_pump(my_id)
    except Exception as e:
        return HttpResponse(f'Exception: {str(e)}')

    context = {'form': form, 'pump': pump}

    return render(request, "pump/pump_update.html", context)

def pump_delete_view(request, my_id):
    form = PumpForm(request.POST or None)
    print("Inside pump delete view", my_id)

    delete_pump(my_id)

    context = {'form': form, 'pump_id': my_id}

    return pump_view(request)

def pump_update_view(request):
    form = PumpForm(request.POST or None)
    print("Inside pump update view")

    if request.method == 'POST':
        pump_data = [
            request.POST.get("pump_id"), request.POST.get("pump_name"),
            float(request.POST.get("pump_cost"))
        ]
        update_pump(pump_data)

    context = {'form': form}

    if request.method != 'POST':
        return render(request, "pump/pump_update.html", context)
    else:
        return pump_view(request)

def pump_compatiblity_view(request, pump_id):
    print("Inside pump compatibility view")
    compatible, aerial_data = get_compatibility(pump_id)
    context = {'compatible': compatible, 'aerial_data': aerial_data,'pump_id':pump_id}
    return render(request, 'pump/pump_compatibility.html', context)


def pump_modify_compatibility_view(request):
    print("Inside pump modify compatibility view")
    chassis_list = [int(i) for i in request.POST.getlist('selected_aerial')]
    pump_id =  request.POST.get('pump_id')
    print( chassis_list)
    print(pump_id)
    modify_compatibility(pump_id,chassis_list)
    if request.method != 'POST':
        return render(request, "pump/pump_compatibility.html", context)
    else:
        return pump_view(request)