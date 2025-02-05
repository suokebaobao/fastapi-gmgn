from DrissionPage import Chromium
from Blocker import Blocker


# 创建页面对象
tab = Chromium().latest_tab


# 创建  实例
blocker = Blocker(tab)
# blocker.block("img")

# blocker.block("js")

# 访问网页
# tab.get('https://music.migu.cn/v3')
# tab.get("https://spa1.scrape.center/")
# tab.get("https://www.jd.com/")
# tab.get("https://www.gitee.com/")
tab.get("https://www.bilibili.com/")


# 
input("go on?")