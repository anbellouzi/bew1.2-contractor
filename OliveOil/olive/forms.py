from django import forms
from olive.models import Order


class CustomerForm(forms.ModelForm):
    """ Render and process a form based on the Page model. """
    class Meta:
        model = Order
        fields = '__all__'
        
