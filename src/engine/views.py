from django.shortcuts import render
from .data import retrieve_engine_data, save_engine, get_engine, update_engine, delete_engine, get_compatibility,modify_compatibility
from .forms import EngineForm
from .models import Engine
from django.http import HttpResponse

def engine_view(request):
    print("Inside engine view")
    engine_data, chassis_data = retrieve_engine_data()
    context = {'engine_data': engine_data, 'chassis_data': chassis_data}
    return render(request, 'engine/engine_view.html', context)

def engine_create_view(request):
    form = EngineForm(request.POST or None)
    print("Inside engine create view")
    engine_id = -1

    if request.method == 'POST':
        engine_data = [
            request.POST.get("engine_name"), int(request.POST.get("horsepower")),
            int(request.POST.get("peak_torque")), int(request.POST.get("dry_weight")),
            int(request.POST.get("cylinders")), int(request.POST.get("displacement")),
            int(request.POST.get("clutch_engagement_torque")), int(request.POST.get("governed_speed")),
            float(request.POST.get("engine_cost"))
        ]
        engine_id = save_engine(engine_data)

    context = {'form': form,'engine_id':engine_id}

    if request.method != 'POST':
        return render(request, "engine/engine_create.html", context)
    else:
        return engine_compatiblity_view(request,engine_id)

def engine_get_view(request, my_id):
    form = EngineForm(request.POST or None)
    print("Inside engine get view", my_id)

    try:
        engine = get_engine(my_id)
    except Exception as e:
        return HttpResponse(f'Exception: {str(e)}')

    context = {'form': form, 'engine': engine}

    return render(request, "engine/engine_update.html", context)

def engine_delete_view(request, my_id):
    form = EngineForm(request.POST or None)
    print("Inside engine delete view", my_id)

    delete_engine(my_id)

    context = {'form': form, 'engine_id': my_id}

    return engine_view(request)

def engine_update_view(request):
    form = EngineForm(request.POST or None)
    print("Inside engine update view")

    if request.method == 'POST':
        engine_data = [
            request.POST.get("engine_id"), request.POST.get("engine_name"),
            int(request.POST.get("horsepower")), int(request.POST.get("peak_torque")),
            int(request.POST.get("dry_weight")), int(request.POST.get("cylinders")),
            int(request.POST.get("displacement")), int(request.POST.get("clutch_engagement_torque")),
            int(request.POST.get("governed_speed")), float(request.POST.get("engine_cost"))
        ]
        update_engine(engine_data)

    context = {'form': form}

    if request.method != 'POST':
        return render(request, "engine/engine_update.html", context)
    else:
        return engine_view(request)

def engine_compatiblity_view(request, engine_id):
    print("Inside engine compatibility view")
    compatible, chassis_data = get_compatibility(engine_id)
    context = {'compatible': compatible, 'chassis_data': chassis_data,'engine_id':engine_id}
    return render(request, 'engine/engine_compatibility.html', context)


def modify_compatibility_view(request):
    print("Inside modify compatibility view")
    chassis_list = [int(i) for i in request.POST.getlist('selected_chassis')]
    engine_id =  request.POST.get('engine_id')
    print( chassis_list)
    print(engine_id)
    modify_compatibility(engine_id,chassis_list)
    if request.method != 'POST':
        return render(request, "engine/engine_compatibility.html", context)
    else:
        return engine_view(request)