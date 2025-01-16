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

        graphics_card_budget = budget * 0.42

        if selected_graphics_brand == "Nvidia":
            graphics_cards = NV.objects.filter(price__lte=graphics_card_budget).order_by(
                '-price')  #
        else:
            graphics_cards = RD.objects.filter(price__lte=graphics_card_budget).order_by(
                '-price')

        selected_graphics_card = graphics_cards.first()

        remaining_budget_after_graphics = budget - (selected_graphics_card.price if selected_graphics_card else 0)

        if selected_processor_brand == "AMD":
            processors = Rizen.objects.filter(price__lte=remaining_budget_after_graphics).order_by(
                '-price')
        else:
            processors = Intel.objects.filter(price__lte=remaining_budget_after_graphics).order_by(
                '-price')

        if processors.exists():
            selected_processor = processors.first()
        else:
            selected_processor = Rizen.objects.order_by(
                '-price').first() if selected_processor_brand == "AMD" else Intel.objects.order_by('-price').first()

        remaining_budget_for_others = remaining_budget_after_graphics - (
            selected_processor.price if selected_processor else 0)

        othersets = OtherSet.objects.filter(priceSum__lte=remaining_budget_for_others).order_by(
            '-priceSum')

        if othersets.exists():
            selected_other_set = othersets.first()
        else:
            selected_other_set = OtherSet.objects.order_by('priceSum').first()


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







