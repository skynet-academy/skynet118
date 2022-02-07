import os

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
#from django.template import loader
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from django import forms
#importing for user
from django.contrib.auth.models import User, Group

from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.utils.translation import gettext as _

from .decorators import (
        unauthenticated_user, 
        portfolio_created, 
        allowed_users, 
        admin_only,
        profile_created
        )

from .forms import (
        UserProfileForm,
        PortfolioForm,
        CommentForm,
        RegisterUserForm
        )

# importing models 
from courses.models import Course

from .models import (
            UserProfile,
            Comment,
            Portfolio
        )

# importing forms

from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def index(request):
    courses = Course.objects.all().order_by('id')
    if(request.method == "POST"):
        data = request.body.decode('utf-8')
    context = {
            "courses": courses
            }
    return render(request, 'blog/index.html', context) 

##################################################

def contact_view(request):
    if(request.user.is_authenticated):
        user = User.objects.get(username=request.user) 
        context = {
                'user': user
                }
    return render(request, 'blog/contact.html', context)

def contacts_view(request):
    users = User.objects.all() 
    context = {
            'users': users
            }
    return render(request, 'blog/contacts.html', context)


def contact_create(request):
    if(request.method == 'POST'):
        contact = ContactProfileForm(request.POST)
        print(request.body)
        if(contact.is_valid()):
            contact.save()
            return redirect('/')
        context = {'contact': contact}
        return render(request, 'blog/contact_create.html', context)

def contact_update(request, pk):
    pass

def contact_delete(request, pk):
    pass

##################################################

def portfolios_view(request):
    portfolios = Portfolio.objects.all()
    context = {'portfolios': portfolios}
    return render(request, 'blog/portfolios.html', context)

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


def portfolio_view(request, id):
    portfolio_exists = Portfolio.objects.filter(user=id).exists()
    if(portfolio_exists):
        #portfolio = Portfolio.objects.get(user=request.user)
        portfolio = Portfolio.objects.get(user=id)
        context = {'portfolio': portfolio}
        return render(request, 'blog/portfolio.html', context)
    else:
        return redirect('/portfolio_create/')

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

@portfolio_created
@allowed_users(allowed_roles=['admin', 'teacher'])
def portfolio_create(request):
    portfolio = PortfolioForm()
    if(request.method == 'POST'):
        portfolio = PortfolioForm(request.POST, request.FILES)
        if(portfolio.is_valid()):
            portfolio.save()
            portfolio_name = portfolio.cleaned_data.get('name')
            messages.success(request, "The portfolio was successful created for " + portfolio_name)
            messages.error(request, "Here is an error")
            return redirect('/')

    context = {'portfolio': portfolio }
    return render(request, 'blog/portfolio_create.html', context)

@allowed_users(allowed_roles=['admin', 'teacher'])
def portfolio_update(request, pk):
    portfolio = Portfolio.objects.get(id=pk)
    form = PortfolioForm(instance=portfolio)
    if(request.method == "POST"):
        form = PortfolioForm(request.POST, request.FILES, instance=portfolio)
        if(form.is_valid()):
            img_path = portfolio.image.path 
            if(os.path.exists(img_path)):
                os.remove(img_path)
            form.save()
            return redirect(f"/portfolio/{request.user.id}")
    context = {'form': form}
    return render(request, 'blog/portfolio_update.html', context)

##################################################

class CommentView(generic.ListView):
    model = Comment 
    template_name = "blog/comment.html"
    paginate_by = 10

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class CommentDetailView(generic.DetailView):
    model = Comment
    template_name = "blog/comment_detail.html"

##################################################

@unauthenticated_user
def registerPage(request):
    form = RegisterUserForm()
    if(request.method == "POST"):
        form = RegisterUserForm(request.POST)
        if(form.is_valid()):
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            email_exists = User.objects.filter(email=email).exists()
            if(email_exists):
                messages.error(request, f"The email: {email} is already in use")
                return redirect("/register/")
            user = form.save()
            group = Group.objects.get(name='customer')
            user.groups.add(group)
            messages.success(request, "The account was successful created for " + username)

            return redirect("/login/")

    context = {'form': form}
    return render(request, 'blog/register.html', context)

##################################################

@allowed_users(allowed_roles=['admin', 'teacher', 'student'])
def profile_create(request):
    profile = UserProfileForm()
    if(request.method == "POST"):
        profile = UserProfileForm(request.POST, request.FILES)
        if(profile.is_valid()):
            profile.save()
            return redirect("/") 
    context = {"profile": profile}
    return render(request, 'blog/profile_create.html', context)


def profile_view(request, id):
    profile_exists = UserProfile.objects.filter(user=id).exists()
    if(profile_exists):
        profile = UserProfile.objects.get(user=request.user)
        context = {'profile': profile}
        return render(request, 'blog/profile.html', context)
    else:
        return redirect('/profile_create/')


def profile_update(request, id):
    profile = UserProfile.objects.get(id=id)
    form = UserProfileForm(instance=profile)
    if(request.method == "POST"):
        form = UserProfileForm(request.POST, request.FILES , instance=profile)
        if(form.is_valid()):
            img_path = profile.avatar.path 
            if(os.path.exists(img_path)):
                os.remove(img_path)
            form.save()
            return redirect(f"/profile/{request.user.id}")
    context = {'form': form}
    return render(request, 'blog/profile_update.html', context)





##################################################

@unauthenticated_user
def loginPage(request):
    if(request.method == "POST"):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if(user is not None):
            login(request, user)
            return redirect("/")
        else:
            messages.info(request, "The username or password is incorrect")
    context = {}
    return render(request, 'blog/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('/')

def restricted_view(request):
    user = request.user 
    context = {
            'user': user
            }
    return render(request, 'blog/restricted_page.html', context)
