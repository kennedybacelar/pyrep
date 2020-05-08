import pandas as pd 

#----------- Switching off the SettingWithCopyWarning: -------------------------#
pd.set_option('mode.chained_assignment', None) 

def check_outlier(df):

  def process_check(value, media, std):
    if ( (median - (2 * std)) <= value <= (median + (2 * std))):
      return value
    else:
      return 'outlier'

  unique_indexes = df['nr_conta'].unique()

  for customer in unique_indexes:
    df_individual = (df['nr_conta'] == customer)
    median = df[df_individual]['qt_kwh_med'].median()
    standard_deviation = df[df_individual]['qt_kwh_med'].std()
    indexes = df[df_individual].index
    df['qt_kwh_med'][indexes] = df[df_individual]['qt_kwh_med'].apply(process_check, args=(median, standard_deviation))

  return df['qt_kwh_med']