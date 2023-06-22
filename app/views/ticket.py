from django.shortcuts import render, redirect
from django.http import request,HttpRequest
from app.models import Ticket,Category
from app.forms import TicketForm

# @login_required(login_url='login_index')
def index(request):
    tickets = Ticket.objects.all()
    categories = Category.objects.all()
    
    category = request.GET.get('category')
    
    if category == None:
        tickets = Ticket.objects.order_by('-price').filter(status = True)
    else:
        tickets = Ticket.objects.filter(categorie__description = category)
    
    
        
    context = {'tickets': tickets, 'categories': categories}
    
    return render(request, 'app/tickets/index.html', context)
  
  
def detail(request, pk):
    eachticket = Ticket.objects.get(id=pk)
  
    context = {'eachticket': eachticket}
    
    return render(request, 'app/tickets/detail.html', context)
  
  
def addTicket(request):
    form = TicketForm()
    
    if request.method == 'POST':
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ticket_index')
    else:
        form = TicketForm()
        
    context = {'form': form}
    
    return render(request, 'app/tickets/add.html', context)
  
def editTicket(request, pk):
    ticket = Ticket.objects.get(id=pk)
    
    form = TicketForm(instance=ticket)
    
    if request.method == 'POST':
        form = TicketForm(request.POST, request.FILES, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect('ticket_index')
        
    context = {'form': form}
    
    return render(request, 'app/tickets/edit.html', context)
  
def deleteTicket(request, pk):
    ticket = Ticket.objects.get(id=pk)
    ticket.delete()
    return redirect('ticket_index')
