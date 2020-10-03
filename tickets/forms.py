from django import forms 
from django.forms import ModelForm 
# import GeeksModel from models.py 
from .models import Ticket 
  
# create a ModelForm 
class TicketForm(ModelForm): 
    # specify the name of model to use 
    class Meta: 
        model = Ticket 
        fields = "__all__"
form=TicketForm()       