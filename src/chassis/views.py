from django.shortcuts import render
from .data import retrieve_data, save_chassis,get_chassis,update_chassis,delete_chassis, retrieve_chassis_names, ct_chassis_get, save_engine_compatibility,save_transmission_compatibility,save_electrical_compatibility,save_suspension_compatibility,save_aerials_compatibility,update_chassis_status
from .forms import ChassisForm
from .models import Chassis
from django.http import HttpResponse
from home import config
from engine.data import retrieve_engine_data
from transmission.data import retrieve_transmission_data
from electricalsystem.data import retrieve_electrical_system_data
from suspension.data import retrieve_data as retrieve_suspension_data
from aerials.data import retrieve_aerial_data
from home import config

# Create your views here.
def chassis_view(request):
    print("Inside chassis view")
    chassis_data = retrieve_data()
    status_list  = config.STATUS_CONFIG_LIST    
    context = {'chassis_data': chassis_data,'status_list':status_list}
    return render(request, 'chassis/chassis_view.html', context)

def ct_chassis_view(request):
    print("Inside ct_chassis_view ")
    chassis_data = retrieve_chassis_names()
    context = {'chassis_data': chassis_data}
    return render(request, 'chassis/ct_chassis_view.html', context)

def ct_chassis_get_view(request, chassis):
    print("Inside ct_chassis_get_view ")
    chassis_data, engine_list, transmission_list, electrical_system_list,front_suspension_list,rear_suspension_list = ct_chassis_get(chassis)
    context = {'chassis_data': chassis_data, 'engine_list':engine_list, 'transmission_list':transmission_list, 'electrical_system_list':electrical_system_list, 'front_suspension_list':front_suspension_list, 'rear_suspension_list':rear_suspension_list}
    return render(request, 'chassis/ct_chassis_get_view.html', context)

def chassis_create_view(request):
    form = ChassisForm(request.POST or None)
    print("hello")

    query_array = []
    cid = -1
    if request.method == 'POST':
        #chassis = Chassis(chassis_name=request.POST.get("chassis_name"), frontal_airbags=request.POST.get("frontal_airbags"), seating_capacity=request.POST.get("seating_capacity"), side_roll_protection=request.POST.get("side_roll_protection"), front_gawr=request.POST.get("front_gawr"), rear_gawr=request.POST.get("rear_gawr"), chassis_cost=request.POST.get("chassis_cost"))
        query_array.append(request.POST.get("chassis_name"))
        query_array.append(request.POST.get("frontal_airbags"))
        query_array.append(int(request.POST.get("seating_capacity")))
        query_array.append(request.POST.get("side_roll_protection"))
        query_array.append(int(request.POST.get("front_gawr")))
        query_array.append(int(request.POST.get("rear_gawr")))
        query_array.append(float(request.POST.get("chassis_cost")))
        cid = save_chassis(query_array)
    context = {
        'form':form,
        'cid':cid
    }
    
    if request.method != 'POST':
        return render(request, "chassis/chassis_create.html", context)
    else:
        #return chassis_view(request)
        return chassis_engine_compatibility_view(request,cid)

def chassis_get_view(request,chassis_id):
    form = ChassisForm(request.POST or None)
    print("Inside get view",chassis_id)

    query_array = []
    try:
        chassis = get_chassis(chassis_id)
        print("get view chassis",chassis.cid)
    except:
        return HttpResponse(config.CHASSIS_DATA_NOT_FOUND)
   # form.
    context = {
        'form':form,
        'chassis':chassis
    }
    
    return render(request, "chassis/chassis_update.html", context)

def chassis_delete_view(request,my_id):
    form = ChassisForm(request.POST or None)
    print("inside delete view ",my_id)

    chassis = delete_chassis(my_id)

    context = {
        'form':form,
        'cid':my_id
    }
    
    return chassis_view(request)

def chassis_update_view(request):
    form = ChassisForm(request.POST or None)
    print("hello update ")

    query_array = []

    if request.method == 'POST':
        #chassis = Chassis(chassis_name=request.POST.get("chassis_name"), frontal_airbags=request.POST.get("frontal_airbags"), seating_capacity=request.POST.get("seating_capacity"), side_roll_protection=request.POST.get("side_roll_protection"), front_gawr=request.POST.get("front_gawr"), rear_gawr=request.POST.get("rear_gawr"), chassis_cost=request.POST.get("chassis_cost"))
        query_array.append(request.POST.get("cid"))
        query_array.append(request.POST.get("chassis_name"))
        query_array.append(request.POST.get("frontal_airbags"))
        query_array.append(request.POST.get("seating_capacity"))
        query_array.append(request.POST.get("side_roll_protection"))
        query_array.append(request.POST.get("front_gawr"))
        query_array.append(request.POST.get("rear_gawr"))
        query_array.append(request.POST.get("chassis_cost"))
        print(query_array)
        update_chassis(query_array)
    context = {
        'form':form
    }
    if request.method != 'POST':
        return render(request, "chassis/chassis_update.html", context)
    else :
        return chassis_view(request)


def chassis_engine_compatibility_view(request,cid):
    print("Inside chassis_engine_compatibility_view")
    context = {"engine_data":retrieve_engine_data()[0],"cid":cid}
    return render(request, "chassis/chassis_engine_compatibility.html", context)

def chassis_transmission_compatibility_view(request):
    print("Inside chassis_transmission_compatibility_view")
    engine_id_list = [int(i) for i in request.POST.getlist('selected_engine')]
    cid = request.POST.get('cid')
    save_engine_compatibility(engine_id_list, cid)
    context = {"transmission_data":retrieve_transmission_data()[0],"cid":cid}
    return render(request, "chassis/chassis_tranmission_compatibility.html", context)

def chassis_electricals_compatibility_view(request):
    print("Inside chassis_electricals_compatibility_view")
    transmission_id_list = [int(i) for i in request.POST.getlist('selected_transmission')]
    cid = request.POST.get('cid')
    save_transmission_compatibility(transmission_id_list, cid)
    context = {"electrical_system_data":retrieve_electrical_system_data()[0],"cid":cid}
    return render(request, "chassis/chassis_electricals_compatibility.html", context)

def chassis_suspension_compatibility_view(request):
    print("chassis_suspension_compatibility_view ")
    transmission_id_list = [int(i) for i in request.POST.getlist('selected_electrical')]
    cid = request.POST.get('cid')
    save_electrical_compatibility(transmission_id_list, cid)
    context = {"suspension_data":retrieve_suspension_data()[0],"cid":cid}
    return render(request, "chassis/chassis_suspension_compatibility.html", context)

def chassis_aerials_compatibility_view(request):
    print("chassis_aerials_compatibility_view ")
    fa_suspension_id_list = [int(i) for i in request.POST.getlist('selected_fa_suspension')]
    ra_suspension_id_list = [int(i) for i in request.POST.getlist('selected_ra_suspension')]
    cid = request.POST.get('cid')
    save_suspension_compatibility(fa_suspension_id_list,ra_suspension_id_list,cid)
    context = {"aerial_data":retrieve_aerial_data()[0],"cid":cid}
    return render(request, "chassis/chassis_aerials_compatibility.html", context)

def chassis_save_aerials_compatibility_view(request):
    print("chassis_save_aerials_compatibility_view ")
    aerial_id_list = [int(i) for i in request.POST.getlist('selected_aerial')]
    cid = request.POST.get('cid')
    save_aerials_compatibility(aerial_id_list,cid)
    #return render(request, "chassis/chassis_aerials_compatibility.html", {})
    return chassis_view(request)

def update_chassis_status_view(request,cid,status):
    print("Inside update_chassis_status_view ")
    print(cid,status);
    update_chassis_status(cid,status)
    return chassis_view(request)