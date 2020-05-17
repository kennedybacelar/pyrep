import pandas as pd 
import dateutil.parser
import logger
import sys

#-- This function is responsible for checking if all columns are correct, accordingly the pre-defined

def check_columns(columns):

  result = True

  for index in range(len(columns)):
    columns[index] = columns[index].lower()

  defined_columns = [ 'Date', 'Shift', 'Clock', 'Number',	'Name',	'Product', 'Run Time', 'Produced' ]

  for label in defined_columns:
    if ( not label.lower() in columns ):
      logger.logger.info('{} - Label missing'.format(label))
      result = False
  
  return result

def date_converter(date_to_be_converted):

  try:
    try:
      converted_date = dateutil.parser.parse(date_to_be_converted, dayfirst=True).date()
    except ValueError as err:
      logger.logger.info('{}'.format(err))
      return date_to_be_converted
    return converted_date.strftime('%d-%m-%Y')
  except:
    logger.logger.info('Not possible executing function')
    return date_to_be_converted


def check_outliers(column_to_be_checked_outliers):

  def process_check_outlier(row_value, median, standard_deviation):
    if ( (median - (2 * standard_deviation)) <= row_value <= (median + (2 * standard_deviation))):
      return row_value
    else:
      return 'Outlier'

  median = column_to_be_checked_outliers.median()
  standard_deviation = column_to_be_checked_outliers.std()

  column_to_be_checked_outliers = column_to_be_checked_outliers.apply(process_check_outlier, args=(median, standard_deviation))

  return column_to_be_checked_outliers

def main():

  excel_file_path = '/home/kennedy/Documents/Dev/k10python/pyrep/executable_file_ubuntu/shift-data.xlsx'
  excel_file_path_after_processed = '/home/kennedy/Documents/Dev/k10python/pyrep/executable_file_ubuntu/processed_shift-data.xlsx'
  try:
    try:
      df = pd.read_excel(excel_file_path, sheet_name='first', converters= { 'Date' : str } )
    except ValueError as err:
      sys.exit(err)
  except:
    sys.exit('Not possible opening the file{}'.format(excel_file_path))

  check_columns(list(df.columns))
  df['Date'] = df['Date'].apply(date_converter)
  df['Produced'] = check_outliers(df['Produced'])

  df.to_excel(excel_file_path_after_processed)


if __name__ == '__main__':
  main()