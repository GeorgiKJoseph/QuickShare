from django.shortcuts import render
from .models import Card
from .extras import system_info
from .forms import CardForm
from django.utils import timezone

def home(request):
    info = request.META['HTTP_USER_AGENT']
    os, device = system_info(info)
    # input form
    if request.method == 'POST':
        form = CardForm(request.POST)
        if form.is_valid():
            card = form.save(commit=False)
            card.sender = os + ' ' + device
            card.created_date = timezone.now()
            card.save()
    form = CardForm()

    # display content
    cards = Card.objects.all().order_by('-created_date')
    rtn = {'form': form, 'os':os,'device':device,'cards': cards}
    return render(request,'quickshare/home.html', rtn)