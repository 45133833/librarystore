from django.shortcuts import redirect, render
from .models import *
from .forms import *
from django.http import HttpResponse
# Create your views here.

def index(request):
    shelf =Book.objects.all()
    return render(request,'book/library.html',{'shelf':shelf})

def upload(request):
    upload=bookcreate()
    if request.method=='POST':
        upload= bookcreate(request.POST )
        if upload.is_valid() :
            upload.save()
            return redirect('index')
        else:
            return HttpResponse("something went wrong . please reload the web page by clicking <a href={{url 'index'}}>reload</a>")
        
    else:
        return render(request , 'book/upload_form.html' , {'upload_form':upload})


def update_book(request,book_id):
    book_id=int(book_id)
    try:
        book_shelf=Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return redirect('index')
    book_form=bookcreate(request.POST or None , instance=book_shelf)
    if book_form.is_valid():
        book_form.save()
        return redirect('index')
    else:
        return render(request,'book/upload_form.html',{'upload_form':book_form})
    
def delete_book(request ,book_id):
    book_id=int(book_id)
    try:
        book_shelf=Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return redirect('index')
    book_shelf.delete()
    return redirect('index')

    
    






        
