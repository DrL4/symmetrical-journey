from django.shortcuts import render
from django.http import request,HttpResponse
import stripe
from app.models import Ticket,Category
from django.conf import settings
from django.views.generic.base import TemplateView


stripe.api_key = settings.STRIPE_SECRET_KEY
class index(TemplateView):
    template_name = 'app/sports/index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["key"] = settings.STRIPE_PUBLISHABLE_KEY
        return context
    
def search(request):
    search_query = request.GET.get('q')
    if search_query:
        # category = search_query
        # categories = Category.objects.filter(description=category)
        # print(categories)
        tickets = Ticket.objects.filter(categorie__description=search_query)
        print(tickets,'======')
        return render(request, 'app/sports/index.html', { 'tickets': tickets})
    else:
        categories = Category.objects.all()
        tickets = Ticket.objects.all()
        return render(request, 'app/sports/index.html', {'categories': categories, 'tickets': tickets})
    
def charge(request):
    if request.method =='POST':
        charge = stripe.Charge.create(
            amount=int(request.POST['amount']),

        )