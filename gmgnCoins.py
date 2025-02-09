import crud, schemas
from database import engine, Base, SessionLocal
from DrissionPage import WebPage, Chromium, ChromiumOptions


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def getInfo():
    # co = ChromiumOptions().headless()
    # tab = Chromium(co).latest_tab
    tab = Chromium().latest_tab

    tab.get('https://gmgn.ai/new-pair?chain=sol&tab=new_pair')
    tab.wait.load_start()  # 等待页面加载完成

    while 1:
        tab.listen.start('gmgn.ai/defi/quotation/v1/pairs/sol/new_pairs')
        res = tab.listen.wait()  # 等待并获取一个数据包
        data = res.response.body['data']['pairs']
        saveInfo(data)

def saveInfo(data):
    db = SessionLocal()
    for coin in data:
        get_coin = crud.get_coin_by_id(db=db, coin_id=coin['id'])
        if get_coin == None:
            data = crud.create_coin(db=db, coin=coin)
            db.commit()
        else:
            break

