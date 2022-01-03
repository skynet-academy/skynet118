from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Portfolio

def unauthenticated_user(view_func):
    def wrapper_function(request, *args, **kwargs):
        if(request.user.is_authenticated):
            return redirect("/blog/")
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_function


def portfolio_created(portfolio_create):
    def evaluation(request, *args, **kwargs):
        portfolio_exists = Portfolio.objects.filter(user=request.user).exists()
        if(portfolio_exists):
            portfolio_created = Portfolio.objects.get(user=request.user)
            if(str(portfolio_created.user) == request.user.username):
                return redirect('/blog/')
            else:
                return portfolio_create(request, *args, **kwargs)
        else:
            return portfolio_create(request, *args, **kwargs)
    return evaluation

