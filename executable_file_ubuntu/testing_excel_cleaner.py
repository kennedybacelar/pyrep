import unittest
import pandas as pd 
import excel_cleaner

class TestingExcelCleaner(unittest.TestCase):


  def test_check_columns(self):

    df_test_columns = [ 'Date', 'Shift', 'Clock', 'Number', 'Name',	'Product', 'Run Time', 'Produced' ]
    df_test_columns2 = [ 'date', 'shift', 'clock', 'number', 'name',	'product', 'run time', 'produced' ]
    df_test_columns3 = [ 'Date', 'Shit', 'Clock', 'Number', 'Name',	'Product', 'Run Time', 'Produced' ]
    df_test_columns4 = [ 'Date', 'Shit', 'Clock', 'Name',	'Product', 'Run Time', 'Produced' ]
    
    self.assertEqual(excel_cleaner.check_columns(df_test_columns), True)
    self.assertEqual(excel_cleaner.check_columns(df_test_columns2), True)
    self.assertEqual(excel_cleaner.check_columns(df_test_columns3), False)
    self.assertEqual(excel_cleaner.check_columns(df_test_columns4), False)


  def test_date_handler(self):

    df_test = pd.DataFrame({ 'date': ['25 mar 2020', '19/04/1989', '01 January 2025', '12/12/20', '2019/12/05'] })
    df_test['date'] = df_test['date'].apply(excel_cleaner.date_converter)
    expected_response = pd.DataFrame({ 'date': ['25-03-2020', '19-04-1989', '01-01-2025', '12-12-2020', '12-05-2019']})

    pd.testing.assert_series_equal(df_test.date, expected_response.date, check_names=False)
    self.assertEqual(excel_cleaner.date_converter('01 May 2020'), '01-05-2020')
    self.assertEqual(excel_cleaner.date_converter('01 at Jul 01'), '01-07-2001')
    self.assertEqual(excel_cleaner.date_converter('August 01 1957'), '01-08-1957')
    self.assertEqual(excel_cleaner.date_converter('1st March 2002'), '01-03-2002')


  def test_check_outliers(self):

    df_serie = pd.Series( [1, 2, 16, 4, 5, 3, 15, 16, 14, 12, 18, 1000000] )
    expected_response = pd.Series( [1, 2, 16 , 4, 5, 3, 15, 16, 14, 12, 18, 'Outlier'] )

    pd.testing.assert_series_equal(excel_cleaner.check_outliers(df_serie), expected_response, check_names=False)


if __name__ == '__main__':
  unittest.main()