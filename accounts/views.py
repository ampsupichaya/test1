from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import vocab
from django.contrib.auth import authenticate, login

# Create your views here.
from .forms import CreateUserForm

def indexView(request):
    return render(request, 'index.html')

def mainView(request):
    return render(request, 'main.html')

# def LoginView(request):
#     if request.method == "POST":
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         user = authenticate(request, username=username, password=password)

#         if user is not None:
#             login(request, user)
#             return redirect('home')



@login_required
def deshboardView(request):
    return render(request, 'dashboard.html')

def dashboardView(request):
    return render(request, 'dashboard.html')

def registerView(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form = CreateUserForm()
    return render(request, 'registration/register.html',{'form':form})

def vocabView(request):
    vocab_name = request.POST.get("vocab_name")
    vocab_detail = request.POST.get("vocab_detail")

    new_vocab = vocab(vocab_name=vocab_name, vocab_detail=vocab_detail)
    new_vocab.save()

    return render(request, 'insertvocab.html')

def showvocabView(request):
    all_vocab = vocab.objects.all()
    return render(request, 'showvocab.html', {'all_vocab':all_vocab})

def deletevocabView(request, i):
    x = vocab.objects.get(id=i).delete()
    return redirect('/showvocab')

def editvocabView(request, i):
    y = vocab.objects.get(id=i)
    return render(request, 'editvocab.html', {'y':y})
