#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = '__Jack__'

from sqlalchemy import Column, String, Integer, BigInteger, Date, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship

from database import Base, engine



class Coin(Base):
    __tablename__ = 'coin'  # 数据表的表名

    id = Column(String(50), primary_key=True, comment='主键')
    address = Column(String(50), nullable=True, comment='address')
    base_address = Column(String(50), nullable=True, comment='base_address')
    open_timestamp = Column(String(10), nullable=True, comment='open_timestamp')
    quote_symbol = Column(String(30), comment='链')
    name = Column(String(100), nullable=True)


    created_at = Column(DateTime, server_default=func.now(), comment='创建时间', onupdate=func.now())

    # __mapper_args__ = {"order_by": updated_at}  # 默认是正序，倒序加上.desc()方法

    def __repr__(self):
        return f'{self.id}'


Base.metadata.create_all(engine) # 用于生成表 lxg20250208