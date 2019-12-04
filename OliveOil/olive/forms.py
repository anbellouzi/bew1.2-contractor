from django import forms
from olive.models import Order


class CustomerForm(forms.ModelForm):
    """ Render and process a form based on the Page model. """
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ["author", "olive_id"]
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'John Doe'}),
            'email': forms.TextInput(attrs={'placeholder': 'Enter your email'}),
            'phone_number': forms.TextInput(attrs={'placeholder': '###-###-####'}),
        }
