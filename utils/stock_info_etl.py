from urllib import request
import csv

from utils.models import Stock
from utils.etl_base import ETLBase
from utils.models import Base
from typing import List

CSV_FILES_URL = "https://www1.nseindia.com/content/indices/ind_nifty500list.csv"


class StockInfoETL(ETLBase):
    @staticmethod
    def job() -> None:
        data: List[Base] = []
        with request.urlopen(CSV_FILES_URL) as f:
            csvText : str = f.read().decode("utf-8")
            reader = csv.reader(csvText.splitlines())
            next(reader, None)
            for line in reader:
                line[3] = 'INR'
                data.append(Stock.process_response(line))
        ETLBase.load_data(data)
