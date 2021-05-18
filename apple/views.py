from django.shortcuts import render,redirect
from .models import branches , bikes,orders
import datetime
from django.contrib import messages
def index(request):
    brs = branches.objects.all()
    bks = bikes.objects.all()
    city= branches.objects.values('branch_city').distinct()
    bkmdls=bikes.objects.values('bike_model').distinct()
    items, item_model = [], []
    for bk in bks:
        if bk.bike_model not in item_model:
            items.append(bk)
            item_model.append(bk.bike_model)
    print(items)
    return render(request, 'index.html', {'branches':brs , 'bikes': items , 'cities' : city, 'models' : bkmdls})


def bikespage(request):
    if request.method == 'POST':
        cities = branches.objects.values('branch_city').distinct()
        models = bikes.objects.values('bike_model').distinct()
        city=request.POST['city']
        bike_model =request.POST['bike_model']
        temp=branches.objects.filter(branch_city=city)
        lst=[]
        for tem in temp:
            q= bikes.objects.filter(bike_model = bike_model , branch_id= tem, bike_availability=1 )
            print(q[0].branch_id.branch_city)
            lst.append(q)
        return render(request, 'bikes.html', {'cities' : cities , 'models' : models , 'bikes_list': lst})
    else:
        cities = branches.objects.values('branch_city').distinct()
        models = bikes.objects.values('bike_model').distinct()
        temp=bikes.objects.filter(bike_availability=1)
        lst=[]
        lst.append(temp)
        return render(request, 'bikes.html', {'cities' : cities , 'models' : models , 'bikes_list': lst})


def book (request):
    if request.method== 'POST':
        bike_id = request.POST['id']
        q = bikes.objects.get(bike_id=bike_id)
        if q.bike_availability == 0 :
            order = orders.objects.get(bike_id__bike_id=bike_id)
            return render(request, 'bike.html', {'bike': q,'message':'','order': order})
        else:
            return render(request, 'bike.html', {'bike': q, 'message': ''})
def book_process(request,id):
    bike=bikes.objects.get(bike_id=id)
    bike.bike_availability = 0
    bike.save()
    q=orders(bike_id = bikes.objects.get(bike_id=id),user=request.user,take_time=datetime.datetime.now(),give_time=datetime.datetime.now(),cost=bike.bike_cost)
    q.save()
    return render(request,'bike.html',{'bike': bike ,'message':'sucessfully booked','order':q })
def return_process(request,id,id1):
    qb=bikes.objects.get(bike_id=id)
    q=orders.objects.get(order_id=id1)
    q.give_time=datetime.datetime.now()
    q.save()
    t1=str(q.give_time)[:19]
    t2=str(q.take_time)[:19]
    datetimeformat='%Y-%m-%d %H:%M:%S'
    time=datetime.datetime.strptime(t1,datetimeformat)- datetime.datetime.strptime(t2,datetimeformat)
    day=time.days
    day=day+1
    cst=day*qb.bike_cost
    q.cost=cst
    q.save()
    st='amount to be paid is '+ str(cst)
    qb.bike_availability=1
    qb.save()
    return render(request, 'bike.html', {'bike': qb,'message':st})
def cart(request):
    q=orders.objects.filter(user=request.user)
    return render(request,'cart.html',{'orderlist':q})
