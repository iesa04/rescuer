from django.shortcuts import render
from users.forms import AdminForm
from .data import validate_data, validate_signup, validate_username, save_customer, retrieve_fdid,validate_fdid_zip
from django.http import HttpResponse
from home import config

def login_view(request):
	return render(request, 'login/login.html',{})

def landing_page_view(request):
    user_type_code = request.session['user_type_code']
    if user_type_code == 'AD':
        return render(request, 'login/landing_page.html',{})
    elif user_type_code == 'CT':
        return render(request, 'login/customer_landing_page.html',{}) 

def validate_login_view(request):
    form = AdminForm(request.POST or None)
    print("validate_login_view")

    query_array = []
    error_code = ""

    if request.method == 'POST':
        query_array.append(request.POST.get("username"))
        query_array.append(request.POST.get("password"))
        try:
            user = validate_data(query_array)
        except:
            return render(request, 'login/login.html', {'error_message':config.INAVLID_LOGIN})
    context = {
        'form':form,
    }
    
    request.session['username'] = user.username
    request.session['user_type_code'] = user.user_type_code
    if user.user_type_code == 'AD':
    	return render(request, 'login/landing_page.html',context)
    elif user.user_type_code == 'CT':
        request.session['fdid'] = retrieve_fdid(user.username)
        return render(request, 'login/customer_landing_page.html',context) 
    #return render(request, 'login/landing_page.html',context)

def signup_login_view(request):
    return render(request, 'login/signup.html',{})   	

def validate_signup_view(request):
    print("Validating:")

    query_array = []
    error_code = ""

    if request.method == 'POST':
        query_array.append(request.POST.get("fdid"))
        query_array.append(request.POST.get("zip"))
        query_array.append(request.POST.get("username"))
        query_array.append(request.POST.get("password1"))
        query_array.append(request.POST.get("password2"))

        try:
            validate_username(query_array[2])
        except Exception as error:
            return render(request, 'login/signup.html', {'error_message':error})
        
        if query_array[-1] != query_array[-2]:
            return render(request, 'login/signup.html', {'error_message':config.INVALID_PASSWORD})

        try:
            validate_fdid_zip(query_array[0])
        except Exception as error :
            return render(request, 'login/signup.html', {'error_message':error})

        try:
            dept_info = validate_signup(query_array)
            print(dept_info)
            name = dept_info[1]
            save_customer(query_array, name)
            context = {
                'dept_info':dept_info
            }
            return render(request, 'login/login.html',context)
        except:            
            return render(request, 'login/signup.html', {'error_message':config.INVALID_FDID_ZIP})

    
    
    
    """
    elif user.user_type_code == 'CT':
        return render(request, 'login/customer_landing_page.html',context)
        """

def isLoggedIn(request):
    try:
        if(request.session['username'] != "") :
            return True;
        else :
            return False;
    except :
        return False;

def logout_view(request):
    try:
        # Delete a session value
        del request.session['username']
        del request.session['user_type_code']
        del request.session['order_detail_list']
        del request.session['order_summary']
        del request.session['fdid']
    except:
        pass
    return render(request, 'home/home.html',{})