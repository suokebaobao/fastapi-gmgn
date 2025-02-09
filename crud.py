#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = '__Jack__'

from sqlalchemy.orm import Session

import models, schemas
import hashlib, json


def create_coin(db: Session, coin: schemas.CreateCoin):
    data = {}
    data['id'] = coin['id']
    data['address'] = coin['address']
    data['base_address'] = coin['base_address']
    data['open_timestamp'] = coin['open_timestamp']
    data['quote_symbol'] = coin['quote_symbol']
    data['name'] = coin['base_token_info']['name']

    exist = db.query(models.Coin).filter(models.Coin.id == coin['id']).first()
    if exist is not None:
        pass
    else:
        db_data = models.Coin(**data)
        db.add(db_data)
        db.flush()
        # db.commit()
        # db.refresh(db_data)
        return db_data

def get_coin_by_id(db: Session, coin_id: str):
    coin = db.query(models.Coin).filter(models.Coin.id == coin_id).first()
    return coin

def get_coin_base_address(db: Session, quote_symbol: str, slice: int):
    coins = (db.query(models.Coin.base_address).order_by(models.Coin.created_at.desc(), models.Coin.id)
             .filter(models.Coin.quote_symbol == quote_symbol).slice(10*slice-10,10*slice).all())
    return [address[0] for address in coins]
