from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.core.mail import send_mail
from django.utils import timezone


from .forms import CustomerForm

from .models import OliveOil, Order


class IndexView(ListView):
    model = OliveOil

    def get(self, request):
        product_list = OliveOil.objects.all()
        context = {'olive_oil_list': product_list}
        return render(request, 'olive/index.html', context)


class DetailView(DetailView):
    model = OliveOil

    def get(self, request, olive_id):
        olive = OliveOil.objects.get(pk=olive_id)
        return render(request, 'olive/detail.html', {'olive': olive})


class OrderView(DetailView):
    model = OliveOil

    def get(self, request, olive_id):
        olive = OliveOil.objects.get(pk=olive_id)
        return render(request, 'olive/order.html', {'olive': olive})

class CustomerFormView(CreateView):
    model = Order

    def get(self, request, olive_id):
        user = request.user
        olive = OliveOil.objects.get(pk=olive_id)
        form = CustomerForm()

        context = {'form': form, 'olive': olive}
        return render(request, "olive/customer_form.html", context)

    def post(self, request, olive_id):
        user = request.user
        olive = OliveOil.objects.get(pk=olive_id)
        if request.method == "POST":
            form = CustomerForm(request.POST)
            if form.is_valid():
                order = form.save(commit=False)
                # order.product = olive
                order.save()


                txt_message = order.customer_name+" Your order was processed successfully"
                # messages.success(request, txt_message)

                return render(request, 'olive/thankyou.html', {'order': order})
            else:

                errors = "Your order was not created"
                # messages.error(request, errors, extra_tags='alert')
        else:
            form = PageForm()

        context = {'form': form}

        return render(request, 'olive/index.html', context)




class ThankyouView(DetailView):
    model = OliveOil

    def get(self, request, olive_id):
        olive = OliveOil.objects.get(pk=olive_id)
        return render(request, 'olive/thankyou.html', {'olive': olive})
