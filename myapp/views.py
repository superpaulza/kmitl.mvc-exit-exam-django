import random
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from .upload import MemeUpload
from .models import Meme
import decimal
from decimal import Decimal


# Controller

# an index page
def index(request):
    return render(request, 'myapp/index.html')


# a upload page
def upload(request):
    form = MemeUpload()
    if request.method == 'POST':
        form = MemeUpload(request.POST)
        if form.is_valid():
            meme = form.save(commit=False)
            max_rand = random.randint(1, 100000)
            meme.reach = max_rand
            meme.like = random.randint(1, max_rand - 1)
            meme.share = random.randint(1, max_rand - 1)
            meme.comment = random.randint(1, max_rand - 1)
            meme.save()
            messages.success(request, 'Upload success')
            return HttpResponseRedirect(reverse('myapp:index', kwargs={}))
        messages.error(request, 'Upload failed')
    return render(request, 'myapp/upload.html', {
        'form': form,
    })


# view all meme page
def view_meme(request):
    meme = Meme.objects.all()
    return render(request, 'myapp/meme.html', {
        'meme': meme,
    })
