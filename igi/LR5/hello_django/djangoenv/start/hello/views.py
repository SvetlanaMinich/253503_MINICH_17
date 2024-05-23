from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.db.models import F
import datetime
from django.views import View
from .forms import UserForm, LoginForm
from .models import Master, Client, Specialization, CarModel, CarType, Service, Promocode, Part, Order

def main(request):
    return render(request, "main.html")

def about_company(request):
    return render(request, "about_company.html")

def contacts(request):
    return render(request, "contacts.html")

def news(request):
    return render(request, "news.html")

def politics(request):
    return render(request, "politics.html")

def promocodes(request):
    return render(request, "promocodes.html")

def qa(request):
    return render(request, "qa.html")

def reviews(request):
    return render(request, "reviews.html")

def vacancies(request):
    return render(request, "vacancies.html")

def login(request):
    if request.method == "POST":
        tname = request.POST.get("name")
        tphone_number = "+375 (" + request.POST.get("phone_code") + ") " + request.POST.get("phone_number")
        usertype = request.POST.get("user_type")
        if usertype == "master":
            searched_masters = Master.objects.filter(name=tname)
            if len(searched_masters) > 0:
                searched_masters = searched_masters.filter(phone_number = tphone_number)
                if len(searched_masters) == 1:
                    return redirect(f'master/{searched_masters.first().pk}')
                else:
                    return HttpResponseNotFound("No master with this phone number found")
            else:
                return HttpResponseNotFound("No master with this name found")
        else:
            searched_clients = Client.objects.filter(name = tname)
            if len(searched_clients) > 0:
                searched_clients = Client.objects.filter(phone_number = tphone_number)
                if len(searched_clients) == 1:
                    return redirect(f'client/{searched_clients.first().pk}')
                else:
                    return HttpResponseNotFound("No client with this phone number found")
            else:
                return HttpResponseNotFound("No client with this name found")
    else:
        return render(request, "login.html")

def register(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        tphone_number = "+375 (" + request.POST.get("phone_code") + ") " + request.POST.get("phone_number")
        usertype = request.POST.get("user_type")
        if usertype == "master":
            if Master.objects.filter(phone_number = tphone_number).exists():
                return HttpResponse("Master with this phone_number already exists.")
            new_master = Master()
            new_master.name = name
            new_master.age = age
            new_master.phone_number = tphone_number
            new_master.order_count = 0
            new_master.specialization = Specialization.objects.first()
            new_master.save()
            return redirect(f'master/{new_master.pk}')
        else:
            if Client.objects.filter(phone_number = tphone_number).exists():
                return HttpResponse("Client with this phone_number already exists.")
            new_client = Client()
            new_client.name = name
            new_client.age = age
            new_client.phone_number = tphone_number
            new_client.result_price = 0
            new_client.car_model = CarModel.objects.first()
            new_client.car_type = CarType.objects.first()
            new_client.save()
            return redirect(f'client/{new_client.pk}')
    else:
        userForm = UserForm()
        return render(request, "register.html", {'specializations' : Specialization.objects.all()})
    
    

def mastersview(request, master_id):
    mast = Master.objects.get(id = master_id)
    return render(request, "master.html", {"master": mast, "master_id" : master_id, "specs" : Specialization.objects.all(),
                                           "orders" : Order.objects.filter(master = mast)})

def clientsview(request, client_id):
    client = Client.objects.get(id = client_id)
    return render(request, "client.html", {"client": client, "client_id" : client_id, "car_models" : CarModel.objects.all(), "car_types" : CarType.objects.all()})


def editmaster(request, master_id):
    mast = Master.objects.get(id = master_id)
    if request.method == "POST":
        tname = request.POST.get("name")
        tage = request.POST.get("age")
        tphone_number = "+375 (" + request.POST.get("phone_code") + ") " + request.POST.get("phone_number")
        tspecialization = request.POST.get("specialization")
        Master.objects.filter(id = master_id).update(name=tname,age=tage,phone_number=tphone_number,specialization=tspecialization)
        mast = Master.objects.get(id = master_id)
        return redirect('master',master_id=master_id)
    return render(request, "editmaster.html", {"master": mast, "specs" : Specialization.objects.all()})

def editclient(request, client_id):
    client = Client.objects.get(id = client_id)
    if request.method == "POST":
        tname = request.POST.get("name")
        tage = request.POST.get("age")
        tphone_number = "+375 (" + request.POST.get("phone_code") + ") " + request.POST.get("phone_number")
        tmodel = request.POST.get("model_car")
        ttype = request.POST.get("type_car")
        Client.objects.filter(id = client_id).update(name=tname, age=tage, phone_number=tphone_number, car_model=tmodel, car_type=ttype)
        client = Client.objects.get(id = client_id)
        return redirect('client',client_id = client_id)
    else:
        return render(request, "editclient.html", {"client": client, "car_models" : CarModel.objects.all(), "car_types" : CarType.objects.all()})
    

def createorder(request, client_id):
    client = Client.objects.get(id = client_id)
    if request.method == "POST":
        order = Order()
        order.master = Master.objects.get(id = request.POST.get("master"))
        order.client = client
        order.ordering_time = datetime.datetime.now()
        order.service = Service.objects.get(id = request.POST.get("service"))
        selected_parts = Part.objects.filter(id__in=request.POST.getlist("parts"))
        prom = None
        if request.POST.get("promocode"):
            try:
                prom = Promocode.objects.get(name = request.POST.get("promocode"))
            except:
                prom = None
        if prom is None:
            order.whole_price = order.CountPrice(parts=selected_parts)
        else:
            order.whole_price = order.CountPrice(prom,selected_parts)
        order.save()
        Client.objects.filter(id = client_id).update(result_price=F('result_price') + order.whole_price)
        Master.objects.filter(id = order.master.pk).update(order_count=F('order_count') + 1)
        client = Client.objects.get(id = client_id)
        return redirect('client',client_id = client.pk)
    else:
        return render(request,"createorder.html", {"client_id" : client_id, 
                                                   "masters" : Master.objects.all(), 
                                                   "services" : Service.objects.all(), 
                                                   "parts" : Part.objects.filter(car_model = client.car_model)})