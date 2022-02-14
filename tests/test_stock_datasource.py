from math import floor
import unittest
from utils.stock_info_etl import StockNamesDataSource


class TestStockInfoScraper(unittest.TestCase):

    def test_data_source(self):
        DataSource = StockNamesDataSource()
        data = []
        TOTAL_DATA_COUNT = 200
        for index, line in enumerate(DataSource.data):
            if(index == TOTAL_DATA_COUNT):
                break
            values = line.values()
            if('' in values):
                continue
            if(not line['isin'].startswith('IN')):
                continue
            data.append(line)
        self.assertGreater(len(data), floor(
            TOTAL_DATA_COUNT*0.9), "Data consistency is less than 90%")


if __name__ == '__main__':
    unittest.main()
