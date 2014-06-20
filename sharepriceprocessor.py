""" This module processes share prices of multiple companies from a csv file
and lists for each Company year and month in which the share price is highest
"""

import sys
import os

class SharePriceProcessorException(Exception):
    pass
    
class SharePriceProcessorInvalidFileException(Exception):
    pass

class Company(object):
    """ This class represents a company

    Attributes:
      name (str): name of company.
      max_share_price (float): maximun share price of company.
      max_share_year_month (list): lsit of Years and months when share price
      was maximum.
    """

    def __init__(self, name):
        self.name = name
        self.max_share_price = -1
        self.max_share_year_month = []

    def __str__(self):
        return "Company : %s \nmax share price : %s \n(year, month) : %s \n"\
        %(self.name, self.max_share_price, \
        str(self.max_share_year_month).strip('[]').replace("'", ""))

def get_best_price_month_years(csv_file_path):
    """ Reads specified csv file conataining share prices of various companies
    and prints for each Company year and month in which the share price is
    highest

    Args:
      csv_file_path: Path of csv file which contains company and share prices
                     information.

    Returns:
      List of company objects processed.

    """
    # validate passed csv file path
    if not os.path.exists(csv_file_path):
        print "specified csv file does not exist : %s" %(csv_file_path)
        raise SharePriceProcessorInvalidFileException("specified csv file does not exist : %s" %(csv_file_path))
    # structure to maintain all objects of companies in csv file
    companies = {}
    try:
        with open(csv_file_path, 'rb') as csv_file:
            header_row = csv_file.readline().strip().split(",")
            # create companies using header
            for index in range(2, len(header_row)):
                companies[index] = Company(header_row[index])
            for row in csv_file:
                row = row.strip().split(",")
                for index in range(2, len(row)):
                    share_price = float(row[index])
                    # check if we have greater share price
                    if share_price > companies[index].max_share_price:
                        # update company's share price/year/month with this
                        # price/year/month
                        companies[index].max_share_price = share_price
                        # delete old year/month
                        del companies[index].max_share_year_month[:]
                        companies[index].max_share_year_month.append((int(row[0]),\
                                                                      row[1]))
                    # check if we have equal share price
                    elif share_price == companies[index].max_share_price:
                        # append this year/month in company's year/month as
                        # this too belongs to max share price '''
                        companies[index].max_share_year_month.append((int(row[0]),\
                                                                      row[1]))
        # print prices on console
        for company in companies.values():
            print company
        return companies.values()
    except Exception as e:
        raise SharePriceProcessorException(e)

if  __name__ == '__main__':
    if len(sys.argv) < 2:
        print "Usage : sharepriceprocessor.py <share prices csv file path>"
        exit(1)
    get_best_price_month_years(sys.argv[1])
