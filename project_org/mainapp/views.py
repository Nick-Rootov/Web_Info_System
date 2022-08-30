from django.shortcuts import render, redirect
from .models import *
from django.core.cache import cache
from .forms import AddSotrForm, AddDogovForm, AddProjForm

# Create your views here.
def index(request):
    data = {
        'title': 'Главная страница',
        'values': ['Some', 'Hello', '123'],
        'obj': {
            'car':'BMW',
            'age':'18',
            'hobby':'football'}
    }
    return render(request, 'mainapp/index.html', data)

def sotr(request):
    sortirovka = request.GET.getlist('q')
    if sortirovka:
        spisok_sotrudnikov = Sotrudniki.objects.order_by(*sortirovka)
        cache.set('sort_cache', sortirovka, 60)
    else:
        sortirovka = cache.get('sort_cache')
        if sortirovka:
            spisok_sotrudnikov = Sotrudniki.objects.order_by(*sortirovka)
        else:
            spisok_sotrudnikov = Sotrudniki.objects.order_by('last_name')

    cache.add('sort_cache', sortirovka, 60)

    return render(request, 'mainapp/sotr.html',{'spisok_sotrudnikov': spisok_sotrudnikov})

def add_sotr(request):
    if request.method == 'POST':
        form = AddSotrForm(request.POST)
        if form.is_valid():
            #print(form.cleaned_data)
                #Sotrudniki.objects.create(**form.cleaned_data)
            form.save()
            return redirect('sotr')
    else:
        form = AddSotrForm()

    return render(request, 'mainapp/add_sotr.html', {'form':form})

def dogov(request):
    sortirovka = request.GET.getlist('q')
    if sortirovka:
        spisok_dogovorov = Dogovor.objects.order_by(*sortirovka)
        cache.set('dogov_cache', sortirovka, 60)
    else:
        sortirovka = cache.get('dogov_cache')
        if sortirovka:
            spisok_dogovorov= Dogovor.objects.order_by(*sortirovka)
        else:
            spisok_dogovorov = Dogovor.objects.order_by('zakazchik')

    cache.add('dogov_cache', sortirovka, 60)
    sum = 2;
    return render(request, 'mainapp/dogov.html',{'spisok_dogovorov': spisok_dogovorov, 'sum': sum})

def add_dogov(request):
    if request.method == 'POST':
        form = AddDogovForm(request.POST)
        if form.is_valid():
            #print(form.cleaned_data)
                #Sotrudniki.objects.create(**form.cleaned_data)
            form.save()
            return redirect('dogov')
    else:
        form = AddDogovForm()

    return render(request, 'mainapp/add_dogov.html', {'form':form})



def proj(request):
    sortirovka = request.GET.getlist('q')
    if sortirovka:
        spisok_projects = Project.objects.order_by(*sortirovka)
        cache.set('proj_cache', sortirovka, 60)
    else:
        sortirovka = cache.get('proj_cache')
        if sortirovka:
            spisok_projects = Project.objects.order_by(*sortirovka)
        else:
            spisok_projects = Project.objects.order_by('name')

    cache.add('proj_cache', sortirovka, 60)

    return render(request, 'mainapp/proj.html',{'spisok_projects': spisok_projects})

def add_proj(request):
    if request.method == 'POST':
        form = AddProjForm(request.POST)
        if form.is_valid():
            #print(form.cleaned_data)
                #Sotrudniki.objects.create(**form.cleaned_data)
            form.save()
            return redirect('proj')
    else:
        form = AddProjForm()

    return render(request, 'mainapp/add_proj.html', {'form':form})

def otd(request):
    sortirovka = request.GET.getlist('q')
    if sortirovka:
        spisok_otdelov = Otdel.objects.order_by(*sortirovka)
        cache.set('otd_cache', sortirovka, 60)
    else:
        sortirovka = cache.get('otd_cache')
        if sortirovka:
            spisok_otdelov = Otdel.objects.order_by(*sortirovka)
        else:
            spisok_otdelov = Otdel.objects.order_by('name')

    cache.add('otd_cache', sortirovka, 60)

    return render(request, 'mainapp/otd.html',{'spisok_otdelov': spisok_otdelov})

def mach(request):
    sortirovka = request.GET.getlist('q')
    if sortirovka:
        spisok_machines = Machine.objects.order_by(*sortirovka)
        cache.set('mach_cache', sortirovka, 60)
    else:
        sortirovka = cache.get('mach_cache')
        if sortirovka:
            spisok_machines = Machine.objects.order_by(*sortirovka)
        else:
            spisok_machines = Machine.objects.order_by('name')

    cache.add('mach_cache', sortirovka, 60)

    return render(request, 'mainapp/mach.html',{'spisok_machines': spisok_machines})