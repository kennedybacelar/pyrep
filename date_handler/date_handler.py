import dateutil.parser
import pandas as pd
import logger

#DATE_FORMAT = "%m/%d/%y"
#-- This code takes an Pd Series object and convert the date of each row. 
#-- If a row is kept in a format not supported by dateutil lib, It is informed within the log file
#-- The function .date() assures that just the date will be returned from the datetime object
#-- Param day first set true. Means that in (e.g 01/05/20) the date to be considered is 01 May 2020

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








