from URLManager.UrlCollection import UrlGenerator
from Downloader.UrlDownloader import UrlDownloader
from Parser.HtmlParser import Parser
def main() :
    urlg = UrlGenerator()
    urlset = urlg.Generate()
    ud = UrlDownloader()
    pa = Parser()
    i = 0
    for url in urlset:
        html = ud.Download(url)
        print('下载完毕开始解析')
        pa.Parse(html)
    if(ud.unfinishedset is not None):
        print('未完成的url')
        print(ud.unfinishedset)
if __name__ == "__main__" :
    main()