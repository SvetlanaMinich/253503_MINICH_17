from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.db.models import F
import datetime
import pytz
import logging
from django.utils import timezone
import requests
import collections
from django.views import View
from .forms import UserForm, LoginForm
from .models import Master, Client, Specialization, CarModel, CarType, Service, Promocode, Part, Order, ClientMaster, QA, Job, Review, Article
import statistics

logging.basicConfig(level=logging.INFO, filename="my_log.log",filemode="a",format="%(asctime)s %(levelname)s %(message)s")


def main(request):
    services = Service.objects.all()
    
    url = "https://catfact.ninja/fact"
    response = requests.get(url).json()

    url2 = "https://dog.ceo/api/breeds/image/random"
    response2 = requests.get(url2).json()

    article = Article()
    article.text = response["fact"]
    article.img_url = response2["message"]
    article.title = f"Random Cat Fact - {datetime.datetime.now()}"
    try:
        article.save()
        logging.info(f"{article.title} is saved.")
    except:
        logging.warning(f"{article.title} cannot be saved.")

    article = Article.objects.order_by("created_at").last()

    # Получение часового пояса пользователя
    user_tz = timezone.get_current_timezone()

    # Получение текущей даты для пользователя и UTC
    utc_now = datetime.datetime.now(tz=pytz.utc)

    if request.method == "POST":
        price_from = int(request.POST.get('price_from'))
        price_to = int(request.POST.get('price_to'))
        if price_from > price_to:
            return HttpResponse("Filter is not correct.")
        services = services.filter(price__gte=price_from)
        services = services.filter(price__lte=price_to)
    return render(request, "main.html", {"services" : Service.objects.all(), "article" : article,
                                         "user_now": datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S'),
                                         "utc_now": utc_now.strftime('%d/%m/%Y %H:%M:%S'),})

def statisticsv(request):
    clients = Client.objects.all()

    sum = 0
    years = []
    for cl in clients:
        years.append(cl.age)
        sum += cl.age
    avg_age = sum/len(years)
    median_age = statistics.median(years)

    sum = 0
    sale_prices = []
    for cl in clients:
        sum += cl.result_price
        sale_prices.append(cl.result_price)
    avg_sale_price = sum/len(clients)
    median_sale_price = statistics.median(sale_prices)
    mode_sale_price = statistics.mode(sale_prices)

    alphabet_clients = Client.objects.order_by("name")
    whole_sale_price = sum

    orders = Order.objects.all()

    order_services = []
    for o in orders:
        order_services.append(o.service)
    service_counts = collections.Counter(order_services)
    most_common_service = max(service_counts, key=service_counts.get)


    return render(request, "statistics.html", {"average_age" : avg_age,
                                               "median_age" : median_age,
                                               "average_sale_price" : avg_sale_price,
                                               "median_sale_price" : median_sale_price,
                                               "mode_sale_price" : mode_sale_price,
                                               "sorted_clients" : alphabet_clients,
                                               "whole_sale_price" : whole_sale_price,
                                               "most_common_service" : most_common_service})

def about_company(request):
    return render(request, "about_company.html")

def contacts(request):
    return render(request, "contacts.html", {"masters" : Master.objects.all()})

#сортировка
def news(request):
    artcs = Article.objects.all()
    if request.method == "POST":
        val = request.POST.get("sort")
        if val == "date_new":
            artcs = Article.objects.order_by("created_at").reverse()
        elif val == "date_old":
            artcs = Article.objects.order_by("created_at")
        return render(request, "news.html", {"articles" : artcs})
    return render(request, "news.html", {"articles" : artcs})

def politics(request):
    return render(request, "politics.html")

#поиск
def promocodes(request):
    proms = Promocode.objects.all()
    sprom = None
    if request.method == "POST":
        tname = request.POST.get("search_term")
        if Promocode.objects.filter(name = tname).exists():
            sprom = Promocode.objects.filter(name = tname)
            return render(request, "promocodes.html", {"proms" : proms, "searched" : sprom})
    return render(request, "promocodes.html", {"proms" : proms, "searched" : sprom})

def qa(request):
    qas = QA.objects.all()
    return render(request, "qa.html", {"qas" : qas})

def reviews(request):
    if request.method == "POST":
        return render(request, "register.html", {'specializations' : Specialization.objects.all()})
    return render(request, "reviews.html", {"reviews" : Review.objects.order_by("date").reverse()})

def vacancies(request):
    return render(request, "vacancies.html", {"jobs" : Job.objects.all()})

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
                    logging.info(f"Master {searched_masters.first().name} added.")
                    return redirect(f'master/{searched_masters.first().pk}')
                else:
                    logging.warning(f"Master not found.")
                    return HttpResponseNotFound("No master with this phone number found")
            else:
                logging.warning(f"Master not found.")
                return HttpResponseNotFound("No master with this name found")
        else:
            searched_clients = Client.objects.filter(name = tname)
            if len(searched_clients) > 0:
                searched_clients = Client.objects.filter(phone_number = tphone_number)
                if len(searched_clients) == 1:
                    logging.info(f"Client {searched_clients.first().name} added.")
                    return redirect(f'client/{searched_clients.first().pk}')
                else:
                    logging.warning(f"Client not found.")
                    return HttpResponseNotFound("No client with this phone number found")
            else:
                logging.warning(f"Client not found.")
                return HttpResponseNotFound("No client with this name found")
    else:
        return render(request, "login.html")

def register(request):
    userform = UserForm()
    if request.method == "POST":
        userform = UserForm(request.POST)
        if userform.is_valid():
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
            return HttpResponse("Invalid data")
    else:
        return render(request, "register.html", {'specializations' : Specialization.objects.all(),
                                                 "form" : userform})
    
    

def mastersview(request, master_id):
    mast = Master.objects.get(id = master_id)
    clients_id = ClientMaster.objects.filter(master = mast)
    clients = set(cm.client for cm in clients_id)
    return render(request, "master.html", {"master": mast, "master_id" : master_id, "specs" : Specialization.objects.all(),
                                           "orders" : Order.objects.filter(master = mast),
                                           "clients" : clients})

def clientsview(request, client_id):
    client = Client.objects.get(id = client_id)
    return render(request, "client.html", {"client": client, 
                                           "client_id" : client_id, 
                                           "car_models" : CarModel.objects.all(), 
                                           "car_types" : CarType.objects.all(),
                                           "proms" : Promocode.objects.all(),
                                           "reviews" : Review.objects.filter(user = client).order_by("date").reverse()})


def editmaster(request, master_id):
    mast = Master.objects.get(id = master_id)
    if request.method == "POST":
        tname = request.POST.get("name")
        tage = request.POST.get("age")
        tphone_number = "+375 (" + request.POST.get("phone_code") + ") " + request.POST.get("phone_number")
        tspecialization = request.POST.get("specialization")
        tphoto = request.POST.get("photo")
        Master.objects.filter(id = master_id).update(name=tname,age=tage,phone_number=tphone_number,specialization=tspecialization,img_url=tphoto)
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
        master = Master.objects.get(id = order.master.pk)
        client = Client.objects.get(id = client_id)
        new_clientmaster = ClientMaster()
        new_clientmaster.client = client
        new_clientmaster.master = master
        new_clientmaster.save()
        return redirect('client',client_id = client.pk)
    else:
        return render(request,"createorder.html", {"client_id" : client_id, 
                                                   "masters" : Master.objects.all(), 
                                                   "services" : Service.objects.all(), 
                                                   "parts" : Part.objects.filter(car_model = client.car_model)})
    

def createreview(request, client_id):
    user = Client.objects.get(id = client_id)
    if request.method == "POST":
        ttext = request.POST.get("text")
        new_review = Review()
        new_review.user = user
        new_review.text = ttext
        new_review.save()
        return redirect('client',client_id = user.pk)
    else:
        return render(request,"createreview.html")
    
def editreview(request, client_id, review_id):
    user = Client.objects.get(id = client_id)
    review = Review.objects.get(id = review_id)
    if request.method == "POST":
        ttext = request.POST.get("text")
        Review.objects.filter(id = review_id).update(text = ttext)
        return redirect('client',client_id = user.pk)
    else:
        return render(request,"editreview.html", {"review" : review})
    
def deletereview(request, client_id, review_id):
    user = Client.objects.get(id = client_id)
    review = Review.objects.get(id = review_id)
    if request.method == "POST":
        review.delete()
        return redirect('client',client_id = user.pk)
    else:
        return render(request,"deletereview.html", {"review" : review})
    

    