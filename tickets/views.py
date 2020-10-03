from django.shortcuts import render
from .filters import TicketFilter
from .models import Ticket
from django.views.generic import ListView
from .forms import TicketForm
from django.http import HttpRequest, HttpResponseRedirect, request


# Create your views here.
class TicketListView(ListView):
    model= Ticket
    template_name='tickets/index.html'
    
   
        
    def get_context_data(self,**kwargs): 

     
        
        context=super().get_context_data(**kwargs)
        context['filter']=TicketFilter(self.request.GET,queryset=self.get_queryset())
        return context
