Nanth
=====================

This is a python package that can call the class TtestStats 
and will allow you to use methods .calc_stats() and .ttest() to
find the mean, standard deviation, and variance along with the 
Welch's t-test on the values provided. 

EX:

>>> import nanth as nth

>>> nth.TtestStats(x, 'DMSO', 6, 8, sample_col='Treatment')

>>> x.calc_stats()

... returns DataFrame

>>> x.ttest()

... returns DataFrame

>>> x.stats_df

The last line will return the df with mean, std, var, p_value, t_value. sample_col defaults to the index of the dataframe unless told otherwise

