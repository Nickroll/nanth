# Imports 

import pandas as pd
import numpy as np
from scipy.stats import ttest_ind_from_stats

class TtestStats(object):
    '''
    This class will take in raw csv DataFrame and perform an analysis to:
    calculate mean
    calculate std
    calculate var
    return a df with these values
    
    Then it will use that DF to preform a Welch's t-test and
    add p-value and t-score to the df from before
    '''
    
    def __init__(self, data, control, n_cont, n_test, sample_col='index'):
        '''
        Return an object who has a DataFrame, a control, and a
        integer for number of replicate samples in controls and test group
        '''
        self.data = data
        self.control = control
        self.n_cont = n_cont
        self.n_test = n_test
      
        
        
        # We are going to set the index to be the sample col name if it
        # is not that way already
        if sample_col != 'index':
            self.data.set_index(sample_col, inplace=True)
    
    def calc_stats(self):
        '''
        Calculate the mean, std, var, and return a DataFrame with these values
        '''
        col_names = ['mean', 'std', 'var']
        new_index = []
        avg = []
        std = []
    
        # This loop goes through and calcs avg and std for each row and
        # saves the row names to use for making the df later
        for index in self.data.itertuples():
            new_index.append(index[0])
            avg.append(np.nanmean(index[1:]))
            std.append(np.nanstd(index[1:]))
        
        self.stats_df = pd.DataFrame(index=new_index, columns=col_names)
        self.stats_df['mean'] = avg
        self.stats_df['std'] = std
        self.stats_df['var'] = (np.array(std)**2)
        self.stats_df['p_value'] = np.nan
        self.stats_df['t_value'] = np.nan
        
        return self.stats_df
    
    def ttest(self):
        '''
        This will perform the Welch's t-test with scipy ttest_ind_from_stats
        will use equal_var=False as Welch's is always better even if var is equal
        '''
        
        # This loop will calculate the ttest
        for i in range(len(self.stats_df)):
            t,p = ttest_ind_from_stats(self.stats_df.loc[self.control]['mean'],
                                          self.stats_df.loc[self.control]['std'],
                                          self.n_cont,
                                          self.stats_df['mean'][i],
                                          self.stats_df['std'][i],
                                          self.n_test,
                                          equal_var=False)
            self.stats_df['p_value'][i] = p
            self.stats_df['t_value'][i] = t
        
        return self.stats_df
