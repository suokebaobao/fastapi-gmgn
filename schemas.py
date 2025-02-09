#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = '__Jack__'


from datetime import datetime

from pydantic import BaseModel



class CreateCoin(BaseModel):
    name: str = 'name'


class ReadAsset(CreateCoin):
    id: int
    base_address: str
    open_timestamp: str
    quote_symbol: str
    name: str
    created_at: datetime

    class Config:
        from_attributes = True
