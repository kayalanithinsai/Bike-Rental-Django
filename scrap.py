from apple.models import bikes,branches
c=bikes.objects.get(bike_id=28)
for i in range(57,85):
    if(i==76 or i==78):
        continue
    q = bikes.objects.get(bike_id=i)
    q.bike_model='YFZ R15 V3'
    q.save()


    #q= bikes(bike_id=i+168,bike_company='bajaj',bike_model='pulsar 150',bike_cost=350,bike_availability=1,bike_colour='black red',bike_millage=65,bike_cc=150,branch_id=a[i-1])
    #q = bikes(bike_id=i + 168, bike_company='Royale Enfield', bike_model='classic 150', bike_cost=700, bike_availability=1,bike_colour='black', bike_millage=37, bike_cc=346, branch_id=a[i - 1])
    #q = bikes(bike_id=i + 224, bike_company='honda', bike_model='activa 125', bike_cost=350,bike_availability=1, bike_colour='pearl amazing white', bike_millage=59, bike_cc=125, branch_id=a[i - 1])
    #q = bikes(bike_id=i+280, bike_company='honda', bike_model='activa 125', bike_cost=350, bike_availability=1,bike_colour='midnight blue metalic', bike_millage=59, bike_cc=125, branch_id=a[i - 1])
    #q = bikes(bike_id=i+252, bike_company='honda', bike_model='activa 125', bike_cost=350, bike_availability=1,bike_colour='rebal red metalic', bike_millage=59, bike_cc=125, branch_id=a[i - 1])
    #q = bikes(bike_id=i + 196, bike_company='Royale Enfield', bike_model='thunder bird 350', bike_cost=700,bike_availability=1, bike_colour='roving red', bike_millage=35, bike_cc=346, branch_id=a[i - 1])
        q.save()
c=bikes.objects.get(bike_id=308)
b.image('hqdefault.jpg', open('C:\Users\Nithin sai\Pictures\cities\chennai\hqdefault.jpg','rb'))
p= open('C:\Users\Nithin sai\Pictures\cities\chennai\hqdefault.jpg','rb')
57 84
for i in range (57,85):
    q = bikes.objects.get(bike_id=i)
    q.bike_model='YFZ R15 V3'
    q.save()
