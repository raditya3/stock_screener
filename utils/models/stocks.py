from utils.models.base import Base
from sqlalchemy import Column, String, DateTime
from datetime import datetime
from typing import List, Dict


class Stock(Base):
    __tablename__ = 'stocks'
    isin = Column(String, primary_key=True)
    name = Column(String)
    symbol = Column(String)
    currency = Column(String)
    sector = Column(String)
    yahoo_ticker = Column(String)
    dw_created = Column(DateTime, default=datetime.utcnow)
    dw_modified = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    @staticmethod
    def parse_yahoo_ticker_from_isin(record: Dict[str, str]) -> str:
        symbol: str = record.get('symbol', '').replace(' ', '-')
        isin_country: str = record.get('isin', '')[:2]
        currency: str = record.get('currency', '')
        if currency == 'INR':
            return symbol + '.NS'
        else:
            return ''

    @classmethod
    def process_response(cls, response: List) -> Base:
        record: Dict[str, str] = {
            'isin': response[4],
            'name': response[0],
            'symbol': response[2],
            'currency': response[3],
            'sector': response[1]
        }
        record['yahoo_ticker'] = cls.parse_yahoo_ticker_from_isin(record.copy())
        result: Base = cls(**record)
        return result
