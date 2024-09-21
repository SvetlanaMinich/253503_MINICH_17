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
from .forms import UserForm
from .models import *
import statistics

logging.basicConfig(level=logging.INFO, filename="my_log.log",filemode="a",format="%(asctime)s %(levelname)s %(message)s")


# python manage.py runserver
# python manage.py makemigrations
# python manage.py migrate


def main(request):
    partners = PartnerCompany.objects.all()
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
                                         "utc_now": utc_now.strftime('%d/%m/%Y %H:%M:%S'),
                                         "partners" : partners})


def statisticsv(request):
    clients = Client.objects.all()

    sum = 0
    years = []
    for cl in clients:
        age = datetime.date.today().year - cl.age.year
        years.append(age)
        sum += age
    avg_age = round(sum/len(years), 2)
    median_age = statistics.median(years)

    sum = 0
    sale_prices = []
    for cl in clients:
        sum += cl.result_price
        sale_prices.append(cl.result_price)
    avg_sale_price = round(sum/len(clients), 2)
    median_sale_price = statistics.median(sale_prices)
    mode_sale_price = statistics.mode(sale_prices)

    alphabet_clients = Client.objects.order_by("name")
    whole_sale_price = round(sum, 2)

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
    company_info = CompanyInfo.objects.first()
    return render(request, "about_company.html", {'company': company_info})

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
    userform = UserForm()
    if request.method == "POST":
        userform = UserForm(request.POST)
        if not userform.is_valid():
            tlogin = request.POST.get("login")
            tpassword = request.POST.get("password")
            usertype = request.POST.get("user_type")
            
            if usertype == "master":
                searched_masters = MasterCredentials.objects.filter(login = tlogin)
                if len(searched_masters) > 0:
                    searched_masters = searched_masters.filter(password = tpassword)
                    if len(searched_masters) == 1:
                        logging.info(f"Master {searched_masters.first().master.name} added.")
                        return redirect(f'master/{searched_masters.first().master.pk}')
                    else:
                        logging.warning(f"Master not found.")
                        return HttpResponseNotFound("Invalid password")
                else:
                    logging.warning(f"Master not found.")
                    return HttpResponseNotFound("No master with this login found")
            else:
                searched_clients = ClientCredentials.objects.filter(login = tlogin)
                if len(searched_clients) > 0:
                    searched_clients = searched_clients.filter(password = tpassword)
                    if len(searched_clients) == 1:
                        logging.info(f"Client {searched_clients.first().client.name} added.")
                        return redirect(f'client/{searched_clients.first().client.pk}')
                    else:
                        logging.warning(f"Client not found.")
                        return HttpResponseNotFound("Invalid password")
                else:
                    logging.warning(f"Client not found.")
                    return HttpResponseNotFound("No client with this login found")
        else:
            return HttpResponse("Invalid data")
    else:
        return render(request, "login.html", { "form" : userform })


def CheckAge(age):
    min_birthday = datetime.date.today() - datetime.timedelta(days=365*18)
    if min_birthday < age:
        return False
    return True


def register(request):
    userform = UserForm()
    if request.method == "POST":
        userform = UserForm(request.POST)
        if userform.is_valid():
            tpassword = request.POST.get("password")
            tlogin = request.POST.get("login")
            name = request.POST.get("name")
            age = request.POST.get("date_of_birth")
            tphone_number = "+375 (" + request.POST.get("phone_code") + ") " + request.POST.get("phone_number")
            usertype = request.POST.get("user_type")

            dob = datetime.datetime.strptime(age, "%Y-%m-%d").date()

            is_adult = CheckAge(dob)
            if is_adult == False:
                return HttpResponse("You must be 18+ y/o.")
            
            if usertype == "master":
                if MasterCredentials.objects.filter(login = tlogin).exists():
                    return HttpResponse("Master with this login already exists.")
                new_master = Master()
                new_master.name = name
                new_master.age = age
                new_master.phone_number = tphone_number
                new_master.order_count = 0
                new_master.specialization = Specialization.objects.first()
                new_master.save()
                new_master_cred = MasterCredentials()
                new_master_cred.master = new_master
                new_master_cred.login = tlogin
                new_master_cred.password = tpassword
                new_master_cred.save()
                return redirect(f'master/{new_master.pk}')
            else:
                if ClientCredentials.objects.filter(login = tlogin).exists():
                    return HttpResponse("Client with this login already exists.")
                new_client = Client()
                new_client.name = name
                new_client.age = age
                new_client.phone_number = tphone_number
                new_client.result_price = 0
                new_client.car_model = CarModel.objects.first()
                new_client.car_type = CarType.objects.first()
                new_client.save()
                new_cl_creds = ClientCredentials()
                new_cl_creds.client = new_client
                new_cl_creds.login = tlogin
                new_cl_creds.password = tpassword
                new_cl_creds.save()
                return redirect(f'client/{new_client.pk}')
        else:
            return HttpResponse("Invalid data")
    else:
        return render(request, "register.html", {'specializations' : Specialization.objects.all(),
                                                 "form" : userform})
    

def article_detail(request, article_id):
    article = Article.objects.get(id=article_id)
    return render(request, 'article_detail.html', {'article': article})


def service_info_not(request, service_id):
    service = Service.objects.get(id=service_id)
    return render(request, 'service_info_not.html', {'service': service})


def service_info_registered(request, client_id, service_id):
    client = Client.objects.get(id=client_id)
    service = Service.objects.get(id=service_id)

    if request.method == 'POST':
        # Логика для добавления услуги в корзину
        specialization = None if not Specialization.objects.filter(name = service.name) else Specialization.objects.filter(name = service.name).first()
        master = Master.objects.all().first() if not Master.objects.filter(specialization=specialization) else Master.objects.filter(specialization=specialization).first()
        cart_item = CartItem(user=client, master=master, service=service, quantity=1)  # Пример, если есть модель CartItem
        cart_item.save()
        return redirect('createorder',client_id=client_id)

    return render(request, 'service_info_registered.html', {'service': service,
                                                            'client': client})


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
    services = Service.objects.all()
    return render(request,"createorder.html", {"client_id" : client_id, 
                                               "services" : Service.objects.all()})
    

def cartview(request, client_id):
    client = Client.objects.get(id=client_id)
    
    if request.method == 'POST':
        if 'remove' in request.POST:
            item_id = request.POST.get('item_id')
            try:
                cart_it = CartItem.objects.get(id=item_id, user=client)
                cart_it.delete()
            except CartItem.DoesNotExist:
                # Optionally log this error or handle it as needed
                pass
            cart_items = CartItem.objects.filter(user=client)
            total_price = sum(item.total_price() for item in cart_items)
            return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price,
                                                 "client_id": client_id})

    cart_items = CartItem.objects.filter(user=client)
    total_price = sum(item.total_price() for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price,
                                         "client_id": client_id})


def createreview(request, client_id):
    user = Client.objects.get(id = client_id)
    if request.method == "POST":
        ttext = request.POST.get("text")
        trating = request.POST.get("rating")
        new_review = Review()
        new_review.user = user
        new_review.text = ttext
        new_review.rating = int(trating)
        new_review.save()
        return redirect('client',client_id = user.pk)
    else:
        return render(request,"createreview.html")
    

def editreview(request, client_id, review_id):
    user = Client.objects.get(id = client_id)
    review = Review.objects.get(id = review_id)
    if request.method == "POST":
        ttext = request.POST.get("text")
        trating = request.POST.get("rating")

        Review.objects.filter(id = review_id).update(text = ttext)
        Review.objects.filter(id = review_id).update(rating = int(trating))
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
    

def cart(request):
    if request.method == "POST":
        return render(request, "register.html", {'specializations' : Specialization.objects.all()})
    return render(request, "cart.html")
    cart_items = CartItem.objects.filter(user=request.user)

    if request.method == "POST":
        action = request.POST.get("action")
        service_id = request.POST.get("service_id")
        quantity = int(request.POST.get("quantity", 1))
        service = Service.objects.get(id=service_id)

        if action == "add":
            # Добавление товара в корзину
            cart_item, created = CartItem.objects.get_or_create(user=request.user, service=service)
            if not created:
                cart_item.quantity += quantity
            cart_item.save()

        elif action == "remove":
            # Удаление товара из корзины
            CartItem.objects.filter(user=request.user, service=service).delete()

        elif action == "increase":
            # Увеличить количество товара
            cart_item = CartItem.objects.get(user=request.user, service=service)
            cart_item.quantity += 1
            cart_item.save()

        elif action == "decrease":
            # Уменьшить количество товара
            cart_item = CartItem.objects.get(user=request.user, service=service)
            if cart_item.quantity > 1:
                cart_item.quantity -= 1
                cart_item.save()

    total_cost = sum(item.total_price() for item in cart_items)

    return render(request, 'cart.html', {'cart_items': cart_items, 'total_cost': total_cost})