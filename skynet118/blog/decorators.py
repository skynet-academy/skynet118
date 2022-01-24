from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Portfolio

def unauthenticated_user(view_func):
    def wrapper_function(request, *args, **kwargs):
        if(request.user.is_authenticated):
            return redirect("/")
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_function


def portfolio_created(portfolio_create):
    def evaluation(request, *args, **kwargs):
        portfolio_exists = Portfolio.objects.filter(user=request.user).exists()
        if(portfolio_exists):
            portfolio = Portfolio.objects.get(user=request.user)
            if(str(portfolio.user) == request.user.username):
                return redirect('/')
            else:
                return portfolio_create(request, *args, **kwargs)
        else:
            return portfolio_create(request, *args, **kwargs)
    return evaluation

def profile_created(profile_create):
    def evaluation(request, *args, **kwargs):
        profile_exists = UserProfile.objects.filter(user=request.user).exists()
        if(profile_exists):
            profile = UserProfile.objects.get(user=request.user)
            if(str(profile.user) == request.user.username):
                return redirect('/')
            else:
                return profile_create(request, *args, **kwargs)
        else:
            return profile_create(request, *args, **kwargs)
    return evaluation

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if(request.user.groups.exists()):
                group = request.user.groups.all()[0].name
            if(group in allowed_roles):
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse("<h1>You are not allowed to visit this page. Go <a href='/blog'>Home</a></h1>")
            return view_func(request, *args, **kwargs)
        return wrapper_func
    return decorator

def admin_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if(request.user.groups.exists()):
            group = request.user.groups.all()[0].name

        if(group == "customer"):
            return redirect('contact')
        if(group == "admin"):
            return view_func(request, *args, **kwargs)

    return wrapper_function


