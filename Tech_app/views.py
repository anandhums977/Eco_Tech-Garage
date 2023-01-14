from django.shortcuts import render,redirect
from .models import Service, ServiceStatusDetail,registerDB,ServiceBooking,Teams,Contact
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import User
from .decorators import login_required
# Create your views here.

def Login(request):
    if 'register'in request.POST:
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['paswd']
        confirm_password = request.POST['con_paswd']
        if password == confirm_password:
            obj=registerDB(name=name,email=email,phone=phone,password=password)
            obj.save()
            messages.success(request," user register successfully")
            return redirect(Login)
        else:
            messages.warning(request," password dosenot match!")
    if 'login' in request.POST:
        user_name=request.POST['name']
        password_n=request.POST['password']
        user=registerDB.objects.filter(name=user_name,password=password_n)
        # print(user[0])
        if user.exists():
            user_data=list(user.values())
            print(user_data)
            request.session['userid'] = user[0].id
            request.session['username'] = user[0].name
            messages.success(request,"login successfully")
            return redirect(indexpage)
            
        else:

            messages.error(request,"sorry invalid user !")
    return render(request,'login.html')


def indexpage(request):
    serv = Service.objects.all()
    return render(request,'index.html',{'serv':serv})


def Services(request):
    
    name = Service.objects.all()

    product = Service.objects.filter(service=id)
    
   
    return render(request,'service.html',{'name':name,'product':product,})
  



def Team(request):
    obj = Teams.objects.all()
   
    return render(request,'team.html',{"obj":obj})



def About(request):
   
    return render(request,"about.html")



def Respond(request):
    return render(request,'response.html')


def Contact(request):
    
    if request.session['userid']:

        if 'booking'in request.POST:

            uname = request.POST['m_name']
            email = request.POST['email_n']
            phone = request.POST['phone_n']
            date = request.POST['date']
            message = request.POST['msg_n']
            user = request.session['userid']
            service_id = request.GET.get('serv_id')
          
            obj = ServiceBooking(Aname=uname,email=email,phone=phone,date_for_service=date,message=message,user_id=user,service_id=service_id).save()
            
            last_insert_id=(ServiceBooking.objects.last()).id

            sub=ServiceStatusDetail(booking_id=last_insert_id).save()

            print(last_insert_id)
            messages.success(request,"book successfully")
            return redirect(Respond)
        
    else:     
        if not request.session['userid']:
            return redirect(login) 
  

    return render(request,"booking.html")




# @login_required
def Single_Service(request, serv_id):


    single_service = Service.objects.filter(id=serv_id)
    

    # print(request.session['username'])

    # service= ServiceBooking.objects.filter(id = serv_id)

 
    return render(request,'single_service.html',{'single_service':single_service,'serv_id':serv_id})
 


def Logout(request):
    if request.session:
        request.session.clear()

    return redirect('/login/')
    
    



def status(request):
    data= ServiceStatusDetail.objects.select_related('booking__service').filter(booking__user=request.session['userid'])
   
    
   
        

    return render(request,'status.html',{'datas':data})






def contact_us(request):
    if 'contact'in request.POST:
        names = request.POST['c_name']
        email = request.POST['c_email']
        message = request.POST['c_message']
        obj=Contact(contactname=names,email=email,msg=message)
        obj.save()
        # messages.success(request,"message send successfully")
   


    return render(request,'contact.html')