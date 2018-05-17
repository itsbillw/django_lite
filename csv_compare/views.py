from django.shortcuts import render
from csv_compare.file_comparison import compare_two_dfs
import pandas as pd


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
    if request.POST and request.FILES:
        csvfile1 = request.FILES['csv_file1']
        ds1 = pd.read_csv(csvfile1)
        csvfile2 = request.FILES['csv_file2']
        ds2 = pd.read_csv(csvfile2)

        ds3 = compare_two_dfs(ds1, ds2)
        ds3 = ds3.to_html()
        context = {'ds3': ds3}

    return render(request, 'csv_compare/result.html', context)