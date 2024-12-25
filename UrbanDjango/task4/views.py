from django.views.generic import TemplateView
from django.shortcuts import render

# Create your views here.


class platform(TemplateView):
    template_name = 'platform.html'


def games(request):
    game_names = {"games": ["Atomic Heart", "Cyberpunk 2077", "PayDay 2"], }
    return render(request,
                  template_name='games.html',
                  context={'games': game_names},
                  )


class cart(TemplateView):
    template_name = 'cart.html'