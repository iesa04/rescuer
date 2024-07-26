from django.shortcuts import render, redirect
from .data import retrieve_aerial_data, get_aerial, save_aerial, update_aerial, delete_aerial, get_compatibility, modify_compatibility,save_pump_compatibility,update_aerial_status
from .forms import AerialForm
from django.http import HttpResponse
from aerialclass.data import retrieve_aerial_class_data
from pump.data import retrieve_pump_data
from home import config

def aerial_view(request):
    print("Inside aerial view")
    aerial_data, chassis_data = retrieve_aerial_data()
    aerial_class_dict = retrieve_aerial_class_data()
    status_list  = config.STATUS_CONFIG_LIST    
    context = {'aerial_data': aerial_data,'aerials_class_data': aerial_class_dict, 'chassis_data':chassis_data,'status_list':status_list}
    return render(request, 'aerials/aerial_view.html', context)

def ct_aerial_view(request):
    print("Inside aerial view")
    aerial_class_dict = retrieve_aerial_class_data()
    print (aerial_class_dict)

    context = {'aerials_class_data': aerial_class_dict}

    return render(request, 'aerials/ct_aerial_view.html', context)

def ct_aerial_get_view(request, aerial_class):
    print("Inside aerial view")
    aerial_data, chassis_data = retrieve_aerial_data()
    aerial_class_dict = retrieve_aerial_class_data()
    print (aerial_class_dict)

    context = {'aerial_data': aerial_data,'aerials_class_data': aerial_class_dict, 'chassis_data':chassis_data, 'aerial_class':aerial_class}

    return render(request, 'aerials/ct_aerial_get_view.html', context)

def aerial_create_view(request):
    form = AerialForm(request.POST or None)
    print("Inside aerial create view")

    if request.method == 'POST':
        aerial_data = {
            'class_id': request.POST.get("class_id"),
            'aerial_name': request.POST.get("aerial_name"),
            'basket': request.POST.get("basket"),
            'hstyle_jack': request.POST.get("hstyle_jack"),
            'downjack': request.POST.get("downjack"),
            'stabilizer_spread': request.POST.get("stabilizer_spread"),
            'structural_ladder_warranty': request.POST.get("structural_ladder_warranty"),
            'flow_capacity': request.POST.get("flow_capacity"),
            'minimum_angle': request.POST.get("minimum_angle"),
            'maximum_angle': request.POST.get("maximum_angle"),
            'wind_rating': request.POST.get("wind_rating"),
            'ice_rating': request.POST.get("ice_rating"),
            'horizontal_ladder_reach': request.POST.get("horizontal_ladder_reach"),
            'vertical_ladder_reach': request.POST.get("vertical_ladder_reach"),
            'dry_payload_capacity': request.POST.get("dry_payload_capacity"),
            'wet_payload_capacity': request.POST.get("wet_payload_capacity"),
            'tank': request.POST.get("tank"),
            'aerial_cost': request.POST.get("aerial_cost"),
        }
        aerial_id = save_aerial(aerial_data)

    aerial_class_dict = retrieve_aerial_class_data()
    context = {'form': form,'aerials_class_data': aerial_class_dict}

    if request.method != 'POST':
        return render(request, "aerials/aerial_create.html", context)
    else:
        return aerial_compatiblity_view(request, aerial_id)

def aerial_get_view(request, aerial_id):
    form = AerialForm(request.POST or None)
    print("Inside aerial get view", aerial_id)

    try:
        aerial = get_aerial(aerial_id)
        aerial_class_dict = retrieve_aerial_class_data()
    except Exception as e:
        return HttpResponse(f'Exception: {str(e)}')

    context = {'form': form, 'aerial': aerial,'aerials_class_data': aerial_class_dict}

    return render(request, "aerials/aerial_update.html", context)

def aerial_delete_view(request, aerial_id):
    form = AerialForm(request.POST or None)
    print("Inside aerial delete view", aerial_id)

    delete_aerial(aerial_id)

    context = {'form': form, 'aerial_id': aerial_id}

    return aerial_view(request)

def aerial_update_view(request):
    form = AerialForm(request.POST or None)
    print("Inside aerial update view")

    if request.method == 'POST':
        aerial_data = {
            'aerial_id': request.POST.get("aerial_id"),
            'class_id': request.POST.get("class_id"),
            'aerial_name': request.POST.get("aerial_name"),
            'basket': request.POST.get("basket"),
            'hstyle_jack': request.POST.get("hstyle_jack"),
            'downjack': request.POST.get("downjack"),
            'stabilizer_spread': request.POST.get("stabilizer_spread"),
            'structural_ladder_warranty': request.POST.get("structural_ladder_warranty"),
            'flow_capacity': request.POST.get("flow_capacity"),
            'minimum_angle': request.POST.get("minimum_angle"),
            'maximum_angle': request.POST.get("maximum_angle"),
            'wind_rating': request.POST.get("wind_rating"),
            'ice_rating': request.POST.get("ice_rating"),
            'horizontal_ladder_reach': request.POST.get("horizontal_ladder_reach"),
            'vertical_ladder_reach': request.POST.get("vertical_ladder_reach"),
            'dry_payload_capacity': request.POST.get("dry_payload_capacity"),
            'wet_payload_capacity': request.POST.get("wet_payload_capacity"),
            'tank': request.POST.get("tank"),
            'aerial_cost': request.POST.get("aerial_cost"),
        }
        update_aerial(aerial_data)
    context = {'form': form}

    if request.method != 'POST':
        return render(request, "aerials/aerial_update.html", context)
    else :
        return aerial_view(request)

def aerial_compatiblity_view(request, aerial_id):
    print("Inside aerial compatibility view")
    compatible, chassis_data = get_compatibility(aerial_id)
    context = {'compatible': compatible, 'chassis_data': chassis_data,'aerial_id':aerial_id}
    return render(request, 'aerials/aerial_compatibility.html', context)

def aerial_modify_compatibility_view(request):
    print("Inside aerial modify compatibility view")
    chassis_list = [int(i) for i in request.POST.getlist('selected_chassis')]
    aerial_id =  request.POST.get('aerial_id')
    print( chassis_list)
    print(aerial_id)
    modify_compatibility(aerial_id,chassis_list)
    if request.method != 'POST':
        return render(request, "aerials/aerial_compatibility.html", context)
    else:
        pump_data = retrieve_pump_data()[0]
        context = {'pump_data': pump_data,'aerial_id':aerial_id}
        return render(request, 'aerials/aerial_pump_compatibility.html', context)

def aerial_modify_chassis_compatibility_view(request,aerial_id):
    print("Inside aerial modify chassis comperial_modify_chassis_compatibility_viewatibility view")
    chassis_list = [int(i) for i in request.POST.getlist('selected_chassis')]
    print( chassis_list)
    print(aerial_id)
    compatible, chassis_data = get_compatibility(aerial_id)
    context = {'compatible': compatible, 'chassis_data': chassis_data,'aerial_id':aerial_id}
     
    if request.method != 'POST':
        return render(request, "aerials/aerial_chassis_compatibility.html", context)
    else:
        return aerial_view(request)

def aerial_save_compatibility_view(request):
    print("Inside aerial save compatibility view")
    chassis_list = [int(i) for i in request.POST.getlist('selected_chassis')]
    aerial_id =  request.POST.get('aerial_id')
    print( chassis_list)
    print(aerial_id)
    modify_compatibility(aerial_id,chassis_list)
    if request.method != 'POST':
        return render(request, "aerials/aerial_chassis_compatibility.html", context)
    else:
        return aerial_view(request)

def save_pump_compatiblity_view(request):
    print("Inside aerial pump save compatibility view")
    pump_list = [int(i) for i in request.POST.getlist('selected_pump')]
    aerial_id =  request.POST.get('aerial_id')
    save_pump_compatibility(aerial_id,pump_list)
    return aerial_view(request)

def update_aerial_status_view(request,aerial_id,status):
    print("Inside update_aerial_status_view ")
    print(aerial_id,status);
    update_aerial_status(aerial_id,status)
    return aerial_view(request)