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
    dw_modified = Column(DateTime, default=datetime.utcnow,
                         onupdate=datetime.utcnow)

    @staticmethod
    def parse_yahoo_ticker_from_isin(record: Dict[str, str]) -> str:
        symbol: str = record.get('symbol', '').replace(' ', '-')
        currency: str = record.get('currency', '')
        if currency == 'INR':
            return symbol + '.NS'
        else:
            return ''

    @classmethod
    def process_response(cls, record: Dict) -> Base:
        record['yahoo_ticker'] = cls.parse_yahoo_ticker_from_isin(
            record.copy())
        result: Base = cls(**record)
        return result
