from django.shortcuts import render,redirect,get_object_or_404
from .models import Poll,Posts
from .forms import *
from django.http import HttpResponse
from django.core.mail import send_mail
from django.core.mail import EmailMessage



def send_message(request):
    send_mail("WEBKA:BACK-END","Content of message","200103189@stu.sdu.edu.kz",["200103189@stu.sdu.edu.kz"],fail_silently=False,html_message="<b>BOLD TEXT</b> <i>Italianski text</i>")
    return render(request,'mail.html')

# Create your views here.
def show_post(request,post_slug):
    post = get_object_or_404(Posts,slug = post_slug)
    context = {'post':post}
    return render(request,'post.html',context=context)

def index(request):
    all_films = Poll.objects.all()
    return render(request, 'index.html', {'films':all_films})

def upload(request):
    upload = FilmCreate()
    if request.method == 'POST':
        upload = FilmCreate(request.POST,request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse("""Error, reload on <a href="{{url : 'index'}}">reload</a>""")
    else:
        return render(request,'upload_form.html',{'upload_form':upload})

def update_post(request, post_id):
    post_id = int(post_id)
    try:
        post_sel = Poll.objects.get(id = post_id)
    except Poll.DoesNotExist:
        return redirect('index')
    post_form = FilmCreate(request.POST or None, instance = post_sel)
    if post_form.is_valid():
        post_form.save()
        return redirect('index')
    return render(request, 'upload_form.html', {'upload_form':post_form})

def delete_post(request, post_id):
    post_id = int(post_id)
    try:
        post_sel = Poll.objects.get(id = post_id)
    except Poll.DoesNotExist:
        return redirect('index')
    post_sel.delete()
    return redirect('index')

def addpage(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid() :
            try:
                form.save()
                return redirect('add_page')
            except:
                form.add_error(None,'Makalany kosylmady')
    else:
            form = AddPostForm()
    return render(request, 'AddPage.html',{'title':'TITLEEE','form':form})