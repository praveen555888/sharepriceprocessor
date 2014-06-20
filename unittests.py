"""
    Unit test cases for share prices processor module
"""

import unittest
from sharepriceprocessor import SharePriceProcessorInvalidFileException, \
           get_best_price_month_years

class TestSharePricesProcessor(unittest.TestCase):
    """
        Test class to test get_best_price_month_years functionality
    """

    def setUp(self):
        """ Set up result data"""
        # This should be the result data for supplied share prices csv file
        self.answers = {"Company 1": (4960, [(1993, 'May'), (1996, 'Aug')]),\
                       "Company 2": (4970, [(2013, 'Aug')]),\
                       "Company 3": (4990, [(1991, 'Mar'), (2006, 'Aug')]),\
                       "Company 4": (5000, [(2010, 'Nov')]),\
                       "Company 5": (4965, [(2003, 'Apr')]),\
                       "Company 6": (5000, [(1990, 'Feb')]),\
                       "Company 7": (4935, [(2001, 'Apr')]),\
                       "Company 8": (4980, [(2010, 'Nov')]),\
                       "Company 9": (4955, [(1999, 'Nov')]),\
                       "Company 10": (4990, [(1999, 'Apr')])}

    def test_non_existing_file(self):
        """ test case to test non existing file usage """
        self.assertRaises(SharePriceProcessorInvalidFileException, \
                              get_best_price_month_years, "i_do_not_exist.csv")

    def test_max_share_price(self):
        """ test case to test correctness of maximum share price """
        result = get_best_price_month_years("shareprices.csv")
        self.assertEqual(len(self.answers), len(result))
        for company in result:
            self.assertEqual(self.answers[company.name][0], \
                                             company.max_share_price)

    def test_max_years_months(self):
        """
            test case to test correctness of years and months belonging to
            maximum share price
        """
        result = get_best_price_month_years("shareprices.csv")
        self.assertEqual(len(self.answers), len(result))
        for company in result:
            for years_months in company.max_share_year_month:
                self.assertIs(years_months in self.answers[company.name][1], \
                               True)

if __name__ == '__main__':
    unittest.main()
