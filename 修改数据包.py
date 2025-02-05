from DrissionPage import Chromium
from Blocker import Blocker


# 创建页面对象
tab = Chromium().latest_tab


# 创建  实例
blocker = Blocker(tab)

blocker.change(type="XHR",url="https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png")


# 访问网页
# tab.get('https://music.migu.cn/v3')
# tab.get("https://spa1.scrape.center/")
# tab.get("https://www.jd.com/")
# tab.get("https://www.gitee.com/")
tab.get("https://gmgn.ai/sol/token/IGWsOLjw_6UmLVDvoAEifansfyuqR1Fyv2t2xYFx9xBbgA8E4JhLX")


# 
input("go on?")