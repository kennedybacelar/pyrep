import numpy as np 
import pandas as pd 
import csv

#---------------------------- Defining Outlier---------------------------------#
# To be considered an outlier, a value shall be lower than Median minus 2 times the
# Standard Deviation (std) or greater than Median plus two times std. 

def check_outlier(value, median, std):
  if ( (median - (2 * std)) <= value <= (median + (2 * std))):
    return value
  else:
    return 'Outlier'

df = pd.read_csv('sample.csv', sep=';')
unique_indexes = df['nr_conta'].unique()

for customer in unique_indexes:
  df_individual = (df['nr_conta'] == customer)
  median = df[df_individual]['qt_kwh_med'].median()
  standard_deviation = df[df_individual]['qt_kwh_med'].std()

  #---- Identifying the indexes of the the rows of the specific customer, so 
  # the main DataFrame can be updated according the indexes of the respective sub DataSet

  indexes = df[df_individual].index
  df['qt_kwh_med'][indexes] = df[df_individual]['qt_kwh_med'].apply(check_outlier, args=(median, standard_deviation))

# ---- Writing the CSV from the main DataSet ---------------
df.to_csv('outliers_file.csv', index=False)
