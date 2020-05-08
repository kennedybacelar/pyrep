import unittest
import pandas as pd
import date_handler

class TestDateHandler(unittest.TestCase):

  def test_date_handler(self):

    df_test = pd.DataFrame({ 'date': ['25 mar 2020', '19/04/1989', '01 January 2025', '12/12/20', '2019/12/05'] })
    df_test['date'] = df_test['date'].apply(date_handler.date_converter)
    expected_response = pd.DataFrame({ 'date': ['25-03-2020', '19-04-1989', '01-01-2025', '12-12-2020', '12-05-2019']})

    pd.testing.assert_series_equal(df_test.date, expected_response.date, check_names=False)
    self.assertEqual(date_handler.date_converter('01 May 2020'), '01-05-2020')
    self.assertEqual(date_handler.date_converter('01 at Jul 01'), '01-07-2001')
    self.assertEqual(date_handler.date_converter('August 01 1957'), '01-08-1957')
    self.assertEqual(date_handler.date_converter('1st March 2002'), '01-03-2002')

if __name__ == '__main__':
    unittest.main()