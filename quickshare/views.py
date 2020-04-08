from django.shortcuts import render
from django.utils import timezone
from django.core.files.storage import FileSystemStorage

from .models import Card
from .extras import system_info
from .forms import CardForm


def home(request):
    info = request.META['HTTP_USER_AGENT']
    os, device = system_info(info)
#                                                                   input form
    if request.method == 'POST':       
        try:
            uploaded_file = request.FILES['fil']
            save(uploaded_file)
            fileExists = True
        except:
            fileExists = False

        #form = CardForm(request.POST, request.FILES)
        form = CardForm(request.POST)
        if form.is_valid():
            card = form.save(commit=False)
            card.sender = os + ' ' + device
            card.created_date = timezone.now()
            if fileExists:
                card.attachment = uploaded_file.name
                fss = FileSystemStorage()
                fss.save(uploaded_file.name,uploaded_file)
            card.save()
    form = CardForm()
    

    # display content
    cards = Card.objects.all().order_by('-created_date')
    rtn = {'form': form, 'os':os,'device':device,'cards': cards}
    return render(request,'quickshare/home.html', rtn)

'''
def handle_uploaded_file(f):
    with open('quickshare/files/test.txt','wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
'''