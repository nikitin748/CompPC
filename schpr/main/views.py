from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return render(request, 'main/main1.html')
def result(request):
    return render(request, 'main/result.html')
# Create your views here.

#
# from django.shortcuts import render, redirect
# from .models import GraphicsCard, Processor, Motherboard


# def build_pc(request):
#     if request.method == 'POST':
#         budget = float(request.POST.get('price'))
#         selected_processor = request.POST.get('processor')
#         selected_graphics = request.POST.get('graphics')
#
#         graphics_card_price = budget * 0.3
#
#         # Получение подходящих комплектующих
#         graphics_cards = GraphicsCard.objects.filter(brand=selected_graphics, price__lte=graphics_card_price)
#         processors = Processor.objects.filter(brand=selected_processor, price__lte=budget - graphics_card_price)
#         motherboards = Motherboard.objects.all()  # Предположим, что материнская плата фиксирована
#
#         context = {
#             'graphics_cards': graphics_cards,
#             'processors': processors,
#             'motherboards': motherboards,
#         }
#         return render(request, 'result.html', context)
#
#     return render(request, 'main1.html')
