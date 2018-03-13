import numpy as np
import pandas as pd
from collections import Counter

def IQR(df, features, n=3):
    # Takes a dataframe and a list of features or a feature, and a n
    outlier_index = []
    
    for col in features:
        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)
        iqr = q3 - q1
        
        up_limit = q3 + (1.5*iqr)
        low_limit = q1 - (1.5*iqr)
        
        outlier_list = df.loc[(df[col] < low_limit) | (df[col] > up_limit)].index
        outlier_index.extend(outlier_list)
    
    outlier_index = Counter(outlier_index)
    multiple_outliers = [k for k,v in outlier_index.items() if v >= n]
    return multiple_outliers
