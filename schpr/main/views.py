from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return render(request, 'main/main1.html')
def result(request):
    return render(request, 'main/result.html')


from django.shortcuts import render
from .models import NV, RD, Rizen, Intel, OtherSet


def index(request):
    return render(request, 'main/main1.html')


def result(request):
    if request.method == 'POST':
        budget = float(request.POST.get('price'))
        selected_processor_brand = request.POST.get('processor')
        selected_graphics_brand = request.POST.get('graphics')

        # Вычисляем бюджет для видеокарты (30% от общего бюджета)
        graphics_card_budget = budget * 0.3

        # Получение подходящих видеокарт
        if selected_graphics_brand == "Nvidia":
            graphics_cards = NV.objects.filter(price__lte=graphics_card_budget).order_by(
                '-price')  # Сортировка по убыванию цены
        else:
            graphics_cards = RD.objects.filter(price__lte=graphics_card_budget).order_by(
                '-price')  # Сортировка по убыванию цены

        # Выбор самой дорогой видеокарты в пределах бюджета
        if graphics_cards.exists():
            selected_graphics_card = graphics_cards.first()
        else:
            selected_graphics_card = NV.objects.order_by(
                '-price').first() if selected_graphics_brand == "Nvidia" else RD.objects.order_by('-price').first()

        # Определяем оставшийся бюджет после выбора видеокарты
        remaining_budget_after_graphics = budget - (selected_graphics_card.price if selected_graphics_card else 0)

        # Получение подходящих процессоров
        if selected_processor_brand == "AMD":
            processors = Rizen.objects.filter(price__lte=remaining_budget_after_graphics).order_by(
                '-price')  # Сортировка по убыванию цены
        else:
            processors = Intel.objects.filter(price__lte=remaining_budget_after_graphics).order_by(
                '-price')  # Сортировка по убыванию цены

        # Выбор самого дорогого процессора в пределах оставшегося бюджета
        if processors.exists():
            selected_processor = processors.first()
        else:
            selected_processor = Rizen.objects.order_by(
                '-price').first() if selected_processor_brand == "AMD" else Intel.objects.order_by('-price').first()

        # Определяем оставшийся бюджет для других комплектующих
        remaining_budget_for_others = remaining_budget_after_graphics - (
            selected_processor.price if selected_processor else 0)

        # Получение всех других комплектующих в зависимости от оставшегося бюджета
        othersets = OtherSet.objects.filter(priceSum__lte=remaining_budget_for_others).order_by(
            '-priceSum')  # Сортировка по убыванию цены

        # Выбор других комплектующих
        if othersets.exists():
            selected_other_set = othersets.first()  # Самая дорогая доступная другая комплектующая в рамках бюджета
        else:
            selected_other_set = OtherSet.objects.order_by('priceSum').first()  # Самое дешевое из всех комплектующих

        # Итоговая цена ПК
        total_price = (selected_graphics_card.price if selected_graphics_card else 0) + \
                      (selected_processor.price if selected_processor else 0) + \
                      (selected_other_set.priceSum if selected_other_set else 0)

        context = {
            'graphics_cards': graphics_cards,
            'processors': processors,
            'othersets': othersets,
            'budget': budget,
            'selected_graphics_card': selected_graphics_card,
            'selected_processor': selected_processor,
            'selected_other_set': selected_other_set,
            'total_price': total_price,
        }

        return render(request, 'result.html', context)

    return render(request, 'main/main1.html')







