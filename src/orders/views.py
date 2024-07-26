from django.shortcuts import render
from .data import ct_orders_data, ct_order_detail_data, ct_configure_aerial,ct_configure_chassis, ct_configure_engine, ct_configure_transmission, ct_configure_electricals, ct_configure_front_suspension, ct_configure_rear_suspension, ct_configure_pump, ct_configure_summary, create_order, place_order,ad_orders_data,ad_update_order_status
from home import config

def ct_orders_view(request):
    print("Inside ct_orders_view")
    orders_data = ct_orders_data(request.session['fdid'])
    context = {'orders_data': orders_data,'no_of_rec':len(orders_data)}
    return render(request, 'orders/ct_order_view.html', context)

def ad_orders_view(request):
    print("Inside ad_orders_view")
    orders_data = ad_orders_data() 
    status_list  = config.ORDER_STATUS_CONFIG_LIST    
    context = {'orders_data': orders_data,'status_list':status_list,'no_of_rec':len(orders_data)}    
    return render(request, 'orders/ad_order_view.html', context)

def ct_order_detail_view(request, order_id):
    print("Inside ct_order detail view")
    orders_data = ct_order_detail_data(order_id)
    context = {'orders_data': orders_data}
    return render(request, 'orders/ct_order_detail_view.html', context)

def ct_new_order_view(request):
    print("Inside ct new order view")
    context = {}
    return render(request, 'orders/ct_order_new.html', context)

def ct_config_aerial_view(request):
    print("Inside config aerial view")
    aerial_id=''
    if request.method != 'POST':
        aerial_id = request.GET.get("aerial")

    aerial_list = ct_configure_aerial()
    context = {'aerial_list':aerial_list,'aerial_id':aerial_id}
    return render(request, 'orders/ct_configurator_aerial.html', context)

def ct_config_chassis_view(request):
    print("Inside config chassis view ww")
    if request.method != 'POST':
        aerial_id = request.GET.get("aerial")
    else:
        aerial_id = request.POST.get("aerial")
    print(aerial_id)
    chassis_list = ct_configure_chassis(aerial_id)
    context = {'chassis_list':chassis_list, 'aerial_id':aerial_id}
    return render(request, 'orders/ct_configurator_chassis.html', context)

def ct_config_engine_view(request):
    print("Inside config engine view")
    if request.method != 'POST':
        aerial_id = request.GET.get("aerial")
        cid = request.GET.get("chassis")
    else:
        aerial_id = request.POST.get("aerial")
        cid = request.POST.get("chassis")
    print(aerial_id)
    print(cid)
    engine_list = ct_configure_engine(cid)
    context = {'engine_list':engine_list, 'aerial_id':aerial_id, 'cid':cid}
    return render(request, 'orders/ct_configurator_engine.html', context)

def ct_config_transmission_view(request):
    print("Inside config transmission view")

    if request.method != 'POST':
        aerial_id = request.GET.get("aerial")
        cid = request.GET.get("chassis")
        engine_id = request.GET.get("engine")
    else:
        aerial_id = request.POST.get("aerial")
        cid = request.POST.get("chassis")
        engine_id = request.POST.get("engine")
               
    print(aerial_id)
    print(cid)
    print(engine_id)
    transmission_list = ct_configure_transmission(cid)
    context = {'transmission_list':transmission_list, 'aerial_id':aerial_id, 'cid':cid, 'engine_id':engine_id}
    return render(request, 'orders/ct_configurator_transmission.html', context)

def ct_config_electrical_system_view(request):
    print("Inside config electical_system view")
    if request.method != 'POST':
        aerial_id = request.GET.get("aerial")
        cid = request.GET.get("chassis")
        engine_id = request.GET.get("engine")
        tid = request.GET.get("transmission")
    else:
        aerial_id = request.POST.get("aerial")
        cid = request.POST.get("chassis")
        engine_id = request.POST.get("engine")
        tid = request.POST.get("transmission")

    print(aerial_id)
    print(cid)
    print(engine_id)
    print(tid)
    electrical_list = ct_configure_electricals(cid)
    context = {'electrical_list':electrical_list, 'aerial_id':aerial_id, 'cid':cid, 'engine_id':engine_id, 'tid':tid}
    return render(request, 'orders/ct_configurator_electrical_system.html', context)

def ct_config_front_suspension_view(request):
    print("Inside config front susp view")

    if request.method != 'POST':
        aerial_id = request.GET.get("aerial")
        cid = request.GET.get("chassis")
        engine_id = request.GET.get("engine")
        tid = request.GET.get("transmission")
        electrical_id = request.GET.get("electrical")
    else:
        aerial_id = request.POST.get("aerial")
        cid = request.POST.get("chassis")
        engine_id = request.POST.get("engine")
        tid = request.POST.get("transmission")
        electrical_id = request.POST.get("electrical")

    print(aerial_id)
    print(cid)
    print(engine_id)
    print(tid)
    print(electrical_id)
    front_suspension_list = ct_configure_front_suspension(cid)
    context = {'front_suspension_list':front_suspension_list, 'aerial_id':aerial_id, 'cid':cid, 'engine_id':engine_id, 'tid':tid, 'electrical_id':electrical_id}
    return render(request, 'orders/ct_configurator_front_suspension.html', context)

def ct_config_rear_suspension_view(request):
    print("Inside config rear susp view")

    if request.method != 'POST':
        aerial_id = request.GET.get("aerial")
        cid = request.GET.get("chassis")
        engine_id = request.GET.get("engine")
        tid = request.GET.get("transmission")
        electrical_id = request.GET.get("electrical")
        front_suspension_id = request.GET.get("front_suspension")
    else:
        aerial_id = request.POST.get("aerial")
        cid = request.POST.get("chassis")
        engine_id = request.POST.get("engine")
        tid = request.POST.get("transmission")
        electrical_id = request.POST.get("electrical")
        front_suspension_id = request.POST.get("front_suspension")

    print(aerial_id)
    print(cid)
    print(engine_id)
    print(tid)
    print(electrical_id)
    print(front_suspension_id)
    rear_suspension_list = ct_configure_rear_suspension(cid)
    context = {'rear_suspension_list':rear_suspension_list, 'aerial_id':aerial_id, 'cid':cid, 'engine_id':engine_id, 'tid':tid, 'electrical_id':electrical_id, 'front_suspension_id':front_suspension_id}
    return render(request, 'orders/ct_configurator_rear_suspension.html', context)

def ct_config_pump_view(request):
    print("Inside config pump view")

    if request.method != 'POST':
        aerial_id = request.GET.get("aerial")
        cid = request.GET.get("chassis")
        engine_id = request.GET.get("engine")
        tid = request.GET.get("transmission")
        electrical_id = request.GET.get("electrical")
        front_suspension_id = request.GET.get("front_suspension")
        rear_suspension_id = request.GET.get("rear_suspension")
    else:
        aerial_id = request.POST.get("aerial")
        cid = request.POST.get("chassis")
        engine_id = request.POST.get("engine")
        tid = request.POST.get("transmission")
        electrical_id = request.POST.get("electrical")
        front_suspension_id = request.POST.get("front_suspension")
        rear_suspension_id = request.POST.get("rear_suspension")

    print(aerial_id)
    print(cid)
    print(engine_id)
    print(tid)
    print(electrical_id)
    print(front_suspension_id)
    print(rear_suspension_id)
    pump_list = ct_configure_pump(aerial_id)
    context = {'pump_list':pump_list, 'aerial_id':aerial_id, 'cid':cid, 'engine_id':engine_id, 'tid':tid, 'electrical_id':electrical_id, 'front_suspension_id':front_suspension_id, 'rear_suspension_id':rear_suspension_id}
    return render(request, 'orders/ct_configurator_pump.html', context)

def ct_config_quantity_view(request):
    print("Inside config quantity view")

    if request.method != 'POST':
        aerial_id = request.GET.get("aerial")
        cid = request.GET.get("chassis")
        engine_id = request.GET.get("engine")
        tid = request.GET.get("transmission")
        electrical_id = request.GET.get("electrical")
        front_suspension_id = request.GET.get("front_suspension")
        rear_suspension_id = request.GET.get("rear_suspension")
        pump_id = request.GET.get("pump")
    else:
        aerial_id = request.POST.get("aerial")
        cid = request.POST.get("chassis")
        engine_id = request.POST.get("engine")
        tid = request.POST.get("transmission")
        electrical_id = request.POST.get("electrical")
        front_suspension_id = request.POST.get("front_suspension")
        rear_suspension_id = request.POST.get("rear_suspension")
        pump_id = request.POST.get("pump")        
    
    print(aerial_id)
    print(cid)
    print(engine_id)
    print(tid)
    print(electrical_id)
    print(front_suspension_id)
    print(rear_suspension_id)
    print(pump_id)
    context = {'aerial_id':aerial_id, 'cid':cid, 'engine_id':engine_id, 'tid':tid, 'electrical_id':electrical_id, 'front_suspension_id':front_suspension_id, 'rear_suspension_id':rear_suspension_id, 'pump_id':pump_id}
    
    return render(request, 'orders/ct_configurator_quantity.html', context)

def ct_config_summary_view(request):
    print("Inside config summary view")
    aerial_id = request.POST.get("aerial")
    cid = request.POST.get("chassis")
    engine_id = request.POST.get("engine")
    tid = request.POST.get("transmission")
    electrical_id = request.POST.get("electrical")
    front_suspension_id = request.POST.get("front_suspension")
    rear_suspension_id = request.POST.get("rear_suspension")
    pump_id = request.POST.get("pump")
    quantity = int(request.POST.get("quantity"))

    order_detail_list = [aerial_id, cid, engine_id, tid, electrical_id, front_suspension_id, rear_suspension_id, pump_id, quantity]
    
    order_summary, subcost = ct_configure_summary(order_detail_list)

    order_detail_list.append(subcost)

    print(subcost)
    order_summary.append(quantity)
    order_summary.append(subcost)    
    order_summary.append(quantity*subcost)    

    #Add to session
    """if 'order_detail_list' in request.session:
        print ('Already in session')
        session_order_detail_list = request.session['order_detail_list']
        session_order_detail_list.append(order_detail_list)
        request.session['order_detail_list'] = session_order_detail_list
    else:
        print ('Not in session')
        session_order_detail_list = list()
        session_order_detail_list.append(order_detail_list)
        request.session['order_detail_list'] = session_order_detail_list
        print (request.session['order_detail_list'])

    if 'order_summary' in request.session:
        print ('Already in session')
        session_order_summary_list = request.session['order_summary']
        session_order_summary_list.append(order_summary)
        request.session['order_summary'] = session_order_summary_list
    else:
        print ('Not in session')
        session_order_summary_list = list()
        session_order_summary_list.append(order_summary)
        request.session['order_summary'] = session_order_summary_list
        print (request.session['order_summary'])    """    

    context = {'order_summary':order_summary,'aerial_id':aerial_id, 'cid':cid, 'engine_id':engine_id, 'tid':tid, 'electrical_id':electrical_id, 'front_suspension_id':front_suspension_id, 'rear_suspension_id':rear_suspension_id, 'pump_id':pump_id,'quantity':quantity}
    
    return render(request, 'orders/ct_configurator_summary.html', context)
    

def ct_cart_view(request):
    print("Inside cart view")
    aerial_id = request.POST.get("aerial")
    cid = request.POST.get("chassis")
    engine_id = request.POST.get("engine")
    tid = request.POST.get("transmission")
    electrical_id = request.POST.get("electrical")
    front_suspension_id = request.POST.get("front_suspension")
    rear_suspension_id = request.POST.get("rear_suspension")
    pump_id = request.POST.get("pump")
    try:
        quantity = int(request.POST.get("quantity"))
        order_detail_list = [aerial_id, cid, engine_id, tid, electrical_id, front_suspension_id, rear_suspension_id, pump_id, quantity]
        
        order_summary, subcost = ct_configure_summary(order_detail_list)

        order_detail_list.append(subcost)

        print(subcost)
        order_summary.append(quantity)
        order_summary.append(subcost)    
        order_summary.append(quantity*subcost)    

        #Add to session
        if 'order_detail_list' in request.session:
            print ('Already in session')
            session_order_detail_list = request.session['order_detail_list']
            session_order_detail_list.append(order_detail_list)
            request.session['order_detail_list'] = session_order_detail_list
        else:
            print ('Not in session')
            session_order_detail_list = list()
            session_order_detail_list.append(order_detail_list)
            request.session['order_detail_list'] = session_order_detail_list
            print (request.session['order_detail_list'])

        if 'order_summary' in request.session:
            print ('Already in session')
            session_order_summary_list = request.session['order_summary']
            session_order_summary_list.append(order_summary)
            request.session['order_summary'] = session_order_summary_list
        else:
            print ('Not in session')
            session_order_summary_list = list()
            session_order_summary_list.append(order_summary)
            request.session['order_summary'] = session_order_summary_list
            print (request.session['order_summary'])          
    except Exception as e:
        #raise
        pass

    try:
        session_order_summary_list = request.session['order_summary']
        session_order_detail_list =  request.session['order_detail_list']
        context = {'order_summary':session_order_summary_list,'order_detail_list':session_order_detail_list}
    except Exception as e:
        context =  {}

    return render(request, 'orders/ct_cart.html', context)  


def ct_cart_delete_view(request,item_id):
    print("Inside cart deltete view")
    try:
        session_order_summary_list = request.session['order_summary']
        session_order_detail_list =  request.session['order_detail_list']

        del session_order_summary_list[item_id]
        del session_order_detail_list[item_id]
        request.session['order_summary'] = session_order_summary_list
        request.session['order_detail_list'] = session_order_detail_list
        context = {'order_summary':session_order_summary_list,'order_detail_list':session_order_detail_list}
    except Exception as e:
        context =  {}
    return render(request, 'orders/ct_cart.html', context)  

def ct_placeorder_view(request):
    print("Inside cart placeorder view")
    order_id = create_order(request)
    place_order(order_id, request)
    del request.session['order_detail_list']
    del request.session['order_summary']
    return ct_orders_view(request)

def update_order_status_view(request, order_id,status):
    print("Inside update_order_status_view ")
    print(order_id,status);
    ad_update_order_status(order_id,status)
    return ad_orders_view(request)