import pandas as pd
import numpy as np

def compare_two_dfs(input_df_1, input_df_2):
    df_1, df_2 = input_df_1.copy(), input_df_2.copy()
    ne_stacked = (df_1 != df_2).stack()
    changed = ne_stacked[ne_stacked]
    changed.index.names = ['row', 'col']
    difference_locations = np.where(df_1 != df_2)
    changed_from = df_1.values[difference_locations]
    changed_to = df_2.values[difference_locations]
    df = pd.DataFrame({
        'from': changed_from,
        'to': changed_to
    }, index=changed.index)
    df.reset_index(inplace=True)
    df['row'] = df['row'] + 2
    return df