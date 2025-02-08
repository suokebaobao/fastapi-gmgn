from DrissionPage import ChromiumPage, WebPage, Chromium
from DrissionPage import SessionPage as Session
from Blocker import Blocker
import requests, json
from hyper.contrib import HTTP20Adapter
from datetime import datetime
import telegram



def gmgnPage():
    # 创建页面对象
    # driver = ChromiumPage()
    # wb = WebPage()
    tab = Chromium().latest_tab

    # 打开目标网页
    tab.get('https://gmgn.ai/sol/token/IGWsOLjw_6UmLVDvoAEifansfyuqR1Fyv2t2xYFx9xBbgA8E4JhLX')
    tab.wait.load_start()  # 等待页面加载完成

    # gmgn.ai/api/v1/token_prices # 获取当前价格
    tab.listen.start('gmgn.ai/api/v1/mutil_window_token_info')
    res = tab.listen.wait()  # 等待并获取一个数据包
    # print(res.url)  # 输出数据包url
    # print(res.request._data_packet)
    # print(res.request._request)

    # print(res.response.headers)  # 输出响应头
    # print(res.response.statusText)  # 输出响应状态码
    # print(res.response.body)  # 输出响应内容
    price = res.response.body['data'][0]['price']['price']
    total_supply = res.response.body['data'][0]['total_supply']
    market_value = total_supply * price
    print(market_value)

    # 执行JavaScript代码并获取结果
    with open("send.js", "r", encoding='UTF-8') as file:
        script = file.read()
    data = {
        "chain": "sol",
        "addresses": ["J3TqbUgHurQGNxWtT88UQPcMNVmrL875pToQZdrkpump",
                      "6UmLVDvoAEifansfyuqR1Fyv2t2xYFx9xBbgA8E4JhLX"]
    }
    data_str = json.dumps(data)
    post = f"var res = sendPost('{res.url}', '{data_str}');return res;"
    js_res_text = tab.run_js(script+post)
    js_res = json.loads(js_res_text)

    for coin in js_res['data']:
        market_value = coin['total_supply'] * coin['price']['price']
        print(market_value)
        if market_value > 1000000000: # 1b
            sendMsg('1b', coin)
        if market_value > 100000000: # 100m
            sendMsg('100m', coin)
        if market_value > 10000000: # 10m
            sendMsg('10m', coin)



async def sendMsg(channel, coin):
    bot = telegram.Bot("8110770762:AAE8T64ms28K0WBJXBJIlh9hjI8zsT3Ai1c")
    async with bot:
        name = coin['name']
        market_value = coin['total_supply'] * coin['price']['price']
        price = coin['price']['price']
        now_time = datetime.now().strftime('%Y-%m-%d (%H:%M:%S)')
        open_time = datetime.fromtimestamp(coin['open_timestamp'])
        holder_count = coin['holder_count']
        volume_5m = coin['price']['volume_5m']
        buy_volume_5m = coin['price']['buy_volume_5m']
        sell_volume_5m = coin['price']['sell_volume_5m']
        token = coin['address']
        url = 'https://gmgn.ai/sol/token/' + coin['address']

        text = f"{name}\n当前市值：{market_value}\n当前价格：${price}\n当前时间：{now_time}\n发币时间：{open_time}\n当前持有人数：{holder_count}\n最近5分钟正向交易量（volume）：{volume_5m}\n最近5分钟买入交易量（volume）：{buy_volume_5m}\n最近5分钟卖出交易量（volume）：{sell_volume_5m}\nToken：{token}\nGMGN地址：{url}"

        if channel == '1b': # 1b
            await bot.send_message(text=text, chat_id=6112223515)
        if channel == '100m': # 100m
            await bot.send_message(text=text, chat_id=6112223515)
        if channel == '10m': # 10m
            await bot.send_message(text=text, chat_id=6112223515)

def postPage():
    url = 'https://gmgn.ai/api/v1/mutil_window_token_info?device_id=2804c717-029f-4eb0-97a9-ba2576542347&client_id=gmgn_web_2025.0128.214338&from_app=gmgn&app_ver=2025.0128.214338&tz_name=Asia%2FShanghai&tz_offset=28800&app_lang=en'
    data = '{"chain":"sol","addresses":["6UmLVDvoAEifansfyuqR1Fyv2t2xYFx9xBbgA8E4JhLX"]}'
    session = requests.Session()
    # session.mount('https://gmgn.ai', HTTP20Adapter())
    r = session.post(url=url, data=data, headers=getHeaders(), verify=False)
    print(r.text)
    # results = json.loads(r.text)


def getHeaders():
    headers = {
        "authority": "gmgn.ai",
        "method": "POST",
        "path": "/api/v1/mutil_window_token_info?device_id=16d9a7ba-50b6-4d2c-a83e-b59b047030fe&client_id=gmgn_web_2025.0128.214338&from_app=gmgn&app_ver=2025.0128.214338&tz_name=Asia%2FShanghai&tz_offset=28800&app_lang=en",
        "scheme": "https",
        'Content-Type':'application/json',
        "accept": "application/json, text/plain, */*",
        "accept-language": "zh-CN,zh;q=0.9",
        "priority": "u=1, i",
        'Cookie':'_ga=GA1.1.892431217.1738412549; cf_clearance=9AZRW.2qfcAq.ENiNt9NkzN4rcSaKzl3qDoZm8Uy6I8-1738656268-1.2.1.1-kcDNidqGmv3fOO78ez_2jhVLEA4ZfPYL_vB6aY6Vd._g_ablKrTWQUZcWzpIF4dLW93AaJDJfYm7dzKcL4YjrCAWOjTjXPi61Ueq.y54_8Axf8zG6MSMD9RAL9wslr2zdlzqR9EIEhUC21Nny4RYjhdWZdgvjSjqvU8evOiYOwqzxx0qeL8yihW2JiXG93VJTaJTdF9vq1olGXRLcuZ7PyKpRMErhMteTDr8fIqaJIh9oMY3LeA6VvZrMZJRwvh4bPNPZtxiv8_pTe84SHPDy13DPkQqVuOuIFrXP6kWvCs; __cf_bm=C_fWnnhtIhvlVWxbP0zSkdFcW.2Hrfr2fISZRcbb1go-1738656547-1.0.1.1-0MlaqrKpIuLGTqQF9KwfzneYoJT3AWde8C9JPoHClbtx8QS6NJMsPiZ6WV7hIszwMVM8jH7NDEx1XSbDLGkElA; _ga_0XM0LYXGC8=GS1.1.1738653719.6.1.1738656753.0.0.0',
        'Origin':'https://gmgn.ai',
        'Priority':'u=1, i',
        'Referer':'https://gmgn.ai/sol/token/IGWsOLjw_6UmLVDvoAEifansfyuqR1Fyv2t2xYFx9xBbgA8E4JhLX',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
        'Sec-Ch-Ua':'"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"',
        'Sec-Ch-Ua-Arch':'"x86"',
        'Sec-Ch-Ua-Bitness':'"64"',
        'Sec-Ch-Ua-Full-Version':'"132.0.6834.160"',
        'Sec-Ch-Ua-Full-Version-List':'"Not A(Brand";v="8.0.0.0", "Chromium";v="132.0.6834.160", "Google Chrome";v="132.0.6834.160"',
        'Sec-Ch-Ua-Mobile':'?0',
        'Sec-Ch-Ua-Model':'""',
        'Sec-Ch-Ua-Platform':'"Windows"',
        'Sec-Ch-Ua-Platform-Version':'"10.0.0"',
        'Sec-Fetch-Dest':'empty',
        'Sec-Fetch-Mode':'cors',
        'Sec-Fetch-Site':'same-origin'
    }
    return headers