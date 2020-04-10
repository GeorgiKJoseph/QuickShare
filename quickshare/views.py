from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse
from django.conf import settings
import os

from .models import Card
from .extras import system_info, get_attachments
from .forms import CardForm


def home(request):
    info = request.META['HTTP_USER_AGENT']
    OS, device = system_info(info)
#                                                                   input form
    if request.method == 'POST':       
        uploaded_files = request.FILES.getlist('attachment')

        form = CardForm(request.POST)
        if form.is_valid():
            card = form.save(commit=False)
            card.sender = OS + ' ' + device
            card.created_date = timezone.now()
            i=0
            for f in uploaded_files:
                if i < 10:
                    exec('card.atmnt' + str(i) + '= f')
                    i += 1
            card.save()
    form = CardForm()

    # display content
    cards = Card.objects.all().order_by('-created_date')
    temp =''
    for x in cards:
        x.attachments = get_attachments(x)
        print(x.attachments)
    rtn = {'form': form, 'os':OS,'device':device,'cards': cards}
    return render(request,'quickshare/home.html', rtn)


def download(request,pk,fname):
    cards = Card.objects.filter(pk=pk)
    for x in cards:
        fn = 'files/' + str(fname)
        file_path = os.path.join(settings.MEDIA_ROOT, str(fn))
        if os.path.exists(file_path):
            with open(file_path, 'rb') as fh:
                response = HttpResponse(fh.read(), content_type="application/doc.txt")
                response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
                return response
    OS = 'Unknown'
    device = 'Unknown'
    form = CardForm()
    cards = Card.objects.all().order_by('-created_date')
    rtn = {'form': form, 'os':OS,'device':device,'cards': cards}
    return render(request,'quickshare/home.html', rtn)