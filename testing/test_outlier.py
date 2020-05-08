import unittest
import outlier
import pandas as pd 

class TestOutlier(unittest.TestCase):

  def test_check_outlier(self):

    #-- In this test the function check_outlier in outlier.py file is being called with the Data Frame
    #-- df_test as an argument. The Data Frame simulates the entries of two customers (1 and 2). 
    #-- Both of them have outliers, values 15 and 93 respectively. 
    #-- And the function check outlier return the panda.series with the string 'outlier' replacing those values.

    df_test = pd.DataFrame({'nr_conta': [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2], 'qt_kwh_med': [1, 2, 16, 4, 5, 3, 15, 16, 14, 12, 93] })
    expected_response = pd.DataFrame({'qt_kwh_med': [1, 2, 'outlier', 4, 5, 3, 15, 16, 14, 12, 'outlier']})
    pd.testing.assert_series_equal(outlier.check_outlier(df_test), expected_response.qt_kwh_med, check_names=False)

if __name__ == '__main__':
    unittest.main()

#Unit testing comparing 2 Panda Series