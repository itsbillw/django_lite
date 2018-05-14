from django.shortcuts import render

def index(request):
    """The home page for learning log"""
    return render(request, 'csv_compare/index.html')

def compare(request):
    """The home page for learning log"""
    return render(request, 'csv_compare/compare.html')

def example(request):
    """The home page for learning log"""
    return render(request, 'csv_compare/example.html')
