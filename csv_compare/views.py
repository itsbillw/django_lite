from django.shortcuts import render

def index(request):
    """The home page for learning log"""
    return render(request, 'csv_compare/index.html')

def example(request):
    """test page"""
    return render(request, 'csv_compare/example.html')

def compare(request):
    """import and compare two csv files """
    return render(request, 'csv_compare/compare.html')

def result(request):
    """import and compare two csv files """
    return render(request, 'csv_compare/result.html')