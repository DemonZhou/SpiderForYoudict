
import requests
''' 下载器'''
class UrlDownloader:
    def __init__(self):
        self.unfinishedset = set()
        self.finishedset = set()
        self.totalset = set()

    def Download(self,url):
        print(url)
        try :
            if (url is None):
                return None
            headers = {
                       "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36"
                       }
            response = requests.get(url,data=None,headers=headers)
            response.encoding = "utf-8"
            htmldoc = response.text
            self.finishedset.add(url)
            return htmldoc
        except Exception as e :
            print(e)
            self.unfinishedset.add(url)
        return None
