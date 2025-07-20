from django.shortcuts import render
from .models import Apartment, Booking, Host, ChatMessage, LogEntry, FinanceRecord

def dashboard(request):
    context = {
        'apartments': Apartment.objects.all(),
        'bookings': Booking.objects.all(),
        'hosts': Host.objects.all(),
        'chats': ChatMessage.objects.order_by('-timestamp')[:10],
        'logs': LogEntry.objects.order_by('-timestamp')[:10],
        'finance': FinanceRecord.objects.all(),
    }
    return render(request, 'portal/dashboard.html', context)