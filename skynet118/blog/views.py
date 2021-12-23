from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
#from django.template import loader
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.utils.translation import gettext as _

from .forms import (
        SkillForm,
        UserProfileForm,
        ContactProfileForm,
        TestimonialForm,
        MediaForm,
        PortfoliForm,
        CommentForm,
        CertificateForm,
        RegisterUserForm
        )

# importing models 
from courses.models import Course

from .models import (
            UserProfile,
            Comment,
            Portfolio,
            Testimonial,
            Certificate
        )

# importing forms

from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def index(request):
    template_name = "blog/index.html"

    courses = Course.objects.all().order_by('id')
    if(request.method == "POST"):
        data = request.body.decode('utf-8')
        print(data)
        print(request.method)
    if(request.method == "GET"):
        data = request.body.decode('utf-8')
        print(request.method)
        print(data)
    testimonials = Testimonial.objects.filter(is_active=True)
    certificates = Certificate.objects.filter(is_active=True)
    Comments = Comment.objects.filter(is_active=True)
    portfolio = Portfolio.objects.filter(is_active=True)
    context = {
            "testimonials": testimonials,
            "certificates": certificates,
            "Comments": Comments,
            "portfolio": portfolio,
            "courses": courses
            }
    return render(request, 'blog/index.html', context) 

class ContactView(generic.FormView):
    template_name = "blog/contact.html"
    form_class = ContactProfileForm()
    success_url = "/"
    
    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Thank you. We will be in touch soon.")
        return super().form_valid(form)

def contact_create(request):
    contact = ContactProfileForm()
    if(request.method == 'POST'):
        contact = ContactProfileForm(request.POST)
        if(contact.is_valid):
            contact.save()
            return redirect('/blog/')
    context = {'contact': contact}
    return render(request, 'blog/contact_create.html', context)



def contact_update(request, pk):
    pass

def contact_delete(request, pk):
    pass


class PortfolioView(generic.ListView):
    model = Portfolio
    template_name = "blog/portfolio.html"
    paginate_by = 10

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

def portfolio_create(request):
    portfolio = PortfoliForm()
    if(request.method == 'POST'):
        portfolio = PortfoliForm(request.POST)
        if(portfolio.is_valid()):
            portfolio.save()
            return redirect('/blog/')
    context = { 'portfolio': portfolio }
    return render(request, 'blog/portfolio_create.html', context)

class PortfolioDetailView(generic.DetailView):
    model = Portfolio
    template_name = "blog/portfolio_detail.html"


class CommentView(generic.ListView):
    model = Comment 
    template_name = "blog/comment.html"
    paginate_by = 10

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

class CommentDetailView(generic.DetailView):
    model = Comment
    template_name = "blog/comment_detail.html"

def profile(request):
    context = {}
    return render(request, 'blog/profile.html', context)


def registerPage(request):
    if(request.user.is_authenticated):
        return redirect("/blog/")
    else:
        form = RegisterUserForm()
        if(request.method == "POST"):
            form = RegisterUserForm(request.POST)
            if(form.is_valid()):
                form.save()
                user= form.cleaned_data.get('username')
                messages.success(request, "The account was successful created for " + user)
                messages.error(request, "Here is an error")
                return redirect("/blog/login/")

        context = {'form': form}
        return render(request, 'blog/register.html', context)


def loginPage(request):
    if(request.user.is_authenticated):
        return redirect("/blog/")
    else:
        if(request.method == "POST"):
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if(user is not None):
                login(request, user)
                return redirect("/blog/")
            else:
                messages.info(request, "The username or password is incorrect")
        context = {}
        return render(request, 'blog/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('/blog/')


