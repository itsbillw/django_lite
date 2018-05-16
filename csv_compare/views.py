from django.shortcuts import render
import pandas as pd
import numpy as np

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

        def compare_two_dfs(input_df_1, input_df_2):
            df_1, df_2 = input_df_1.copy(), input_df_2.copy()
            ne_stacked = (df_1 != df_2).stack()
            changed = ne_stacked[ne_stacked]
            changed.index.names = ['id', 'col']
            difference_locations = np.where(df_1 != df_2)
            changed_from = df_1.values[difference_locations]
            changed_to = df_2.values[difference_locations]
            df = pd.DataFrame({
                'from': changed_from,
                'to': changed_to
            }, index=changed.index)
            return df

        ds3 = compare_two_dfs(ds1, ds2)
        ds3 = ds3.to_json
        context = {'ds3': ds3}

    return render(request, 'csv_compare/result.html', context)