from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Sauce, Order


class IndexView(generic.ListView):
    template_name = 'shop/index.html'
    context_object_name = 'latest_sauce_list'

    def get_queryset(self):
        """Return the last five published sauces."""
        return Sauce.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Sauce
    template_name = 'shop/detail.html'

class ResultsView(generic.DetailView):
    model = Sauce
    template_name = 'shop/results.html'

def order(request, sauce_id):
    sauce = get_object_or_404(Sauce, pk=sauce_id)
    try:
        selected_sauce = sauce.choice_set.get(pk=request.POST['order'])
    except (KeyError, Order.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'shop/detail.html', {
            'sauce': sauce,
            'error_message': "You didn't select a sauce.",
        })
    else:
        selected_sauce.sauce_rating += 1
        selected_sauce.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('shop:results', args=(sauce.id,)))
