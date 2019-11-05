from django.shortcuts import get_object_or_404, render

from .models import OliveOil


def index(request):
    olive_oil_list = OliveOil.objects.order_by('-pub_date')
    context = {'olive_oil_list': olive_oil_list}
    return render(request, 'olive/index.html', context)

def detail(request, olive_id):
    olive = get_object_or_404(OliveOil, pk=olive_id)
    return render(request, 'olive/detail.html', {'olive': olive})

# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)

# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)
