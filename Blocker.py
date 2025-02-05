from DrissionPage import Chromium
from pprint import pprint as pp

class Blocker:
    def __init__(self, tab):
        """
        初始化 Requester 类
        :param tab: Chromium 的标签页对象
        """
        self.tab = tab
        self.call_back=None
        self.target_type=None
        self.target_url=None
        self.debug=False


    def _handle_request(self, **args):
        """
        请求拦截回调函数
        :param args: 请求的详细信息
        """
        if self.debug:
            pp(args)  # 打印请求信息

        r_id = args["requestId"]
        r_type = args["resourceType"]
        r_url = args["request"]["url"]
        r_headers = args["request"]["headers"]
        r_method = args["request"]["method"]
        print("\n" * 2)  # 打印分隔符

        # # 如果是图片请求，重定向到指定 URL
        # if r_type == "Image":
        #     self.tab.run_cdp("Fetch.continueRequest", requestId=r_id, url=img_url)
        #     return

        # 如果是图片请求，可以选择阻止请求
        if r_type == "Image" and self.target_type=="Image":
            self.tab.run_cdp("Fetch.failRequest", requestId=r_id, errorReason="BlockedByClient")
            return
        # 如果是 JavaScript 请求，可以选择阻止请求
        if r_type == "Script" and self.target_type=="Script":
            self.tab.run_cdp("Fetch.failRequest", requestId=r_id, errorReason="BlockedByClient")
            return
        # 如果是视频请求，可以选择阻止请求
        if r_type == "Video" and self.target_type=="Video":
            self.tab.run_cdp("Fetch.failRequest", requestId=r_id, errorReason="BlockedByClient")

        # 默认继续请求
        self.tab.run_cdp("Fetch.continueRequest", requestId=r_id)
    def _handle_request2(self, **args):
        """
        请求拦截回调函数
        :param args: 请求的详细信息
        """
        if self.debug:
            pp(args)  # 打印请求信息

        r_id = args["requestId"]
        r_type = args["resourceType"]
        r_url = args["request"]["url"]
        r_headers = args["request"]["headers"]
        r_method = args["request"]["method"]
        print("\n" * 2)  # 打印分隔符


        # 如果是图片请求，重定向到指定 URL
        if r_type == "Image" and self.target_type=="Image":
            self.tab.run_cdp("Fetch.continueRequest", requestId=r_id, url=self.target_url)
            return
        if r_url=='https://gmgn.ai/api/v1/mutil_window_token_info?device_id=2804c717-029f-4eb0-97a9-ba2576542347&client_id=gmgn_web_2025.0128.214338&from_app=gmgn&app_ver=2025.0128.214338&tz_name=Asia%2FShanghai&tz_offset=28800&app_lang=en':
            args["request"]["postData"] = '{"chain":"sol","addresses":["J3TqbUgHurQGNxWtT88UQPcMNVmrL875pToQZdrkpump"]}'
            print(args)
            self.tab.run_cdp("Fetch.continueRequest", requestId=r_id, data=args["request"]["postData"])
            return
        # 默认继续请求
        self.tab.run_cdp("Fetch.continueRequest", requestId=r_id)
        # https://chromedevtools.github.io/devtools-protocol/tot/Fetch/#method-continueRequest

    def get(self, url):
        """
        访问指定 URL
        :param url: 要访问的 URL
        """
        self.tab.get(url)
        print(f"Page Title: {self.tab.title}")
    def start(self):
        self.tab.run_cdp("Fetch.enable")  # 启用 Fetch 拦截功能
        self.tab.driver.set_callback("Fetch.requestPaused", self.call_back)  # 设置请求拦截回调 
        return self 

    def block(self,type):
        if type=="img":
            self.target_type="Image"
        if type=="js":
            self.target_type="Script"
        if type=="video":
            self.target_type="Video"
        if type=="XHR":
            self.target_type="XHR"
            
        self.call_back=self._handle_request
        self.start()
        return self
    def change(self,type,url):
        if type=="img":
            self.target_type="Image"
            self.target_url=url
        if type=="XHR":
            self.target_type="XHR"
            
        self.call_back=self._handle_request2
        self.start()
        return self
 

# 测试代码
if __name__ == "__main__":
    # 创建页面对象
    tab = Chromium().latest_tab

    baidu_logo_url = 'https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png'
    # 创建 Requester 实例
    blocker = Blocker(tab)
    # blocker.block("img")
    blocker.change(type="img",url=baidu_logo_url)
    blocker.debug=True

    # 访问网页
    # tab.get("https://spa1.scrape.center/")
    # tab.get("https://www.jd.com/")
    # tab.get("https://www.gitee.com/")
    tab.get("https://www.bilibili.com/")
    

    # 测试图片重定向
    input("go on?")