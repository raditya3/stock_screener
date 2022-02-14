from urllib import request
import csv

from utils.models import Stock
from utils.etl_base import ETLBase
from typing import List, Dict
import re

URL_REGEX = re.compile(
    "^https?:[a-z0-9/-].*\.csv(\?[&.=,a-z0-9#].*)?$", re.IGNORECASE)


class StockNamesDataSource:
    CSV_FILES_URL = "https://www1.nseindia.com/content/indices/ind_nifty500list.csv"

    def __init__(self):
        self.source_uri = self.CSV_FILES_URL
        self.data: List[Dict[str, str]] = []
        self._populate()

    def _populate(self):
        with request.urlopen(self.source_uri) as f:
            csvText: str = f.read().decode("utf-8")
            reader = csv.reader(csvText.splitlines())
        next(reader, None)  # skip header
        self.data = map(
            lambda response: {'isin': str(response[4]).strip(),
                              'name': str(response[0]).strip(),
                              'symbol': str(response[2]).strip(),
                              'currency': 'INR',
                              'sector': str(response[1]).strip()}, reader)


class StockInfoETL(ETLBase):

    @staticmethod
    def job() -> None:
        DataSource = StockNamesDataSource()
        data = []
        for line in DataSource.data:
            data.append(Stock.process_response(line))
        ETLBase.load_data(data)
