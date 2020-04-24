from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from orders.models import SalesOrder
from orders.serializer import OrderSerializer


def orders_page(request):
    orders = SalesOrder.objects.all()
    return render(request, "index.html", {'orders': orders})


class OrderView(ModelViewSet):
    # в этом классе необходимо определить 2 вещт QuerySet и Serializer
    # QuerySet - список объектов, который будет выводиться
    # Serializer (т.к. нет шаблона куда и что выводить) - в нем нужно определить какие полябудут использоваться, из какиз полей сформируется словарь а затем JSON объект
    queryset = SalesOrder.objects.all()
    serializer_class = OrderSerializer


def orders_app(request):
    return render(request, "main_app.html")