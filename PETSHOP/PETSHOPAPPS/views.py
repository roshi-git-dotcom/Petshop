
from django.shortcuts import render,redirect
from . models import *




# Create your views here.
def reg(request):
    if request.method=="POST":
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        password=request.POST['password']
       
        print("success")
        usersave=register(firstname=fname,secondname=lname,email=email,password=password,role='user')
        usersave.save()
        return redirect('login')
    return render(request,"register.html")

def log(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']
        logdet=register.objects.get(email=email,password=password)
        print(logdet.id)
        request.session['session1']=logdet.id
        print(request.session['session1'])
        if logdet.role=="user":
            return redirect('loged')
        else:
            return redirect("loged")
    return render(request,"login.html")


def home(request):
    return render(request,"home.html")

def loged(request):
    return render(request,"loged.html")

def give(request):
    if request.method=="POST":
        name=request.POST['name']
        breed=request.POST['breed']
        age=request.POST['age']
        colour=request.POST['colour']
        number=request.POST['number']
        city=request.POST['city']
        district=request.POST['district']
        price=request.POST['price']
       
     
        
        if len(request.FILES)!=0:
            image=request.FILES['image']     
        usersave=givee(name=name,breed=breed,age=age,colour=colour,number=number,city=city,district=district,price=price,image=image)
        usersave.save()
        return redirect('adopt')
    

    return render(request,"give.html")
    

def adopt(request):
    c=givee.objects.all()
    context={'adop_list':c}
    return render(request,'adopt.html',context)


def adoptcus(request):
    if request.method=="POST":
        customername=request.POST['customername']
        address=request.POST['address']
        phone=request.POST['phone']
        usersave=adoptcuss(customername=customername,address=address,phone=phone)
        usersave.save()
        return redirect("adoptsuccess")
    return render(request,"adoptcus.html")

def vaccine(request):
    if request.method=="POST":
        vaccinedate=request.POST['vaccinedate']
        usersave=vacc(vaccinedate=vaccinedate)
        usersave.save()
        return redirect("loged")
    return render(request,"vaccine.html")


    
def deworm(request):
    if request.method=="POST":
        dewormdate=request.POST['dewormdate']
        usersave=dewo(dewormdate=dewormdate)
        usersave.save()
        return redirect("loged")
    return render(request,"deworm.html")
    

def vet(request):
    return render(request,"vet.html")

def aboutus(request):
    return render(request,"aboutus.html")



def deworm(request):
    return render(request,"deworm.html")

def surgeon(request):
    return render(request,"surgeon.html")

def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']
        usersave=contactt(name=name,email=email,subject=subject,message=message)
        usersave.save()
        return redirect("suces")
    return render(request,"contact.html")
    

def suces(request):
       return render(request,"suces.html")

def admin(request):
       log_det1=givee.objects.all()
       print(log_det1)
       return render(request,"admin.html",{'log':log_det1})

def adoptsuccess(request):
       return render(request,"adoptsuccess.html")





