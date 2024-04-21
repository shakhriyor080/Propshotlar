from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login, logout
from .middlewares import auth, guest
# Create your views here.

@guest
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('index')
    else:
        initial_data = {'username':'', 'password1':'','password2':""}
        form = UserCreationForm(initial=initial_data)
    return render(request, 'auth/register.html',{'form':form})

@guest
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('index')
    else:
        initial_data = {'username':'', 'password':''}
        form = AuthenticationForm(initial=initial_data)
    return render(request, 'auth/login.html',{'form':form}) 

@auth
def dashboard_view(request):
    return render(request, 'index.html')

def logout_view(request):
    logout(request)
    return redirect('index')


from django.views.generic import  ListView, DetailView
from .models import Post, Otzivlar, Statistika, Tarif,Natijalar

class PostListView(ListView):
    model = Post
    template_name = 'index.html'
    
class OtzivListView(ListView):
    model = Otzivlar
    template_name = 'otziv.html'

class StatistikaListView(ListView):
    model = Statistika
    template_name = 'statistika.html'

class TarifListView(ListView):
    model = Tarif
    template_name = 'tarif.html'

class PropListview(ListView):
    model = Post
    template_name = 'prop-tredir.html'

class KabinetListView(ListView):
    model = Post
    template_name = 'kabinet.html'


class OtzivDetail(DetailView):
    model = Otzivlar
    template_name = 'otziv_detail.html'

class NatijaListView(ListView):
    model = Natijalar
    template_name = 'natija.html'

class NatijaDetail(DetailView):
    model = Natijalar
    template_name = 'natija_detail.html'
