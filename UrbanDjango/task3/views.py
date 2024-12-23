from django.views.generic import TemplateView
from django.shortcuts import render

# Create your views here.


class platform(TemplateView):
    template_name = 'platform.html'


def games(request):
    game_names = [{"name": "Atomic Heart", }, {"name": "Cyberpunk 2077", }, {"name": "PayDay 2", },]
    return render(request,
                  template_name='games.html',
                  context={'game_names': game_names},
                  )


class cart(TemplateView):
    template_name = 'cart.html'
