"""
URL configuration for rescuer project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from chassis.views import chassis_view, chassis_create_view,chassis_update_view,chassis_get_view,chassis_delete_view,ct_chassis_view, ct_chassis_get_view,chassis_engine_compatibility_view,chassis_transmission_compatibility_view,chassis_electricals_compatibility_view,chassis_suspension_compatibility_view,chassis_aerials_compatibility_view,chassis_save_aerials_compatibility_view,update_chassis_status_view
from suspension.views import suspension_view, suspension_create_view, suspension_get_view, suspension_update_view, suspension_delete_view,get_fa_compatibility_view,modify_fa_compatibility_view,get_ra_compatibility_view,modify_ra_compatibility_view
from home.views import home_view
from login.views import login_view, validate_login_view, signup_login_view, validate_signup_view,logout_view,landing_page_view
from users.views import user_types_view, admin_view, customer_view, supplier_view, admin_create_view, admin_delete_view
from engine.views import engine_view, engine_create_view, engine_get_view, engine_delete_view, engine_update_view, engine_compatiblity_view,modify_compatibility_view
from transmission.views import transmission_view, transmission_create_view, transmission_get_view, transmission_delete_view, transmission_update_view, transmission_compatiblity_view, transmission_modify_compatibility_view
from pump.views import pump_view, pump_create_view, pump_get_view, pump_delete_view, pump_update_view, pump_compatiblity_view, pump_modify_compatibility_view
from electricalsystem.views import electrical_system_view, electrical_system_create_view, electrical_system_get_view, electrical_system_delete_view, electrical_system_update_view, electrical_compatiblity_view, electrical_modify_compatibility_view
from aerials.views import aerial_view, aerial_create_view, aerial_get_view, aerial_delete_view, aerial_update_view,ct_aerial_view, ct_aerial_get_view, aerial_compatiblity_view, aerial_modify_compatibility_view,save_pump_compatiblity_view,aerial_modify_chassis_compatibility_view,aerial_save_compatibility_view,update_aerial_status_view
from orders.views import ct_orders_view, ct_order_detail_view, ct_new_order_view, ct_config_aerial_view,ct_config_chassis_view, ct_config_engine_view, ct_config_transmission_view, ct_config_electrical_system_view,ct_config_front_suspension_view, ct_config_rear_suspension_view, ct_config_pump_view, ct_config_quantity_view, ct_config_summary_view,ct_cart_view,ct_cart_delete_view, ct_placeorder_view,ad_orders_view,update_order_status_view

urlpatterns = [
    path('rescuer', home_view),
    path('login/',login_view),
    path('logout/',logout_view),    
    path('login/validatelogin',validate_login_view),
    path('login/validatesignup',validate_signup_view),
    path('login/signup',signup_login_view),
    path('login/home/',landing_page_view),

    path('chassis/', chassis_view),
    path('chassis/create', chassis_create_view),
    path('chassis/update', chassis_update_view),
    path('chassis/get/<int:chassis_id>', chassis_get_view),
    path('chassis/delete/<int:my_id>', chassis_delete_view),
    path('chassis/getenginecompatibility',chassis_engine_compatibility_view),
    path('chassis/gettransmissioncompatibility',chassis_transmission_compatibility_view),
    path('chassis/getelectricalscompatibility',chassis_electricals_compatibility_view),  
    path('chassis/getsuspensioncompatibility',chassis_suspension_compatibility_view),
    path('chassis/getaerialscompatibility',chassis_aerials_compatibility_view),
    path('chassis/saveaerialscompatibility',chassis_save_aerials_compatibility_view),
    path('chassis/updatechassisstatus/<int:cid>/<str:status>',update_chassis_status_view),

    path('admin/', admin.site.urls),

    path('engine/',engine_view),
    path('engine/create', engine_create_view),
    path('engine/get/<int:my_id>', engine_get_view),
    path('engine/update', engine_update_view),
    path('engine/delete/<int:my_id>', engine_delete_view),
    path('engine/modifycompatibility/<int:engine_id>', engine_compatiblity_view),
    path('engine/modifycompatibility', modify_compatibility_view),

    path('suspension/', suspension_view),
    path('suspension/create', suspension_create_view),
    path('suspension/get/<int:suspension_id>', suspension_get_view),
    path('suspension/update', suspension_update_view),
    path('suspension/delete/<int:suspension_id>', suspension_delete_view),
    path('suspension/getfacompatibility/<int:suspension_id>',get_fa_compatibility_view),
    path('suspension/modifyfacompatibility',modify_fa_compatibility_view),
    path('suspension/getracompatibility/<int:suspension_id>',get_ra_compatibility_view),
    path('suspension/modifyracompatibility',modify_ra_compatibility_view),

    path('transmission/',transmission_view),
    path('transmission/create', transmission_create_view),
    path('transmission/get/<int:my_id>', transmission_get_view),
    path('transmission/update', transmission_update_view),
    path('transmission/delete/<int:my_id>', transmission_delete_view),
    path('transmission/modifycompatibility/<int:tid>', transmission_compatiblity_view),
    path('transmission/modifycompatibility', transmission_modify_compatibility_view),

    path('pump/',pump_view),
    path('pump/create', pump_create_view),
    path('pump/get/<int:my_id>', pump_get_view),
    path('pump/update', pump_update_view),
    path('pump/delete/<int:my_id>', pump_delete_view),
    path('pump/modifycompatibility/<int:pump_id>', pump_compatiblity_view),
    path('pump/modifycompatibility', pump_modify_compatibility_view),

    path('electricalsystem/',electrical_system_view),
    path('electricalsystem/create', electrical_system_create_view),
    path('electricalsystem/get/<int:my_id>', electrical_system_get_view),
    path('electricalsystem/update', electrical_system_update_view),
    path('electricalsystem/delete/<int:my_id>', electrical_system_delete_view),
    path('electricalsystem/modifycompatibility/<int:electrical_id>', electrical_compatiblity_view),
    path('electricalsystem/modifycompatibility', electrical_modify_compatibility_view),

    path('aerials/',aerial_view),
    path('aerials/create', aerial_create_view),
    path('aerials/get/<int:aerial_id>', aerial_get_view),
    path('aerials/update', aerial_update_view),
    path('aerials/delete/<int:aerial_id>', aerial_delete_view),
    path('aerials/modifycompatibility/<int:aerial_id>', aerial_compatiblity_view),
    path('aerials/modifycompatibility', aerial_modify_compatibility_view),
    path('aerials/savepumpcompatibility',save_pump_compatiblity_view),
    path('aerials/modifychassiscompatibility/<int:aerial_id>',aerial_modify_chassis_compatibility_view),
    path('aerials/savechassiscompatibility',aerial_save_compatibility_view),
    path('aerials/updateaerialstatus/<int:aerial_id>/<str:status>',update_aerial_status_view),

    path('users/', user_types_view),
    path('users/AD', admin_view),
    path('users/delete/<int:user_id>', admin_delete_view),
    path('users/CT', customer_view),
    path('users/SU', supplier_view),
    path('users/create', admin_create_view),

    path('CT/chassis/', ct_chassis_view),
    path('CT/aerials/', ct_aerial_view),
    path('CT/aerials/get/<int:aerial_class>', ct_aerial_get_view),

    path('CT/get/<str:chassis>', ct_chassis_get_view),
    path('CT/orders/', ct_orders_view),
    path('CT/orders/detail/<int:order_id>', ct_order_detail_view),
    path('CT/orders/new', ct_new_order_view),
    path('CT/orders/new/aerial', ct_config_aerial_view),
    path('CT/orders/new/chassis', ct_config_chassis_view),
    path('CT/orders/new/engine', ct_config_engine_view),
    path('CT/orders/new/transmission', ct_config_transmission_view),
    path('CT/orders/new/electrical_system', ct_config_electrical_system_view),
    path('CT/orders/new/front_suspension', ct_config_front_suspension_view),
    path('CT/orders/new/rear_suspension', ct_config_rear_suspension_view),
    path('CT/orders/new/pump', ct_config_pump_view),
    path('CT/orders/new/quantity', ct_config_quantity_view),
    path('CT/orders/new/summary', ct_config_summary_view),
    path('CT/orders/cart', ct_cart_view),
    path('CT/orders/cart/delete/<int:item_id>', ct_cart_delete_view),
    path('CT/orders/cart/placeorder', ct_placeorder_view),

    path('AD/orders/', ad_orders_view), 
    path('AD/orders/updateorderstatus/<int:order_id>/<str:status>',update_order_status_view),
]
