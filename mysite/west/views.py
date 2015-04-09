#encoding=UTF-8
from django.shortcuts import render
from django.http import HttpResponse

from west.models import Character

from django.core.context_processors import csrf
from django import forms
#from django.contrib.auth import *

# Create your views here.

def first_page(requset):
    return HttpResponse('<p>west food</p>')

def staff(request):
    staff_list = Character.objects.all()
    return render(request, 'templay.html', {'staffs' : staff_list})
    '''
    staff_str = map(str, staff_list)
    context = {'label': ' '.join(staff_str)}
    return render(request, 'templay.html', context)
    '''

def templay(request):
    context = {}
    context['label'] = 'hello world'
    return render(request, 'templay.html', context)

def form(request):
    return render(request, 'form.html')

class CharacterForm(forms.Form):
    #通过属性name，说明输入栏name的类型为字符串，最大长度为200
    name = forms.CharField(max_length = 200)

def investigate(request):
    if request.POST:
        form = CharacterForm(request.POST)
        if form.is_valid():
            submitted  = form.cleaned_data['name']
            new_record = Character(name = submitted)
            new_record.save()

    form = CharacterForm()
    ctx ={}
    ctx.update(csrf(request))
    all_records = Character.objects.all()
    ctx['staff'] = all_records
    ctx['form']  = form
    return render(request, "investigate.html", ctx)

def user_login(request):
    '''
    login
    '''
    if request.POST:
        username = password = ''
        username = request.POST.get('username')
        password = request.POST.get('password')
        user     = authenticate(username=username, password=password)
        if user is not None and user.is_active:
                login(request, user)
                return redirect('/')
    ctx = {}
    ctx.update(csrf(request))
    return render(request, 'login.html',ctx)



