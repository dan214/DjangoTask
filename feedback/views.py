from django.shortcuts import render,render_to_response
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .forms import UserForm, FeedbackForm
from .models import Company, Feedback
# Create your views here.

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                companys = Company.objects.filter(user=request.user)
                return render_to_response('company.html', {'object_list': Company.objects.all()})
            else:
                return render(request, 'login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'login.html', {'error_message': 'Invalid login'})
    return render(request, 'login.html')

def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render_to_response('company.html',{'object_list': Company.objects.all()})
    context = {
        "form": form,
    }
    return render(request, 'register.html', context)

def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'login.html', context)

def create_comment(request):
    if not request.user.is_authenticated():
        return render(request, 'login.html')
    else:
        form = FeedbackForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.save()
            return render_to_response('company.html', {'object_list': Company.objects.all()})
        context = {
            "form": form,
        }
        return render(request, 'create_comment.html', context)
