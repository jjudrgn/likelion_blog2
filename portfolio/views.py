from django.shortcuts import render, get_object_or_404, redirect
from .models import Portfolio
# Create your views here.
def portfolio(request):
    portfolios = Portfolio.objects
    return render(request, "portfolio.html", {'portfolios':portfolios})